from django.shortcuts import render
import random
import math
from django.conf import settings
from twilio.rest import Client

def mobile_otp():
    numbers = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += numbers[math.floor(random.random()*10)]
    return OTP



def view_otp(request):
    template_name = "otp_template/otp.html"
    client = Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
    message = client.messages.create(
            body = f'Your otp for withdraw cash {mobile_otp()}',
            from_ = "+1 406 719 7127",
            to =('+919899651827')
            )
    return render(request, template_name,context={"message":message.body ,"to_number":message.to})


# function to send otp to mobile number

# class Message_handler:
#     phone_number = None
#     otp = None
    
#     def __init__(self,phone_number):
#         self.phone_number = phone_number
#         self.otp = mobile_otp()
#         print('ur otp is::',self.otp)

#     def _send_otp_on_phone(self):
#         client = Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
#         message = client.messages.create(
#             body = f'Your otp for withdraw cash {self.otp}:',
#             from_ = "+1 406 719 7127",
#             to =self.phone_number
#             )