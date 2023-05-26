from django import forms
from django.forms import ModelForm
from accounts.models import profile
from .models import post


class profile_form(ModelForm):
    # Meta: is a Django word use to modify the forms.
    class Meta:
        model = profile
        fields = ('name', 'lastname', 'username', 'email', 'phone', 'date_of_birth', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'settings-inputs', 'placeholder': 'name'}),
            'lastname': forms.TextInput(attrs={'class': 'settings-inputs', 'placeholder': 'lastname'}),
            'username': forms.TextInput(attrs={'class': 'settings-inputs', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'settings-inputs', 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'settings-inputs', 'placeholder': 'phone'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'settings-inputs', 'type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'settings-inputs', 'placeholder': 'description'}),
        }
