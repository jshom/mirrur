from analysis import *
import heuristics

uj = UserJournal(phone_number="0000000")
uj.add_submission(Submission(text="I will never get this to work."))
uj.add_submission(Submission(text="Don't know if this will ever work"))

r = Report(uj)
a0 = Analysis(function=heuristics.determiner_heuristic, result_name="polarized_determiners")
r.add_analysis(a0)

r.generate()
r.log()
