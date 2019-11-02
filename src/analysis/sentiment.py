import numpy
#from analysis import analysis

def output_sentiment(uj): #handles UserJournal
    subs = uj.submissions
    last_submission = subs[-1]
    last_str = clean_str(last_submission)
    return calculate_sentiment(last_submission)

def calculate_sentiment(str): #adds up sentiment for individual submissions
    word_dict = get_dict('word_dictionary.txt')
    total = 0
    for word in str.split():
        try:
            total += word_dict[word.lower()]
        except:
            continue

    norm_sent = total/numpy.sqrt(numpy.sum(total**2))
    print(norm_sent)

def clean_str(submission):
    content = submission.text
    split_content = content.split('\n')
    sentence = split_content[0].strip('text: ')
    return sentence

def get_dict(f):
    dict_f = open(f, 'r')

    word_dict = {}

    for l in dict_f: #adds keyword with a specific set value
        split_line = l.strip().split('\n')
        word_dict[split_line[0].strip()] = int(word_dict[split_line[1].strip()])  #adds word with a number
