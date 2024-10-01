from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from dashboard.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from dotenv import load_dotenv
import os
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordChangeView,
    PasswordResetConfirmView
)
from dashboard.forms import (
    RegistrationForm,
    LoginForm,
    UserPasswordResetForm,
    UserSetPasswordForm,
    UserPasswordChangeForm
)


# Create your views here.

load_dotenv()

# Dashboard
def analytics(request):
  context = {
    'parent': 'dashboard',
    'segment': 'analytics'
  }
  return render(request, 'pages/dashboards/analytics.html', context)

def sales(request):
  context = {
    'parent': 'dashboard',
    'segment': 'sales'
  }
  return render(request, 'pages/dashboards/sales.html', context)

def smart_home(request):
  context = {
    'parent': 'dashboard',
    'segment': 'smart_home'
  }
  return render(request, 'pages/dashboards/smart-home.html', context)

# Applications
def test(request):
  context = {
    'parent': 'applications',
    'segment': 'test'
  }
  return render(request, 'pages/applications/test.html', context)

# Blockchain
def nft(request):
	context = {
		'parent': 'blockchain',
		'segment': 'nft'
	}
	return render(request, 'pages/blockchain/nft.html', context)

def registration(request):
	herdeiros = ['Alex', 'Jhon', 'Lewis', 'Daniel'] # Variável somente para o carrousel da partial owners.html
	return render(request, 'pages/blockchain/registration.html', {'herdeiros': herdeiros})

def marketplace(request):

	geo_points = [
        
        {
            "lat": -23.22155,
            "lng": -44.71992,
            "name": "Paraty/RJ",
            "description": "Mercado Municipal do Produtor Rural de Paraty.",
            "image": "https://i.postimg.cc/7PcgqgTq/Paraty.png"
        }        
    ]

	context = {
		'parent': 'blockchain',
		'segment': 'marketplace',
		'geo_points': geo_points
	}
	return render(request, 'pages/blockchain/marketplace.html', context)

def defi(request):
	cryptos = get_cryptos()
	crypto_paginated = add_pagination(request, cryptos, 50)
	context = {
    	'objects': crypto_paginated,
    }
	return render(request, 'pages/blockchain/defi.html', context)

def token(request):
	context = {
		'parent': 'blockchain',
		'segment': 'token'
	}
	return render(request, 'pages/blockchain/token.html', context)

def storage(request):
	context = {
		'parent': 'blockchain',
		'segment': 'storage'
	}
	return render(request, 'pages/blockchain/storage.html', context)

def emporium(request):

	geo_points = [
        
        {
            "lat": -23.22155,
            "lng": -44.71992,
            "name": "Paraty/RJ",            
            "image": "https://i.postimg.cc/7PcgqgTq/Paraty.png"
        }        
    ]

	context = {
		'parent': 'blockchain',
		'segment': 'emporium',
		'geo_points': geo_points
	}
	return render(request, 'pages/blockchain/emporium.html', context)


# Authentication -> Login
class BasicLoginView(LoginView):
  template_name = 'accounts/signin/basic.html'
  form_class = LoginForm

# Authentication -> Register
def basic_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/basic-login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/signup/basic.html', context)

# Authentication -> Lock
def basic_lock(request):
  return render(request, 'accounts/lock/basic.html')

# Authentication -> Reset
class BasicPasswordResetView(PasswordResetView):
  template_name = 'accounts/reset/basic.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/reset-confirm/basic.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/change/basic.html'
  form_class = UserPasswordChangeForm

# Authentication 2FA -> Verification
def basic_verification(request):
  return render(request, 'accounts/verification/basic.html')


# Error
def error_404(request):
  return render(request, 'accounts/error/404.html')

def error_500(request):
  return render(request, 'accounts/error/500.html')

def logout_view(request):
  logout(request)
  return redirect('/accounts/basic-login/')