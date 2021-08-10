# A program which determines the plural form for an English noun.

# Variant 1 uses just python arrays.
# Variant 2 uses python dictionaries.

# Variant 1

# Creating lists of vowels and consonants
eng_vowels = ["a", "e", "i", "o", "u"]
eng_consonants = ["b", "c", "d","f", "g", "h", "j", "k", "l", "m", "n", "p",
"q", "r", "s", "t", "v", "w", "x", "y", "z"]

list_ss_ch = ["ss", "sh", "ch"]
list_s_z_x = ["s", "z", "x"]

# Creating lists of irregular nouns

irreg_list = ["child", "children", "goose", "geese", "man", "men","woman",
"women","tooth", "teeth", "foot", "feet", "mouse", "mice", "person", "people",
"photo","photos", "piano", "pianos", "halo", "halos" "roof", "roofs",
"belief", "beliefs", "chef", "chefs", "chief", "chiefs", "fez", "fezzes",
"gas", "gasses", "roof", "roofs", "belief", "beliefs", "chef", "chefs", "chief", "chiefs"]

double_forms = ["cactus", "cacti", "cactuses", "focus", "foci", "focuses"]
no_change = ["sheep", "series", "species", "deer"]
always_plural = ["jeans", "scissors", "tongs", "shoes", "slippers"]

all_irregulars = irreg_list + double_forms + no_change + always_plural

                                        # Writing the programme
# We ask the user to enter the word.
# We save it in a variable after removing
# leading and trailing characters (if some)
# and converting it in lowercase.

print("Please enter a word")
user_input = input().strip().lower()

# First, we  check if the user's word
# is not in any list of exceptions.

if user_input in all_irregulars:
    if user_input in irreg_list:
        for word in range(len(irreg_list)):
            if irreg_list[word] == user_input:
                print("Plural form:", irreg_list[word+1])
    if user_input in double_forms:
        for word in range(len(double_forms)):
            if double_forms[word] == user_input:
                print("This word has two plural forms:", double_forms[word+1], ",", double_forms[word+2])
    elif user_input in no_change:
        print("This word has the same form for plural:", user_input)
    elif user_input in always_plural:
        print("This form exists only in plural:", user_input)

# If it is not the case, we proceed to checking other irregularities.

# formulating the rule for phenomenon-phenomena and the like
elif user_input[-2:] == "on":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"a")
# formulating the rule for analysis-analyses and the like
elif user_input[-2:] == "is":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"es")
# formulating the rule for cactus-cacti and the like

# formulating the rule for lunch-lunches and the like
elif user_input[-2:] in list_ss_ch:
    print("Plural form:", user_input+"es")
# formulating the rule for bus-buses and the like
elif user_input[-1:] in list_s_z_x:
    print("Plural form:", user_input+"es")
# formulating the rule for tomato-tomatoes and the like
elif user_input[-1:] == "o":
    if user_input == "volcano":
        print("This is a unique word.\nBoth of the following plural forms are correct: volcanos, volcanoes", )
    else:
        print("Plural form:", user_input+"es")
#formulating the rules for city-cities
elif user_input[-1] == "y" and user_input[-2] in eng_consonants:
    user_input = user_input[:-1]
    print("Plural form:", user_input+"ies")
#formulating the rules for ray-rays
elif user_input[-1] == "y" and user_input[-2] in eng_vowels:
    print("Plural form:", user_input+"s")
#formulating the rules for wife-wifes
elif user_input[-2] == "fe":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"ves")
#formulating the rules for wolf-wolfes
elif user_input[-1] == "f":
    user_input = user_input[:-1]
    print("Plural form:", user_input+"ves")

# Eventually, if the word is a regular noun like car-cars, we just add "s"
else:
    print("Plural form:", user_input+"s")


# Variant 2
                            #Preparing the data (lists, dictionaries)
# Creating lists of vowels and consonants
eng_vowels = ["a", "e", "i", "o", "u"]
eng_consonants = ["b", "c", "d","f", "g", "h", "j", "k", "l", "m", "n", "p",
"q", "r", "s", "t", "v", "w", "x", "y", "z"]

