from django.db import models
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    VALIDITY = 5
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=self.VALIDITY)
