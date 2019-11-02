from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from analysis import *

app = Flask(__name__)


UJ_Dict = dict()


@app.route('/')
def home():
    return 'Hello, World'

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    sub = Submission(phone_number=number, text=message_body)
    UJ = UserJournal(phone_number=number)

    UJ.add_submission(submission=sub)

    UJ_Dict[number] = UJ


    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == '__main__':
    app.run()