list_ss_ch = ["ss", "sh", "ch"]
list_s_z_x = ["s", "z", "x"]

# Creating several lists and dictionaries of irregular nouns.

irreg_dict_one = {
    'child':'children', 'goose':'geese', 'man':'men',
    'woman':'women','tooth':'teeth','foot':'feet',
    'mouse':'mice', 'person':'people', "roof": "roofs",
    "belief":"beliefs", "chef": "chefs", "chief": "chiefs"
    }
irreg_dict_two = {'photo':'photos', 'piano':'pianos','halo':'halos'}
irreg_dict_three = {'roof':'roofs', 'belief':'beliefs', 'chef':'chefs', 'chief':'chiefs'}
irreg_dict_four = {'fez':'fezzes', 'gas':'gasses'}

irreg_list_focus = ["cactus", "cacti", "cactuses", "focus", "foci", "focuses"]
irreg_list_deer = ["sheep", "series", "species", "deer"]
irreg_list_jeans = ["jeans", "scissors", "tongs", "shoes", "slippers"]
list_ss_ch = ["ss", "sh", "ch"]
list_s_z_x = ["s", "z", "x"]

irreg_all = list(irreg_dict_one.keys()) + list(irreg_dict_two.keys()) + list(irreg_dict_three.keys()) + list(irreg_dict_four.keys()) + irreg_list_focus + irreg_list_deer + irreg_list_jeans

                                        # Writing the programm
# We ask the user to enter the word.
# We save it in a variable after removing
# leading and trailing characters (if some)
# and converting it in lowercase.

print("Please enter a word")
user_input = input().strip().lower()

# First, we  check if the user's word
# is not in any list or dictionary of exceptions.

if user_input in irreg_all:
    if user_input in irreg_dict_one:
        print("Plural form:", irreg_dict_one[user_input])
    elif user_input in irreg_dict_two:
        print("Plural form:", irreg_dict_two[user_input])
    elif user_input in irreg_dict_three:
        print("Plural form:", irreg_dict_three[user_input])
    elif user_input in irreg_dict_four:
        print("Plural form:", irreg_dict_four[user_input])
    elif user_input in irreg_list_focus:
        for word in range(len(irreg_list_focus)):
            if irreg_list_focus[word] == user_input:
                print("This word has two plural forms:", irreg_list_focus[word+1], ",", irreg_list_focus[word+2])
    elif user_input in irreg_list_deer:
        print("This word do not change when pluralized:", user_input)
    elif user_input in irreg_list_jeans:
        print("This form is already plural:", user_input)

# If it is not the case, we proceed to checking other irregularities.

# formulating the rule for phenomenon-phenomena and the like
elif user_input[-2:] == "on":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"a")
# formulating the rule for analysis-analyses and the like
elif user_input[-2:] == "is":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"es")
# formulating the rule for cactus-cacti and the like

# formulating the rule for lunch-lunches and the like
elif user_input[-2:] in list_ss_ch:
    print("Plural form:", user_input+"es")
# formulating the rule for bus-buses and the like
elif user_input[-1:] in list_s_z_x:
    print("Plural form:", user_input+"es")
# formulating the rule for tomato-tomatoes and the like
elif user_input[-1:] == "o":
    if user_input == "volcano":
        print("This is a unique word.\nBoth of the following plural forms are correct: volcanos, volcanoes", )
    else:
        print("Plural form:", user_input+"es")
#formulating the rules for city-cities
elif user_input[-1] == "y" and user_input[-2] in eng_consonants:
    user_input = user_input[:-1]
    print("Plural form:", user_input+"ies")
#formulating the rules for ray-rays
elif user_input[-1] == "y" and user_input[-2] in eng_vowels:
    print("Plural form:", user_input+"s")
#formulating the rules for wife-wifes
elif user_input[-2] == "fe":
    user_input = user_input[:-2]
    print("Plural form:", user_input+"ves")
#formulating the rules for wolf-wolfes
elif user_input[-1] == "f":
    user_input = user_input[:-1]
    print("Plural form:", user_input+"ves")

# Eventually, if the word is a regular noun like car-cars, we just add "s"
else:
    print("Plural form:", user_input+ "s")