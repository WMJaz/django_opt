from django.shortcuts import render
from django.http import JsonResponse
from ..models import OTP
from .utils import generate_8characters_otp
from .smart_api import send_sms_http

def request_otp(request):
    if request.method == 'POST':
        phone = request.POST.get("mobileno")
        
        if not phone:
            return JsonResponse({
                'status': 'error',
                'message': 'Sending failed',
                'data': None
            }, status=400)
        
        checkifexist_otp = OTP.objects.filter(phone_number=phone).order_by('-created_at').first()
        
        if checkifexist_otp and not checkifexist_otp.is_expired():
            code = checkifexist_otp.code
        else:
            code = generate_8characters_otp()
            OTP.objects.create(phone_number=phone, code=code)
            
        if not send_sms_http(phone, f"Your One-Time-Pin is {code}. Valid for {OTP.VALIDITY} mins"):
            return JsonResponse({
                'status': 'failed',
                'message': 'OTP send failed',
                'data': None
            }, status=400)
        
        return JsonResponse({
            'status': 'success',
            'message': 'OTP sent successfully',
            'data': None
        }, status=200)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method',
        'data': None
    }, status=400)


def verify_otp(request):
    if request.method == 'POST':
        phone = request.POST.get("mobileno")
        code = request.POST.get("otp")
        
        try:
            otp = OTP.objects.filter(phone_number=phone, code=code).latest('created_at')
        except OTP.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid OTP',
                'data': None
            }, status=200)

        if otp.is_expired():
            return JsonResponse({
                'status': 'error',
                'message': 'OTP Already expired',
                'data': None
            }, status=400)
        if otp.validated:
            return JsonResponse({
                'status': 'error',
                'message': 'OTP already validated',
                'data': None
            }, status=400)
        
        otp.validated = True
        otp.save()
        return JsonResponse({
            'status': 'success',
            'message': 'OTP verified successfully',
            'data': None
        }, status=200)
        
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method',
        'data': None
    }, status=400)