from django.shortcuts import render
from django.http import JsonResponse
from ..models import SMSLogs
from .smart_api import send_sms_http


def send_sms_httprequest_single(request):
    if request.method == 'POST':
        phone = request.POST.get("mobileno")
        message = request.POST.get("message")
        
        if not phone:
            return JsonResponse({
                'status': 'error',
                'message': 'Sending failed',
                'data': None
            }, status=400)
            
        if not message:
            return JsonResponse({
                'status': 'error',
                'message': 'Sending failed',
                'data': None
            }, status=400)
            
        if not send_sms_http(phone, f'{message}'):
            SMSLogs.objects.create(
                phone_number=phone, 
                message=message,
                status=SMSLogs.SMSLogs_Choices.FAILED
            )
            return JsonResponse({
                'status': 'failed',
                'message': 'Message send failed',
                'data': None
            }, status=400)
        
        SMSLogs.objects.create(
                phone_number=phone, 
                message=message,
                status=SMSLogs.SMSLogs_Choices.SUCCESS
        )
        return JsonResponse({
            'status': 'success',
            'message': 'Message sent successfully',
            'data': None
        }, status=200)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method',
        'data': None
    }, status=400)