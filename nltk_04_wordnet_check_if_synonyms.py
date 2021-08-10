# A program that determines whether 2 words are synonyms using NLTK and WordNet

from nltk.corpus import wordnet as wn

# We ask the user to enter the first and the second word.
# We delete the space characters (if some), convert them in
# lower case and store in corresponding variables
print("Please enter the first word")
word_one = input().strip().lower()
print("Please enter the second word")
word_two = input().strip().lower()

# We create a variable for common definitions
common_definitions = []

# We check the set of synsets of each word and compare them
for i, synset in enumerate(wn.synsets(word_one)):
    for j, synset2 in enumerate(wn.synsets(word_two)):
        if synset == synset2:
            common_definitions.append(synset.definition())
# if they have definitions in common, we print them out
if common_definitions:
    print("The words are synonyms. Their common senses include:"," ".join(common_definitions))
# if they don't, we display the corresponding message
else:
    print("The words are not synonyms.")