from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CommentsForm(forms.Form):
    name = forms.CharField(max_length=150, initial='Guest')
    text = forms.CharField(widget=forms.Textarea)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Імя', widget=forms.TextInput(attrs={'placeholder': 'Імя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}

    field_order = ['username', 'password1', 'password2']


class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(label='Імя', widget=forms.TextInput(attrs={'placeholder': 'Імя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = {'username', 'password'}

    field_order = ['username', 'password']
