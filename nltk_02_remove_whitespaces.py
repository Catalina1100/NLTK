# A program that removes whitespace at the beginning and end of a string,
# and normalizes whitespace between words to be a single space character.

# We ask the user to enter a text
print("Please enter your text")
# user_input = input()

# Let's try it with our own input
user_input = """
   Only 20% of the entire ocean floor of our planet has been mapped. 
That means that     over half of   the surface of our planet remains uncharted,
and we have hardly any idea  what the ocean    floor looks like in sufficient
detail or     what kinds of organisms are living there.    
"""

# We then split this text into words using the split() function and indicating
# the parameter by which we want to split the text. Before this, we also delete
# leading and trailing whitespace characters so that they did not interfere.
# We then save the resulting pieces as a list.

words_list = user_input.strip().split(" ")
print(words_list)

# We create a new list where we will store our processed words.
new_list = []

# Then we go through all the words in the list, cleaning them of any spaces
# with the strip() function, and adding each clean word to the new list.

for i in range(len(words_list)):
    if words_list[i] != " " and "\n":
        new_list.append(words_list[i].strip())
new_text = new_list[0].join(new_list[1:])
print(new_list)