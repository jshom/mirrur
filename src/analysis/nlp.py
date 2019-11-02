from analysis import *
import nltk

def process(uj):
    sentence = uj.submissions
    for i in sentence:
        tokens = nltk.word_tokenize(i.text)
        print(tokens)
        tagged = nltk.pos_tag(tokens)
        print(tagged)


uj = UserJournal(phone_number="183402")

s0 = Submission(phone_number="183402", text="I am really loving this")
s1 = Submission(phone_number="183402", text="I can't stand this right now.")

uj.add_submission(s0)
uj.add_submission(s1)
process(uj)