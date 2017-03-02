import math
import random
import string
from unittest import mock
import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '!': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():

    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def test_play_game(word_list, hands, replaced_letter = None):

    def replace_letter_mock(hand, letter):
        num = hand[letter]
        del hand[letter]
        hand[replaced_letter] = num
        return hand
    deal_hand_function = sys.modules[__name__].deal_hand 
    substitute_hand_function = sys.modules[__name__].substitute_hand
    sys.modules[__name__].deal_hand = mock.Mock(side_effect=hands)
    if replaced_letter:
        sys.modules[__name__].substitute_hand = mock.Mock(side_effect=replace_letter_mock)
    play_game(word_list)
    sys.modules[__name__].substitute_hand = substitute_hand_function
    sys.modules[__name__].deal_hand = deal_hand_function


def get_word_score(word, n):
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    wildcard = "!"
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n-1):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand.update({wildcard:1})
    return hand

def update_hand(hand, word):

    new_hand = hand.copy()
    new_list = []
    new_list2 = []
    for k, v in new_hand.items():
        new_list.append(k*v)
    str_hand = ''.join(new_list)

    for i in str_hand:
        new_list2.append(i)   

    for i in word.lower():
        if i in new_hand:
            new_list2.remove(i)

    return get_frequency_dict(new_list2)

def is_valid_word(word, hand, word_list):

    word = word.lower()
    hand_result = True
    tmp_hand = hand.copy()
    for i in word:
        if i not in hand:
            return False
    for k,v in tmp_hand.items():
        for i in word:
            if i == k:
                v -= 1
                tmp_hand.update({k:v})
                if v < 0:
                    return False

    if hand_result == True:
        if '!' in word:
            locate = word.find('!')
            for i in CONSONANTS:
                tmp_word = word.replace('!', i)
                if tmp_word in word_list:
                    hand_resul = True
                    return True
                else:
                    hand_result = False                   
        elif word in word_list:
            return True
        else:
            return False
    return hand_result 
    
def calculate_handlen(hand):

    return len(hand)

def play_hand(hand, word_list):
    
    total_score = 0
    while True:
        print('Current Hand:')
        display_hand(hand)
        word = input("Enter word, or *END* to indicate that you are finished: ")
        if word  == '*END*':
            print("Total: {0} points.".format(total_score))
            break
        if is_valid_word(word, hand, word_list) == False:
            print('Please enter valid word')
        elif is_valid_word(word, hand, word_list) == True:
            total_score += get_word_score(word, calculate_handlen(hand))
            print(word, "earned {0} points.".format(get_word_score(word, calculate_handlen(hand))), "Total: {0} points.".format(total_score))
        hand = update_hand(hand, word)
        if hand == {}:
            break
        
    print("Total score for this hand: {0} points".format(total_score))
    return total_score
    

def substitute_hand(hand, letter):

    if letter in VOWELS:
        x = random.choice(VOWELS)
        while x in hand.keys():
            x = random.choice(VOWELS)
        hand.update({x:hand.get(letter)})
        del hand[letter]
    else:
        x = random.choice(CONSONANTS)
        while x in hand.keys():
            x = random.choice(CONSONANTS)
        hand.update({x:hand.get(letter)})
        del hand[letter]
    return hand
       
    
def play_game(word_list):

    substitute_num = 1
    hands_num = int(input("Enter total number of hands: "))
    total_hands_scores = 0
    replay_time =1
    tmp_score = 0
        
    while hands_num > 0:
        hand = deal_hand(HAND_SIZE)
        print("Current hand:")
        display_hand(hand)
        if substitute_num >= 1:
            substitute_answer = input("Would you like to substitute a letter? ").lower()
            if substitute_answer == "yes" or substitute_answer == "y":
                letter = input("Which letter would you like to replace: ").lower()
                substitute_hand(hand, letter)
                substitute_num -= 1
        if replay_time >= 1:
            tmp_score = play_hand(hand, word_list)
            replay_answe = input("Would you like to replay the hand? ").lower()
            if replay_answe == "yes" or replay_answe == "y":
                tmp_replay_score = play_hand(hand, word_list)
                replay_time -= 1
                if tmp_replay_score >= tmp_score:
                    tmp_score = tmp_replay_score
            total_hands_scores += tmp_score       
        else:
            total_hands_scores += play_hand(hand, word_list)

        hands_num -= 1
    print("Total score over all hands: ",total_hands_scores)
    return total_hands_scores

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
