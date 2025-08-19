# otp_app/utils.py
import random

def generate_8characters_otp(length=8):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])