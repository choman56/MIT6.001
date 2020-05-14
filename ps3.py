# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Clarke Homan
# Collaborators : <none>
# Time spent    : ~ 12 hours

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
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
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0 (hand length when the word was played)
    """
    score = 0
    firstComponentScore = 0
    secondComponentScore = 1
    wordLen = len(word)
    if(wordLen > 0):             # word is not empty
        lowerWord = word.lower()   # convert word to lower case
        for char in lowerWord:
            if char != '*':
                letterVal = SCRABBLE_LETTER_VALUES[char]
                firstComponentScore += letterVal
            
        secondComponentScore = max(1, ((7*wordLen) - (3*(n-wordLen))))
        
        score = firstComponentScore * secondComponentScore
    
    return score
#    pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):    # accounts for multiple copies of the same letter
                                         # j gets the letter count
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    hand['*'] = 1 
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()       # start with copy of hand dict

    lowerWord = word.lower()    # make sure there's no capitals
    for char in lowerWord:     # rifle thru each char in the word
        number = newHand.get(char,0) # find letter in hand, fetching the letter's current count
        if number > 0:         # if letter's current count is > 0, decrement it for the letter instance in word
            newHand[char] -= 1
        else:
            continue
    
    return newHand
 #   pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    retStatus = False              #Start with retStatus being False
    wordFound = False              # user word found in dictionary
    
    wordList_len = len(word_list)  # determine the number of words in list
                                   # not actully used but informational
                                   
    word = word.lower()            # lower case  
    
    #
    # Test to see if "word" is in wordList
    #
    for wordListWord in word_list: # search thru wordlist for the word
        wordFound = False
        if len(wordListWord) == len(word):
            starPos = word.find('*')
            if starPos == -1:              # word doesn't contain '*'
                if wordListWord == word:   # is the selected word compares with the word
                    wordFound = True
                    break                  # no need to look further
            else:
                if (VOWELS.find(wordListWord[starPos]) != -1):  # test to see if '*' in selected word points to a vowel
                    if starPos > 0:                             # if not leading vowel
                        if(wordListWord[0:starPos] == word[0:starPos]):   # test to see if substr up to '*' are the same for both strings
                            wordFound = True
                            if starPos+1 < len(word):
                                if(wordListWord[starPos+1:] == word[starPos+1:]): # test to see if substr after the '*' are the same for both strings
                                    wordFound = True
                                    break
                                else:
                                    wordFound = False
                                    continue
                            else:
                                wordFound = True
                                break
                    elif (wordListWord[1:] == word[1:]):  # do word strings [1:] match
                        wordFound = True
                        break
                else:
                    wordFound = False
                    continue
            #
            # Test to see if "word" can be constructed from existing letters in hand
            #
    if wordFound:
        newHand = hand.copy()           # start with copy of hand dict
        lowerWord = word.lower()        # make sure there's no capitals
        for char in lowerWord:          # rifle thru each char in the word
            number = newHand.get(char,0) # find letter in hand, fetching the letter's current count
            if number > 0:     # if letter's current count is > 0, decrement it for the letter instance in word
                wordCanBeBuilt = True       # then return status is at least partial true
                newHand[char] -= 1
            else:
                wordCanBeBuilt = False   # hand doesn't have enough copies of letter
                break          # no sense eval further, hand doesn't have enough
                               # instances of the needed letter
    if wordFound and wordCanBeBuilt:
        retStatus = True
    else:
        retStatus = False
        
    return retStatus    # return function results status
    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for i in hand:
        handLen += hand.get(i)
    return handLen
   # pass  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letteyrs in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    runningScore = 0
    numLetters = calculate_handlen(hand)
    

    print('')
    print('\n\tCurrent hand:', end='  ')
    display_hand(hand)
    print('\nDo you want to replace a letter before playing hand?')
    replaceDecision = input("Type in a 'Y' or 'y' for Yes or a 'N' or 'n' for No: ")
    if (replaceDecision == 'Y') or (replaceDecision == 'y'):
        replacementLetter = input('Enter letter to be replaced: ')
        hand = substitute_hand(hand,replacementLetter)
        print('\n\tUpdated hand:', end='  ')
        display_hand(hand)
    shouldDisplayHand = False
    
    while numLetters  > 0:
        if not shouldDisplayHand:
            shouldDisplayHand = True
        else:
            print('\n\tCurrent hand:', end='  ')
            display_hand(hand)
            
        starNumber = 0
        starNumber = hand.get('*',0) # find letter in hand, fetching the letter's current count
        if starNumber > 0:
            word = input("Enter a word made up of letters (including an '*' if desired representing a vowel ('a', 'e', 'i', 'o' or 'u'')) from hand: ")
        else:
            word = input("Enter a word made up of letters) from hand: ")
        if word == '!!':
            print('Hand score is:', runningScore)
            break
        wordValidity = is_valid_word(word, hand,word_list)
        if wordValidity:
            wordScore = get_word_score(word, numLetters)
            runningScore += wordScore
            print('\nCONGRATULATIONS! Word:', word, 'is a valid word! Word', word, 'earned', wordScore,'Current Score is:', runningScore)
        else:
            print('\nOOPS! Word:', word, 'is a invalid word!', 'Current Score is:', runningScore)
        hand = update_hand(hand, word)
        numLetters = calculate_handlen(hand)
        
    return runningScore


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string (one character)
    returns: dictionary (string -> int)
    """
    newHand = {}       # start with empty return hand
    letterLength = len(letter)
    if letterLength != 1:
        print ('Substitute Letter Procedure Error: can only replace letter in a hand', letter)
        return newHand
    
    if letter in hand:
        letterNumber = hand.get(letter) # fetch the letter's current count
        hand.pop(letter)
        for i in hand:
            tempDict = {i:hand.get(i)}
            newHand.update(tempDict)   # add remaining hand element
        numLetters = calculate_handlen(newHand)
        missingLetters = HAND_SIZE - numLetters
        # if missingLetters > 0:       # need to add missing letters to get inital HAND_SIZE
        while missingLetters > 0:
            # for j in range(missingLetters):    # add missing letters that were deleted 
            if VOWELS.find(letter) != -1:
                x = random.choice(VOWELS)
            if CONSONANTS.find(letter) != -1:  # these should be mutually exclusinve
                x = random.choice(CONSONANTS)
            if (newHand.get(x) == None) and (x != letter):
                newHand[x] = newHand.get(x, 0) + 1
                missingLetters -= 1
            
    return newHand
    
    
    # pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    totalScore = 0
    print('Welcome to my word game')
    print('The object of the game is to create words from the dealt hand, letter chosen at random for you')
    print('You will be asked how many hands (rounds) you want to play')
    print('The hand will then be displayed with', HAND_SIZE, 'letters for you to create words from.')
    print('If the word you enter contains letters from the hand and is a valid word in the program dictionary,')
    print('then a score will be calculated based upon the letter values in the played word. You score will be')
    print('accumulated for the game.')
    print("If a hand contains a '*', that character is a wild card letter that can represent a vowel.")
    print('At the beginning of each round, you can decide to replace a letter in the dealt hand.')
    print('\nAre you ready to play?')
    response = input('Enter a "y" to continue or any other character will quit the game: ')
    
    if response == 'y':
        numGames = int(input('Enter the number of hands you want to play: '))
        for i in range(numGames):
            hand = deal_hand(HAND_SIZE)
            score = play_hand(hand, word_list)
            totalScore += score
        # print('Final score:', totalScore)
        
    return totalScore
    
    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    totalScore = play_game(word_list)
    print('Final score:', totalScore)
