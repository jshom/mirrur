from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from analysis import analysis as an
from analysis import message_generator as mes

app = Flask(__name__)

UJ_Dict = dict()

@app.route('/')
def home():
    return 'Hello, World'

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    sub = an.Submission(text=message_body)
    UJ = an.UserJournal(phone_number=number)

    UJ.add_submission(submission=sub)

    report = an.Report(user_journal=UJ)
    report.generate()
    report.compress()
    message = mes.message_generator(report.compressed_result)

    UJ_Dict[number] = UJ

    resp = MessagingResponse()
    resp.message('number:{} \n message: {}'.format(number, message))
    return str(resp)

if __name__ == '__main__':
    app.run()
