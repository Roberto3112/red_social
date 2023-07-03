from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class user_register_form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username','required':'True'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email','required':'True'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password','required':'True'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password','required':'True'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
