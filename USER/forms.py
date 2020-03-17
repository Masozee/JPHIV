from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.db import transaction
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
    google_scholar_id = forms.CharField(max_length=50)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','Organisasi','google_scholar_id',
                  'email', 'password1', 'password2',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_visitor = True
        user.save()
        return user
