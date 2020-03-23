from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


from .decorators import visitor_required
from .forms import VisitorSignUpForm, StaffSignUpForm
from .models import CustomUser
from django.views.generic import TemplateView


class VisitorSignUpView(CreateView):
    model = CustomUser
    form_class = VisitorSignUpForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'visitor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('homepage')


class StaffSignUpView(CreateView):
    model = CustomUser
    form_class = StaffSignUpForm
    template_name = 'registration/log.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('homepage')