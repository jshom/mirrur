from analysis import *
import heuristics as heuristics

# -----------------------------
# Example Usage for UserJournal
# -----------------------------

uj = UserJournal(phone_number="183402")

s0 = Submission(text="I am really loving this")
s1 = Submission(text="I can't stand this right now.")

uj.add_submission(s0)
uj.add_submission(s1)

# example print userjournal
print(uj)
# example print single submission
print(s0)

# ---------------------------
# Example Usage for Analsysis
# ---------------------------

r = Report(uj)

a = Analysis(function=heuristics.example, result_name="example_result")
a = Analysis(function=heuristics.determiner_heuristic, result_name="example_result")
r.add_analysis(a)

r.generate()
r.print()
