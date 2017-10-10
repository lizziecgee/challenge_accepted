# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from .forms import NinjaRegistrationForm

def index(request):
    return render(request, 'ninjas/index.html')

class RegisterView(View):
    def get(self, request):
        context = {
        'registration_form': NinjaRegistrationForm()
        }
        return render(request, 'ninjas/register.html', context)
  
    def post(self, request):
        print request.POST
        return redirect(reverse('ninjas:dashboard'))

class LoginView(View):
    def get(self, request):
        return render(request, 'ninjas/login.html')
  
    def post(self, request):
        pass

def dashboard(request):
    return render(request, 'ninjas/dashboard.html')
