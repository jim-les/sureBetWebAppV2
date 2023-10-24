from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

def custom_login(request):
    if request.user.is_authenticated:
        return redirect(mainpage)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainpage')
        
        else:
            messages.error(request, "Invalid userame or password.")
            return render(request, "authentication/login.html", context={'message' : "Invalid userame or password."})

    return render(request, "authentication/login.html")

def custom_logout(request):
    logout(request)
    return redirect('login')

def signUp(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)

        # user.profile.phone = phone
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')  # Redirect to the login page after successful registration


    return render(request, "authentication/signUp.html")

import time, random
def get_betika_users():
    n = random.randint(1, 10)
    time.sleep(10)
    return n 

def mainpage(request):
    get_betika_user = 3
    get_betika_user =+ get_betika_users()

    # betikaSubscribers = 
    games = AdminGame.objects.all()
    betikagames = BetikaJackpotGame.objects.all()
    sportpesagames = SportPesaJackpotGame.objects.all()
    subscriptiongames = SubscriptionGame.objects.all()
    context = {'get_betika_user': get_betika_user, 'games' : games, 'betikagames' : betikagames, 'sportpesagames' : sportpesagames, 'subscriptiongames' : subscriptiongames}
    # context = {'betikagames' : betikagames, "games": games}
    return render(request, 'main/index.html', context)

# views.py
from django.http import JsonResponse
import requests
from django.http import HttpResponse

from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0799522900'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")

