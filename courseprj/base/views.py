from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.db.models import Count

from .forms import CommentForm, RoomForm
from .models import Message, Room, Topic

# Create your views here.


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:  # noqa: E722
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username OR Password does not exist")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request=request, user=user)
            return redirect("home")
        else:
            messages.error(request, "An error occured during registration")

    return render(request, "base/login_register.html", {"form": form})


def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )

    room_count = rooms.count()
    topics = Topic.objects.annotate(room_count=Count("room"))
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count,
        "room_messages": room_messages,
    }
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all().order_by("-created_at")
    participants = room.participants.all()

    if request.user.is_authenticated:
        form = CommentForm()
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.user = request.user
                message.room = room
                message.save()
                room.participants.add(request.user)
                return redirect("room", room.id)
    else:
        form = CommentForm()

    context = {
        "room": room,
        "comments": messages,
        "form": form,
        "participants": participants,
    }

    return render(request, "base/room.html", context)


def userProfile(request, username):
    user = User.objects.get(username=username)
    rooms = user.room_set.all()
    messages = user.message_set.all()
    topics = Topic.objects.annotate(room_count=Count("room"))
    context = {
        "user": user,
        "rooms": rooms,
        "room_messages": messages,
        "topics": topics,
        "room_count": Room.objects.count(),
    }
    return render(request, "base/profile.html", context)


@login_required(login_url="login")
def updateUser(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST.get("first_name", "")
        user.username = request.POST.get("username", user.username)
        user.email = request.POST.get("email", "")
        user.save()

        profile = user.profile
        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]
        profile.bio = request.POST.get("bio", "")
        profile.save()

        return redirect("user-profile", username=user.username)

    return render(request, "base/update_user.html", {"user": user})


@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            room.participants.add(request.user)

            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})


@login_required(login_url="login")
def deleteComment(request, pk):
    comment = Message.objects.get(id=pk)
    if request.user != comment.user:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        comment.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": comment})


@login_required(login_url="login")
def editComment(request, pk):
    comment = Message.objects.get(id=pk)
    if request.user != comment.user:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("room", comment.room.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, "base/edit_comment.html", {"form": form})
