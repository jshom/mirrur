from analysis import *
import nltk

def process(uj):
    submissions = uj.submissions
    alltokens = []
    for i in submissions:
        tokens = nltk.word_tokenize(i.text)
        alltokens += tokens
    tags = nltk.pos_tag(alltokens)
    for i in tags:
        if i[1] == "NN" or i[1] == "NNS":
            print(i)
    
    #for word in tokens:
    #    sum += dic[word]
    #return sum
uj = UserJournal(phone_number="183402")

s0 = Submission(text="I am very lonely") 
s1 = Submission(text="My life is not fun")

uj.add_submission(s0)
uj.add_submission(s1)
process(uj)