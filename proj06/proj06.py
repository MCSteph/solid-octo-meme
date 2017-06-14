# Name:
# Date:


# proj06: Hangman
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
#    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere

wordlist = load_words()
numguess = 6



def hangman():
    word = choose_word(wordlist)
    length = len(word)
    print length
    for length in word:
        print "_",
#    print word
    return word




word2 = hangman()
guess = str(raw_input("Guess a letter or word "))


ans_list = []

for l in word2:
    ans_list.append(l)





if guess == word2:
    print("Wow I'm impressed")




else:
    numguess = numguess - 1
    print ("Sorry, that's incorrect")



