from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("profile/<str:username>/", views.userProfile, name="user-profile"),
    path("topics/", views.topicsPage, name="topics"),
    path("activities/", views.activitiesPage, name="activities"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),
    path("delete-comment/<str:pk>/", views.deleteComment, name="delete-comment"),
    path("update-user/", views.updateUser, name="update-user"),
    path("edit-comment/<str:pk>/", views.editComment, name="edit-comment"),
]
