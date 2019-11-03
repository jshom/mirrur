# from determiner_heuristic import determiner_heuristic
import nltk as nltk
import math as math
from gcp_interface import sentiment_analysis
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

def example(user_journal):
    return 0

def latest_sentiment_analysis(user_journal):
    # returns [-1 to 1]
    score = sentiment_analysis(user_journal.submissions[-1].text)
    # map to [0 to 1]
    return (float(score+1)/2)

def general_sentiment_analysis(user_journal):
    # returns [-1 to 1]
    score = sentiment_analysis(user_journal.full_text)
    # map to [0 to 1]
    return (float(score+1)/2)

def polarization_heuristic(user_journal):
    # score (0-1) 0 is full helplessness and 1 is super happy
    # get determiners from all submissions
    # find proportion of polarized determiners to all determiners
    # return that minus 1
    # print(user_journal.full_text)
    tagged_words = nltk.pos_tag(user_journal.full_text.split(' '))
    word_pairs = [(word, nltk.tag.map_tag('en-ptb', 'universal', tag)) for word, tag in tagged_words]

    potential_absolutist_word = []
    for word_tag_pair in word_pairs:
        # word[1] = Part of speech classified
        # RB = Determiners (Some, All, Few, etc., a)
        if (word_tag_pair[1] in ["DET","ADV", "ADJ"]):
            potential_absolutist_word.append(word_tag_pair[0]) # jush push the word, not

    # absolutist ADJ, DET & ADV
    absolutist_words = ["all", "every", "never", "absolutely", "complete", "completely", "constant", "definetly", "entire", "ever", "full", "totally"]

    amount_used_in_text = 0
    for word in absolutist_words:
        if word in user_journal.full_text:
            amount_used_in_text = amount_used_in_text + 1


    # how many words would be significant (40% of determiners)
    threshold = math.ceil(len(potential_absolutist_word) * 0.40)

    if (amount_used_in_text/threshold > 1):
        return 0.0;
    else:
        return 1 - (amount_used_in_text/threshold);


    #
    # weight = 1 - (math.log10(min(1000000000, len(user_journal.full_text)))/10)
    #
    # if (amount_used_in_text >= 0.05):
    #     return 0;
    # if (amount_used_in_text == 2):
    #     return (0.2 + weight)/2
    # if (amount_used_in_text == 1):
    #     return (0.4 + weight)/2
    # return 0.5 # if not return average
