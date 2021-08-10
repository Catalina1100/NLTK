# A program that searches for 3-grams that have a specified sequence of part of speech
# in the Brown corpus
import nltk
from nltk.corpus import brown as bw

print("Please enter 3 abbreviated, space-separated parts of speech:")

print("""Please use the following tagset:\n
VERB - verbs (all tenses and modes)
NOUN - nouns (common and proper)
PRON - pronouns
ADJ - adjectives
ADV - adverbs
ADP - adpositions (prepositions and postpositions)
CONJ - conjunctions
DET - determiners
NUM - cardinal numbers
PRT - particles or other function words
X - other: foreign words, typos, abbreviations
.	punctuation marks	. , ; !
""")

user_tags = ['DET', 'NOUN', 'NOUN']
#user_tags = input().split()

text = nltk.corpus.brown.tagged_words(tagset='universal')[:1000]
list_trigrams = []
for p1,p2,p3 in nltk.trigrams(text):
    if p1[1] == user_tags[0] and p2[1] == user_tags[1] and p3[1] == user_tags[2]:
        a = p1[0] + ", " + p2[0] + ", " + p3[0]
        list_trigrams.append(a)
print("Here are all the phrases of", user_tags, "type found in the corpus:\n",
list_trigrams)
