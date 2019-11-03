from analysis import *
import heuristics

uj = UserJournal(phone_number="183402")
uj.add_submission(Submission(text="I am really loving this"))
uj.add_submission(Submission(text="I can't stand this right now."))

r = Report(uj)

a = Analysis(function=heuristics.example, result_name="example")
b = Analysis(function=heuristics.polarization_heuristic, result_name="polarization")
c = Analysis(function=heuristics.general_sentiment_analysis, result_name="sentiment")
d = Analysis(function=heuristics.latest_sentiment_analysis, result_name="sentiment_latest")

r.add_analysis(a)
r.add_analysis(b)
r.add_analysis(c)
r.add_analysis(d)

r.generate()
r.log()
