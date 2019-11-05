from analysis import *
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
def message_generator(value, report_id=None):
    message = ""
    if value >= 0 and value < 0.1:
        message = "It sounds like you're in need of some help. If you need someone to talk to call the National Suicide Hotline: 1-800-273-8255. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.1 and value < 0.2:
        message = "It sounds like you could be feeling better. Mirrur recomends you find someone to talk to. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.2 and value < 0.35:
        message = "Seems like something is wrong. Try immersing yourself with good company. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.35 and value < 0.4:
        message = "Keep on fighting! See you tomorrow!"
    elif value >= 0.4 and value < 0.5:
        message = "It's alright! Can't wait to hear from you tomorrow!"
    elif value >= 0.5 and value < 0.6:
        message = "Nice! Can't wait to hear from you tomorrow!"
    elif value >= 0.6 and value < 0.7:
        message = "Good to hear from you, seems like you're doing well! Can't wait to hear from you tomorrow!"
    elif value >= 0.7:
        message = "Sounds like you're doing good! Mirrur is always here to listen!"
    return message
