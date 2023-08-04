from django import forms
from art_sharing_app.models import Artwork, ArtworkComment, Userprofile, User
from django.contrib.auth.forms import UserCreationForm

class ArtworkForm(forms.ModelForm):
    class Meta:
        model=Artwork
        fields= [
            "titre",
            "image",
            "legende",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model= ArtworkComment
        fields = [
            "comment",
        ]

class Modifprof(forms.ModelForm):
    class Meta:
        model= Userprofile
        fields = [
            "image",
            "bio",
        ]

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username",
                   "email",
                    "password1", 
                    "password2"
                ]