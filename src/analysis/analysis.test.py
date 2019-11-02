from analysis import *

uj = UserJournal(phone_number="183402")

s0 = Submission(phone_number="183402", text="I am really loving this")
s1 = Submission(phone_number="183402", text="I can't stand this right now.")

uj.add_submission(s0)
uj.add_submission(s1)

# example print userjournal
print(uj)
# example print single submission
print(s0)

# ------------------
# Test for Analsysis
# ------------------

r = Report(user_journal)
a = Analysis(function=example_analysis_function, result_name="example_result")
