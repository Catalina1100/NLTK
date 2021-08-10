# A summariser based on word frequencies that returns
# the most frequent sentences from a text.

# First, we import the libraries that we will need further in the code.
import nltk
from nltk.corpus import stopwords
from operator import itemgetter

# Generally, we ask the user to input the name of the file
# user_file = input()
# with open(user_file) as file_l:

# But for the moment I am using a file from my folder
# We open a file, read it and store the text in a variable
with open("the-word-by-nabokov.txt") as new_file:
    text = new_file.read()

# We tokenize the text by sentences
t_sents = nltk.sent_tokenize(text)

# We will need to create several variables and dictionaries
# 1. a list where we will store a new tokenized sentence
# 2. a varible for total word score per each sentence
# 3. a dictionary to store the score of each word in a sentence
# in case we will need it for further analysis of the text
# 4. a dictionary with total score per each sentence
new_sents_list = []
all_words_score = 0
d_words_scores = {}
d_sents_scores = {}

# 1. We create a new sentence of tokenized words
# and eliminate punctuation marks (if some)
# 2. We find part of speech of each word in a sentence
# and calculate the number of times it appears as this pos
# in a sentence
# 3. We add the word with it score to the dictionary
# 4. We calculate the score of each sentence and store it
# in a dictionary
for sent in range(len(t_sents)):
    new_sent = []
    for word in nltk.word_tokenize(t_sents[sent]):
        if word.isalnum():
            new_sent.append(word.strip("вЂ").strip())
    all_words_score=0
    for word, pos in nltk.pos_tag(new_sent):
        word_score=0
        if word.isalnum() and word.lower() not in stopwords.words():
            for word_2, pos_2 in nltk.pos_tag(new_sent):
                if word.lower() == word_2.lower() and pos == pos_2:
                    word_score+=1
                    all_words_score+=1
            d_words_scores[word + " as " + pos] = word_score
        else:
            continue
    d_sents_scores[sent] = all_words_score/len(new_sent)

# We sort the sentences by items (score), indicating that we want them
# to apeear from the biggest score to the lowest
sorted_ss = sorted(d_sents_scores.items(), key=itemgetter(1), reverse=True)

# We ask the user to input the number of sentences to check.
# print("Please enter a number of sentences you want to check")
# user_num = int(input())
# for i in range(user_num):

# Let's check the scores of the first 5 sentences
for i in range(5):
    print("Sentence", i+1, "with the score", round(list(sorted_ss[i])[1], 3), ":\n", t_sents[sorted_ss[i][0]])