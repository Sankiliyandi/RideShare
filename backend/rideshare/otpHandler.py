from twilio.rest import Client


def otp(phoneNo,code):
    
    acc_sid="ACf9ed85edb96f70568990c0fdca030946"
    token="0bdd0423b2beaf346bf912a7f7e70d04"
    client=Client(acc_sid,token)
    messageOTP=client.messages.create(
        body='your RideShare registration otp:'+code,
        from_="+12344075073",
        to=phoneNo
    )
    print(messageOTP.sid) 

import requests
import random
from django.conf import settings
def send_otp_to_phone(pn,otp):
    try:
       # otp = random.randint(1000, 9999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/+91{pn}/{otp}'
        response = requests.get(url)
       # return otp
    except Exception as e:
        return None