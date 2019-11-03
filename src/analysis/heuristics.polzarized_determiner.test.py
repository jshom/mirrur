from analysis import *
import heuristics

uj = UserJournal(phone_number="00000000")
uj.add_submission(Submission(text="I will never get this to work."))

r = Report(uj)
a0 = Analysis(function=heuristics.polarization_heuristic, result_name="polarized_determiners")
r.add_analysis(a0)

r.generate()
r.log()

uj1 = UserJournal(phone_number="00000001")
uj1.add_submission(Submission(text="Things are fine."))
uj1.add_submission(Submission(text="Would love it if everything would be ok. Sometimes I just don't feel great but usually it is alright. Some more generic text that is normal."))

r1 = Report(uj1)
r1.add_analysis(a0)

r1.generate()
r1.log()
