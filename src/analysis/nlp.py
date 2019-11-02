from analysis import *
import nltk
from nltk import word_tokenize

def process(uj):
    sentence = uj.submissions
    tokens = word_tokenize(sentence[1].text)
    print(tokens)


uj = UserJournal(phone_number="183402")

s0 = Submission(text="I am really loving this")
s1 = Submission(text="I can't stand this right now.")

uj.add_submission(s0)
uj.add_submission(s1)

process(uj)
