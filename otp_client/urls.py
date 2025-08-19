from django.urls import path
from . import views
from .controllers import otp_controllers, smssender_controller

urlpatterns = [
    path('', views.render_applists_page, name='render_home'),
    path('applists/', views.render_applists_page, name='render_applists'),
    
    # OTP Modules
    path('otp/', views.render_otp_page, name='render_otp'),
    path('otp/request-otp/', otp_controllers.request_otp, name='request_otp'),
    path('otp/verify-otp/', otp_controllers.verify_otp, name='verify_otp'),
    
    path('sms/', views.render_sms_page, name='render_sms'),
    path('sms/send-sms', smssender_controller.send_sms_httprequest_single, name='send_sms'),
]