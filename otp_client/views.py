from django.shortcuts import render
from . import controllers

def render_applists_page(request):
    return render(request, 'applists.html')

def render_otp_page(request):
    return render(request, 'otp_client.html')

def render_sms_page(request):
    return render(request, 'smsapp.html')