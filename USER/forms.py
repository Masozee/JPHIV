from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.db import transaction
from django.contrib.auth.models import User
from django.forms.utils import ValidationError

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user

class VisitorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, )
    last_name = forms.CharField(max_length=100, )
    email = forms.EmailField(max_length=150, )
    Organisasi = forms.CharField(max_length=100,)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','Organisasi',
                  'email', 'password1', 'password2',)


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','Organisasi',
                  'email', 'password1', 'password2',)