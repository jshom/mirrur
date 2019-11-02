from datetime import datetime

class Submission:
    """Class for text submittion"""
    def __init__(self, phone_number, text):
        self.phone_number = phone_number
        self.text = text
        self.timestamp = datetime.now()

    def __str__(self):
        return "phone_number: {}\ntext: {}\ntimestamp: {}".format(self.phone_number, self.text, self.timestamp)

class UserJournal:
    """Time series class"""

    def __init__(self, phone_number):
        self.submissions = []
        self.phone_number = phone_number

    def add_submission(self, submission):
        self.submissions.append(submission)

    def __str__(self):
        str = ""
        for submission in self.submissions:
            str += '-------------------\n' + submission.__str__() + '\n'
        return str


class Report:
    """Class to hold report of multiple analysis results"""
    def __init__(self, user_journal):
        self.analysis_list = []
        self.user_journal = user_journal
        self.results = {}

    # using Analysis class
    def add_analysis(analysis):
        # run function and set result to the result dictionary under the result
        self[analysis.result_name] = analysis.run(self.user_journal)
        print(type(analysis))
        if (type(analysis) != "")


# exmaple analysis function

def example_analysis_function(user_journal):
    return 1

class Analysis:
    """General class template for anaysis on user journal"""
    # leave time start and time end to do
    #   partial time series analysis if time allows
    def __init__(self, function, time_start=None, time_end=None):
        self.user_journal = user_journal
        self.function = function
        self.result_name = result_name

    def run(user_journal):
        return self.analysis_function(user_journal)
