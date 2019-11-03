from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import Message, MessagingResponse
from analysis import analysis as an
from analysis import message_generator as mes
from hashlib import md5
from analysis import heuristics as heuristics

app = Flask(__name__)

UJ_Dict = dict()
Report_Dict = dict()

analysis_dict = {
    "polarization": an.Analysis(heuristics.polarization_heuristic, "polarization"),
    "general_sentiment": an.Analysis(heuristics.general_sentiment_analysis, "general_sentiment"),
    "latest_sentiment": an.Analysis(heuristics.latest_sentiment_analysis, "latest_sentiment")
}

@app.route('/')
def home():
    return 'Hello, World'

@app.route('/report/<string:report_id>')
def fetch_report(report_id):
    report = Report_Dict.get(report_id, None)

    # Error check if report not found
    if (not report):
        return jsonify(
            success= False,
            # full_text=None,
            submissions=None,
            results=None,
            average_result=None
        )

    # return report
    return jsonify(
        success= True,
        # full_text=report.user_journal.full_text,
        submissions=list(map(lambda s: s.text, report.user_journal.submissions)),
        results=report.results,
        average_result=report.compressed_result
    )

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print(message_body)

    # generate submission
    sub = an.Submission(text=message_body)

    # check if phone_number is sending as first time
    first_time = number not in UJ_Dict.keys()
    if first_time:
        # create user journal for first timers
        UJ = an.UserJournal(phone_number=number)
        UJ_Dict[number] = UJ # note don't add first text
        # message for first timers
        message = "Hey, from what I can tell, this is your first time using Mirrur. That's ok. \n Mirrur is a place for you to jot down any of your thoughts. Mirrur is here to listen. For now, let me know how your day went."
        # send message
        resp = MessagingResponse()
        resp.message(message)
        return str(resp)

    # common case
    UJ = UJ_Dict[number]
    UJ.add_submission(submission=sub)
    # add analysis to use in report
    report = an.Report(user_journal=UJ)
    report.add_analysis(analysis_dict["polarization"])
    report.add_analysis(analysis_dict["general_sentiment"])
    report.add_analysis(analysis_dict["latest_sentiment"])
    # generate report
    report.generate()
    report.log()
    # save report with ts of last submission
    print(sub.timestamp)
    report_id = md5(str(sub.timestamp).encode('utf-8')).hexdigest()
    print("report_id: {}".format(report_id))
    Report_Dict[report_id] = report
    # generate message to send based on happiness probabiltiy (0-1)
    msg = mes.message_generator(report.compressed_result)
    # return the message

    # TODO: when you hit below 0.3 send the report link
    resp = MessagingResponse()
    resp.message(msg)
    return str(resp)

if __name__ == '__main__':
    app.run()
