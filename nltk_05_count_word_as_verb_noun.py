# A programme to count the number of time a definite word
# is used as a noun or as a verb in a corpus

import nltk
from nltk.corpus import nps_chat as nps
import matplotlib.pyplot as plt

user_input = input("Please enter a word:" ).strip().lower()
text = nps.tagged_words(tagset='universal')

count_verb = 0
for pair in text:
    if pair[0].lower() == user_input.lower():
        if "v" in pair[1].lower():
            count_verb+=1

count_noun = 0
for pair in text:
    if pair[0].lower() == user_input.lower():
        if "n" in pair[1].lower():
            count_noun+=1
if count_noun == 0 and count_verb == 0:
    print("There are no instances of this word neither as a noun, nor as a verb in this corpus")
else:
    print("There are", count_noun, "number of", user_input, " as a noun in the text")
    print("There are", count_verb, "number of", user_input, " as a verb in the text")

    figure = plt.figure()
    plt.title('Word Frequency')
    plt.grid(True)
    plt.bar(['Noun', 'Verb'], [count_noun, count_verb], color=['c', 'm'])
    figure.set_figwidth(4)
    figure.set_figheight(5)