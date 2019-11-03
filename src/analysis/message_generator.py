from analysis import *
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
def message_generator(value):
    message = ""
    if value >= 0 and value < 0.1:
        message = "uh oh"
    elif value >= 0.1 and value < 0.2:
        message = "are you okay?"
    elif value >= 0.2 and value < 0.3:
        message = "are you okay?"
    elif value >= 0.3 and value < 0.4:
        message = "Howdy!"
    elif value >= 0.4 and value < 0.5:
        message = "Howdy!"
    elif value >= 0.5 and value < 0.6:
        message = "Howdy!"
    elif value >= 0.6 and value < 0.7:
        message = "Howdy!"
    elif value >= 0.7 and value <= 0.8:
        message = "Howdy!"
    return message