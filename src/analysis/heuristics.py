# from determiner_heuristic import determiner_heuristic
import nltk as nltk
nltk.download('averaged_perceptron_tagger')

def example(user_journal):
    return 0;

def determiner_heuristic(user_journal):
    # score (0-1) 0 is full helplessness and 1 is super happy
    # get determiners from all submissions
    # find proportion of polarized determiners to all determiners
    # return that minus 1
    # print(user_journal.full_text)
    tagged_words = nltk.pos_tag(user_journal.full_text.split(' '))
    print(tagged_words)
    determiners = []
    for word_tag_pair in tagged_words:
        # word[1] = Part of speech classified
        # DT = Determiners (Some, All, Few, etc., a)
        if (word_tag_pair[1] == "RB"):
            determiners.append(word_tag_pair[0]) # jush push the word, not

    print(determiners)
    return 1;
