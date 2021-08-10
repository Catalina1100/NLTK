# A program to calculate what percentage of noun synsets have no hyponyms.

# First, we import wordnet from nltk library
from nltk.corpus import wordnet as wn

# We set a variable to count the number of words
# which does not contain hyponyms.
counter = 0

for synset in list(wn.all_synsets('n')):
    s = str(synset).strip('Synset').strip('(').strip(')').strip("'")
    if not wn.synset(s).hyponyms():
        counter +=1

# We find out the total number of synsets
total_syn = len(list(wn.all_synsets('n')))

# We count the result and print it out
result = int((counter // (total_syn /100)))
print("There are roughly:", result, "% of synsets that does not have hyponyms")
# There are roughly: 79 % of synsets that does not have hyponyms