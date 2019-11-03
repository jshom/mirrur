from analysis import *
# import nltk
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types



client = language.LanguageServiceClient.from_service_account_file('/Users/andresorbe/PycharmProjects/Hackathon/linus-68f6aad97157.json')

# The text to analyze
text = u'WORDS'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(score_algo(sentiment.score), sentiment.magnitude))

def score_algo(sentiment_score):
    sa = sentiment_score + 1
    return (float(sa)/2)



"""

def process(uj):
    submissions = uj.submissions
    alltokens = []
    for i in submissions:
        tokens = nltk.word_tokenize(i.text)
        alltokens += tokens
    tags = nltk.pos_tag(alltokens)
    for i in tags:
        print(i[1])
    #for word in tokens:
    #    sum += dic[word]
    #return sum




uj = UserJournal(phone_number="183402")

s0 = Submission(text="I am very lonely") 
s1 = Submission(text="My life is not fun")

uj.add_submission(s0)
uj.add_submission(s1)
process(uj)
"""