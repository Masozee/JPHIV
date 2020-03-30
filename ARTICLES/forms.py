from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.db import transaction

class AnotForm(forms.ModelForm):
    judul = forms.CharField(max_length=300, widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Tulis Judul Annotated Bibliography'
            }
        ))
    tanggal = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y', attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language':"en"}),
            input_formats=('%d/%m/%Y', )
    )
    sumber = forms.CharField(max_length=120, widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Jurnal of Biology'
            }
        ))
    Author = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': '"Arfijanto, M. V.", "Diansyah, M. N.", "Kameoka, M.", "Khairunisa, S. Q.", "Kotaki, T.",'
            }
        ) )
    volume = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': '01-11'
        }
    ))
    DOI_number = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': '10.1007/s10461-015-1198-4'
        }
    ))
    DOI_URL = forms.URLField( widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'https://doi.org/10.1109/5.771073'
        }
    ))
    doctype = forms.CharField(max_length=4, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'jpeg, pdf, docx, doc'
        }
    ))
    url = forms.URLField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5337410/pdf/jve-2-27.pdf'
        }
    ))
    bibliografi = forms.CharField(widget=CKEditorWidget())

    tags = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm',
            'placeholder': '"HIV AIDS", "obat-obatan" '
        }
    ), )


    class Meta:
        model = AnotatedJPHIV
        exclude = ('added_by','visit_num')

