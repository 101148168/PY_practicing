# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):

    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    status = True
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            pass
        else:
            status = False
            break       
    return status


def get_guessed_word(secret_word, letters_guessed):

    return_word = ''
    sym = '#'
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            return_word += secret_word[i]
        else:
            return_word += sym
    return return_word


def get_available_letters(letters_guessed):

    available_letters = ''
    a_z = string.ascii_lowercase
    for i in range(len(a_z)):
        if a_z[i] not in letters_guessed:
            available_letters += a_z[i]
    return  available_letters
    
    

def hangman(secret_word):
    guesses = 8
    warnings = 3
    special_use = 1
    letters_guessed = []
    a_z = string.ascii_lowercase
    vowels = ['a','e','i','o','u']
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is {0} letters long.".format(len(secret_word)))
    while guesses > 0:
        if guesses == 8:
            print('---------------')
            print("You have {0} guesses left.".format(guesses))
            print('Available letters: ', a_z)
        elif guesses < 8 and guesses > 1:
            print('---------------')
            print("You have {0} guesses left.".format(guesses))
            print('Available letters: ', get_available_letters(letters_guessed))
        elif guesses == 1:
            print('---------------')
            print("You have {0} guess left.".format(guesses))
            print('Available letters: ', get_available_letters(letters_guessed))
        letters_input = input('Please guess a letter: ').lower()
        if letters_input == '*' and guesses >= 2 and special_use > 0:
            reveal_word = hangman_with_help(secret_word)
            if reveal_word not in letters_guessed:
                print('Letter revealed: {0}'.format(reveal_word))
                guesses -= 2
                special_use -= 1
                letters_input = reveal_word
            else:
                reveal_word = hangman_with_help(secret_word)
                print('Letter revealed: {0}'.format(reveal_word))
                guesses -= 2
                letters_input = reveal_word
        if letters_input in letters_guessed:
            warnings -= 1
            if warnings > 1:
                print('Oops! You\'ve already guessed that letter. You now have {0} warnings.'.format(warnings))
            elif warnings == 1:
                print('Oops! You\'ve already guessed that letter. You now have {0} warning.'.format(warnings))
            elif warnings <= 0:
                print('Oops! You\'ve already guessed that letter. No warnings left', 'lost a guess')
                guesses -= 1
        if len(letters_input) == 1 and letters_input in a_z and letters_input not in letters_guessed:
            letters_guessed.append(letters_input)
            if is_word_guessed(secret_word, letters_guessed) == True:
                print('Congratulations, you won!')
                print('Your total score for this game is: {0}'.format(guesses*(len(secret_word)+len(set(secret_word)))))
                break
            else:
                if letters_input in secret_word:
                    print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
                else:
                    if letters_input in vowels:
                        guesses -= 2
                        print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))    
                    else:
                        guesses -= 1
                        print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
        elif len(letters_input) != 1:
            warnings -= 1
            if warnings > 1:
                print('You now have {0} warnings: '.format(warnings), get_guessed_word(secret_word, letters_guessed))
            elif warnings == 1:
                print('You now have {0} warning: '.format(warnings), get_guessed_word(secret_word, letters_guessed))
            elif warnings <= 0:
                print('No warnings left', 'lost a guess')
                guesses -= 1
        elif letters_input not in a_z:
            warnings -= 1
            if warnings > 1:
                print('You now have {0} warnings: '.format(warnings), get_guessed_word(secret_word, letters_guessed))
            elif warnings == 1:
                print('You now have {0} warning: '.format(warnings), get_guessed_word(secret_word, letters_guessed))
            elif warnings <= 0:
                print('No warnings left', 'lost a guess')
                guesses -= 1
        if guesses <= 0:
            print('Sorry, you ran out of guesses. The word was {0}.'.format(secret_word))
            print('Your total score for this game is: {0}'.format(guesses*(len(secret_word)+len(set(secret_word)))))
        print_man(guesses)
            
def hangman_with_help(secret_word):
    new = random.randint(0, len(secret_word) -1)
    return secret_word[new]

def print_man(guesses):
    if guesses == 8:
        print(" _________     ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif guesses == 7:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif guesses == 6:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|         |    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif guesses == 5:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif guesses == 4:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif guesses == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|         |    ")
        print("|        /     ")
        print("|       /      ")
        print("|              ")
    elif guesses == 2:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|         |    ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")        
    elif guesses == 1:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|       / |    ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")
    elif guesses <= 0:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|       / | \  ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")




if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
    secret_word = choose_word(wordlist)
    hangman_with_help(secret_word)
