from django import forms
from django.forms import ModelForm
from .models import *
from django.db import transaction


class AnotatedForm(ModelForm):

    class Meta:
        model = AnotatedJPHIV
        fields = ['judul', 'tanggal', 'added_by', 'kategori', 'url','download', 'bibliografi', 'anotated', 'tag']

    @transaction.atomic
    def save(self, request):
        user = super().save(commit=False)
        user.added_by = request.user.username
        user.save()
        return user