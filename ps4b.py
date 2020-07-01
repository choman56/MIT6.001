# Problem Set 4B
# Name: Clarke A. Homan
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
    upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_words = load_words(WORDLIST_FILENAME)
    
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.dictList = {}
        self.encryptedString = ''
        # pass #delete this line and replace with your code here

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        
        # pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        wordList = self.valid_words
        return wordList
        # pass #delete this line and replace with your code here

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lettersDict = {}
        for i in range(len(self.upperLetters)):
            j = (i + shift) % 26
            lettersDict[self.upperLetters[i]] = self.upperLetters[j]
        
        for i in range(len(self.lowerLetters)):
            j = (i + shift) % 26
            lettersDict[self.lowerLetters[i]] = self.lowerLetters[j]
            
        return lettersDict        # lettersDict = ({letters[0]: letters[0+shift]})
        # pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        assert type(shift) == int and ((shift >= 0) and (shift < 27)), 'shift value not kosher'
        
        self.dictList = self.build_shift_dict(shift)  # build the encryption dictionary
        
        message = self.get_message_text()  # get the message
        
        encryptedString = ''
        
        for char in message:
            if (char in self.lowerLetters) or (char in self.upperLetters):
                encryptedString += self.dictList[char]
            else:
                encryptedString += char
        
        return encryptedString
        
                
        
        # pass #delete this line and replace with your code here

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.shift = shift
        self.message_text = text
        Message.__init__(self, self.message_text)
        self.message_text_encrypted = self.apply_shift(self.shift)
        # pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
        # pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        dictCopy = self.dictList
        return dictCopy
        # pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
        # pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert type(shift) == int and ((shift >= 0) and (shift < 27)), 'shift value not kosher'
        
        self.shift = shift
        messageObj.build_shift_dict(self.shift)
        pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.PlaintextMessage = ''
        Message.__init__(self, self.message_text)
        
        # pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # wordList = self.message_text
        decodedWordSuccesses = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        for s in range(1,27):
            tempShift = 26 - s
            decodedMessage = self.apply_shift(tempShift)
            wordList = decodedMessage.split()
            for j in range(len(wordList)):
                if is_word(self.valid_words, wordList[j]) == True:
                    decodedWordSuccesses[tempShift] += 1
        
        maxFound = max(decodedWordSuccesses)
        if maxFound > 0 and maxFound == len(wordList):
            shiftValue = decodedWordSuccesses.index(maxFound)
            decodedMessage = self.apply_shift(shiftValue)
            foundTuple = (shiftValue, decodedMessage)
        else:
            foundTuple = (-1,'')
            
        return foundTuple
        
        # pass #delete this line and replace with your code here

if __name__ == '__main__':    
        
#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello world!', 2)
    print('Expected Output: jgnnq yqtnf!')
    encryptedText = plaintext.get_message_text_encrypted()
    if encryptedText ==  'jgnnq yqtnf!':
        print('Congratulations! The encrtpted sting rendered', encryptedText, 'matches "jgnnq yqtnf!"')
    else:
        print('Oops, the encrypted string ', encryptedText, 'does not match the expected encryption "jgnnq yqtnf!"')
#
#   Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq yqtnf!')
    # print('Expected Output:', (24, 'hello'))
    actualOutput = ciphertext.decrypt_message()
    if(actualOutput[0] != -1):
        print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    print('New test case')
    plaintext = PlaintextMessage('Hello World! Please to meet you', 20)
    # print('Expected Output: jgnnq yqtnf!')
    encryptedText = plaintext.get_message_text_encrypted()

    ciphertext = CiphertextMessage(encryptedText)
    # print('Expected Output:', (24, 'hello'))
    actualOutput = ciphertext.decrypt_message()
    if(actualOutput[0] != -1):
        print('Actual Output:', ciphertext.decrypt_message())
        print('Shift is', actualOutput[0])
    

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
