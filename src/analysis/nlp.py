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
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

"""

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
"""