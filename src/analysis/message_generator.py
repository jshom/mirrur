from analysis import *
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
def message_generator(value, report_id=None):
    message = ""
    if value >= 0 and value < 0.1:
        message = "It sounds like you're in need of some help. If you need someone to talk to call the National Suicide Hotline: 1-800-273-8255. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.1 and value < 0.2:
        message = "It sounds like you could be feeling better. Mirrur recomends you find someone to talk to. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.2 and value < 0.3:
        message = "Are you okay? You are not alone in how you're feeling. Try immersing yourself with good company. (https://mirrur.xyz/ui/report/" + report_id + ")"
    elif value >= 0.3 and value < 0.4:
        message = "Keep fighting. I am here to listen so feel free to keep going."
    elif value >= 0.4 and value < 0.5:
        message = "It's alright. Mirrur is always here. Feel free to keep going."
    elif value >= 0.5 and value < 0.6:
        message = "You're doing good! Feel free to keep going."
    elif value >= 0.6 and value < 0.7:
        message = "You're doing good! Feel free to keep going."
    elif value >= 0.7:
        message = "Sounds like you're doing good! Come back anytime!"
    return message
