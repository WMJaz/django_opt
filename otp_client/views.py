from django.shortcuts import render

def home(request):
    return render(request, 'otp_client.html')