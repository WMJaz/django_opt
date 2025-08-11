# otp_app/sms_service.py
import requests
import urllib.parse

SMART_API_USERNAME = "misd.pafhrmc@gmail.com"
SMART_API_PASSWORD = "P@fhrmc1"
SMART_API_REGISTERED = "1"  # e.g. PAFHRMC

def send_sms_http(contact_number, sms_message):
    phone_no = urllib.parse.quote(contact_number)
    msg = urllib.parse.quote(sms_message)
    url = (
        "https://messagingsuite.smart.com.ph/cgphttp/servlet/sendmsg"
        f"?username={SMART_API_USERNAME}"
        f"&password={SMART_API_PASSWORD}"
        f"&destination={phone_no}"
        f"&text={msg}"
        f"&registered={SMART_API_REGISTERED}"
    )
    response = requests.get(url, timeout=5)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code != 200:
        return False
    return True

