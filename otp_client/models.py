from django.db import models
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    VALIDITY = 5
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=self.VALIDITY)
    
class SMSLogs(models.Model):
    class SMSLogs_Choices(models.TextChoices):
        QUEUED      =   '0', 'FAILED'
        SUCCESS     =   '1', 'SUCCESS'
        FAILED      =   '2', 'FAILED'
    
    pk_smslogs = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=10,choices=SMSLogs_Choices.choices)
    created_at = models.DateTimeField(auto_now_add=True)