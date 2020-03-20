from django import forms
from django.forms import ModelForm
from .models import *
from django.db import transaction

class AnotForm(forms.ModelForm):
    class Meta:
        model = AnotatedJPHIV
        exclude = ('added_by','visit_num')

