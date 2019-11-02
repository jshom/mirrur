from datetime import datetime

class Submission:
    """Class for text submittion"""
    def __init__(self, text):
        self.text = text
        self.timestamp = datetime.now()

    def __str__(self):
        return "text: {}\ntimestamp: {}".format(self.text, self.timestamp)

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

    # using Analysis class add to list of analysis to run to generate report
    def add_analysis(self,analysis):
        # run function and set result to the result dictionary under the result
        self.analysis_list.append(analysis)

    def generate(self):
        # run function and set result to the result dictionary under the result
        for analysis in self.analysis_list:
            self.results[analysis.result_name] = analysis.run(self.user_journal)

    def log(self):
        print("====================")
        print("Report for: {}".format(self.user_journal.phone_number))
        print("====================")
        print(self.results)

class Analysis:
    """General class template for anaysis on user journal"""
    # leave time start and time end to do
    #   partial time series analysis if time allows
    def __init__(self, function, result_name, time_start=None, time_end=None):
        self.function = function
        self.result_name = result_name

    def run(self, user_journal):
        return self.function(user_journal)
