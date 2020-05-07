# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "./words.txt"
NOT_FOUND = -1

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    retStatus = True
    for char in secret_word:
        if(letters_guessed.find(char)) == NOT_FOUND:
            retStatus = False
            break

    return retStatus



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    
    letters_guessed: list (of letters), which letters have been guessed so far; 
    assumes that all letters are lowercase
    
    returns: a string of characters comprised of lowercase letters and underscores (_),
             based on what letters in letters_guessed  are found in secret_word.

    '''
    current_userstring = ''  # initialize return string
    for secretword_prt in secret_word:   #seach thru secret word
    # if letters in letters_guessed are found in the secret word, enter the letters
    # into the return string as position found in the secret word. Else enter a '_'
    # into the letter position of the return string not found in the letters_guessed string
        index = letters_guessed.find(secretword_prt)
        if index == NOT_FOUND:
            current_userstring = current_userstring + '_'
        else:
            current_userstring = current_userstring + secretword_prt

    return current_userstring


def get_available_letters(letters_guessed):
    '''
        letters_guessed: list (of letters), which letters have been guessed so far; 
        assumes that all letters are lowercase
    '''
    
    totalavailableletters = 'abcdefghijklmnopqrstuvwxyz'
    availableletters = ''
    
    for char in totalavailableletters:
        index = letters_guessed.find(char)
        if index == NOT_FOUND:
            availableletters += char
    
    return availableletters

def is_vowel_or_consanant(char):
    '''
    char is the user inputted character that was considerd for the secret word
    
    return penalty which is the number of tries a selected consonant or vowel
        incurs when not present in the selected secret word
    '''

    vowels = 'aeiou'

    penalty = 1
    guessnum = vowels.find(char)
    if guessnum == NOT_FOUND:  # must be consonant
        penalty = 2

    
    return penalty

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.

    Parameters
    ----------
    secret_word : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    
    '''
    

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    print('Welcome to the game of Hangman.')
    print('The program has selected a "secret word" for you to guess.')
    print('''\nYou will get six incorrect guesses.
Each correct guess will be displayed in a string with underscores unguessed letter.''')

    NUM_TRIES = max(6,(len(secret_word)-1))
    num_strikes = 0
    secret_word_len = len(secret_word)
    current_userstring = '_' * secret_word_len
    old_userstring = ''
    guess_letters = ''
   
    print('Secret word length is:', secret_word_len)
    i = 0
    while i < NUM_TRIES:         # fetch NUM_TRIES letters from user
        print('\n-------------------------')
        if i == NUM_TRIES-1:
            print('\nLast Guess! Make it count.')
        else:
            print('\nGuess No.:', i+1, 'of', NUM_TRIES)
        print('Current hangman word:', current_userstring)
        if guess_letters != '':
            print('Selected letters:', guess_letters)
        else:
            print('Selected letters: <none>')
            
        availableletters = get_available_letters(guess_letters)
        if availableletters != '':
            print('Available letters:', availableletters)
            
        inputstr = input('Please guess a letter or guess the secret word (enter an "*" to view clues): ')
        if len(inputstr) > 1:      # try to guess the word
            if inputstr == secret_word:
                print('Congratulations! You guessed the secret word')
                return
            else:
                print("That's not the secret word! You lose! The secret word is:", secret_word)
                return

        input_char = inputstr[0]
        if(input_char == '*'):
            clue_words = ''
            for word in wordlist:
                if((match_with_gaps(current_userstring, word)) == True):
                    clue_words += word + '  '
            print('Clue words:', clue_words)
            continue
        else:
            input_char = input_char.lower()
        
        if input_char.isalpha() == False:  # check for input not being a letter
            num_strikes += 1
            print('Input not a letter! Strike', num_strikes)
            if num_strikes > 2:
                print("Strike 3, you're out!, You lose.")
                return
            continue
        
        guessnum = guess_letters.find(input_char)   # check to see if user already entered letter previously
        if guessnum != NOT_FOUND:
            print('Letter', input_char, 'already entered. Lose the turn')
            i += 1
            continue
        
        
        guess_letters += input_char
       
        if is_word_guessed(secret_word,guess_letters):
            print("Congratulations! You've guessed the word")
            score = (NUM_TRIES - i) * len(guess_letters)
            print('Your total score for this game is:', score)
            return
        else:
            old_userstring = current_userstring
            current_userstring = get_guessed_word(secret_word, guess_letters)
            if current_userstring == old_userstring:  # if selected letter is not in secret word
                penalty = is_vowel_or_consanant(input_char)  # increment tries counter by 1 or 2 dependng on letter type
                if penalty == 2:
                    print('Consonant', input_char, 'not found in secret word. Bad consonants cost 2 turns')
                else:
                    print('Vowel', input_char, 'not found in secret word. Bad vowels cost 1 turns')
                i += penalty
                print('Remaining guesses:', NUM_TRIES - i)
            else:
                print('Good job, you guessed a letter, continue')
                
    score = NUM_TRIES - i * len(guess_letters)
    print('Your total score for this game is:', score)

    return



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    
    retStatus = False
    stripped_other_word = other_word.strip()
    if len(my_word) != len(stripped_other_word): # test to see if other word is not the same lenght as my_word
        retStatus = False
    else:               # other word is same length as my_word
        i = 0
        for i in range(len(my_word)):
            if my_word[i] != '_':
                if my_word[i] == stripped_other_word[i]:
                    retStatus = True    # so far a match
                else:
                    retStatus = False  # character do no match between strings
                    break              # no point looking further

    return retStatus
            



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    print('Secret word is:', secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
