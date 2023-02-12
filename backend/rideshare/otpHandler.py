from http import client
from twilio.rest import Client




def otp(phoneNo,code):
    
    acc_sid="ACf9ed85edb96f70568990c0fdca030946"
    token="ca79f75ed614cb655f315b09f9c903dd"
    client=Client(acc_sid,token)
    messageOTP=client.messages.create(
        body='your RideShare registration otp:'+code,
        from_="+12344075073",
        to=phoneNo
    )
    print(messageOTP.sid)