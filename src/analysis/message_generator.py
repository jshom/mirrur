from analysis import *
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
def message_generator(value):
    message = ""
    if value >= 0 and value < 0.1:
        message = "It sounds like you're in need of some help. If you need someone to talk to call the National Suicide Hotline: 1-800-273-8255"
    elif value >= 0.1 and value < 0.2:
        message = "It sounds like you could be feeling better. Mirrur recomends you find someone to talk to"
    elif value >= 0.2 and value < 0.3:
        message = "Are you okay? You are not alone in how you're feeling. Try immersing yourself with good company"
    elif value >= 0.3 and value < 0.4:
        message = "Keep fighting. can't wait to hear from you tomorrow"
    elif value >= 0.4 and value < 0.5:
        message = "Keep it going! can't wait to hear from you tomorrow"
    elif value >= 0.5 and value < 0.6:
        message = "Nice! can't wait to hear from you tomorrow"
    elif value >= 0.6 and value < 0.7:
        message = "Sounds good! can't wait to hear from you tomorrow"
    elif value >= 0.7 and value <= 0.8:
        message = "Sounds like you're having a good day"
    return message