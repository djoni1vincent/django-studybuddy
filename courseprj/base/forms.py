from django import forms
from django.forms import ModelForm

from .models import Message, Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["topic", "name", "description"]


class CommentForm(ModelForm):
    class Meta:
        model = Message
        fields = ["body"]
        widgets = {"body": forms.Textarea(attrs={"rows": 2, "cols": 20})}
