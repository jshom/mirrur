from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from analysis import analysis as an

app = Flask(__name__)

UJ_Dict = dict()

@app.route('/')
def home():
    return 'Hello, World'

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    first_time = (number in UJ_Dict.keys)
    resp = ''

    if first_time:
        sub = an.Submission(phone_number=number, text=message_body)
        UJ = an.UserJournal(phone_number=number)
        UJ.add_submission(submission=sub)
        UJ_Dict[number] = UJ
        resp = MessagingResponse()
        resp.message("Hey, from what I can tell, this is your first time using Mirrur. That's ok. \n Mirrur is a place for you to jot down any of your thoughts. Mirrur is here to listen.")
    else:


    return str(resp)

if __name__ == '__main__':
    app.run()
