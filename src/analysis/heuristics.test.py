from analysis import *
import heuristics

uj = UserJournal(phone_number="183402")
uj.add_submission(Submission(text="I am really loving this"))
uj.add_submission(Submission(text="I can't stand this right now."))

r = Report(uj)

a = Analysis(function=heuristics.example, result_name="example")
b = Analysis(function=heuristics.determiner_heuristic, result_name="polarized_determiners")

r.add_analysis(a)
r.add_analysis(b)

r.generate()
r.log()
