from analysis import *
import nltk

def process(uj):
    submissions = uj.submissions
    tokens = []
    tags = []
    for i in submissions:
        tokens += nltk.word_tokenize(i.text)
        tags += nltk.pos_tag(tokens)
    for i in tags:
        print(i[1])
    #for word in tokens:
    #    sum += dic[word]
    #return sum


uj = UserJournal(phone_number="183402")

s0 = Submission(text="I am really loving this") 
s1 = Submission(text="I can't stand this right now.")

uj.add_submission(s0)
uj.add_submission(s1)
process(uj)