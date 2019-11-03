from analysis import *
# import nltk
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

AUTH_TOKEN_PATH = os.environ['AUTH_TOKEN_PATH']
client = language.LanguageServiceClient.from_service_account_file(AUTH_TOKEN_PATH)

def sentiment_analysis(text):
    # GCP request doc
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    # sentiment.score & sentiment.magnitude exist
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # return score (normalize output in heuristics)
    return sentiment.score
