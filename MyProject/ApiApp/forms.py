from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'author_name',
            'email',
            'age'            
        ]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]


