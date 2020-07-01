# Problem Set 4C
# Name: Clarke Homan
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
    upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerVowels = 'aeiou'
    upperVowels = 'AEIOU'
    valid_words = load_words(WORDLIST_FILENAME)
    
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.dictList = {}
        # self.encryptedString = ''
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lettersDict = {}
        upper_Vowels_Permutation = vowels_permutation.upper()
        vowels_permutation_len = len(vowels_permutation)
        j = 0
        for i in self.upperLetters:
            if i not in self.upperVowels:
                lettersDict[i] = i
            else:
                if i == 'A':
                    lettersDict['A'] = upper_Vowels_Permutation[j]
                if i == 'E':
                    lettersDict['E'] = upper_Vowels_Permutation[j]
                if i == 'I':
                     lettersDict['I'] = upper_Vowels_Permutation[j]
                if i == 'O':
                 lettersDict['O'] = upper_Vowels_Permutation[j]
                if i == 'U':
                 lettersDict['U'] = upper_Vowels_Permutation[j]
                if j < vowels_permutation_len:
                    j += 1
    
        j = 0
        for i in self.lowerLetters:
            if i not in self.lowerVowels:
                lettersDict[i] = i
            else:
                if i == 'a':
                    lettersDict['a'] = vowels_permutation[j]
                if i == 'e':
                    lettersDict['e'] = vowels_permutation[j]
                if i == 'i':
                     lettersDict['i'] = vowels_permutation[j]
                if i == 'o':
                 lettersDict['o'] = vowels_permutation[j]
                if i == 'u':
                 lettersDict['u'] = vowels_permutation[j]
                if j < vowels_permutation_len:
                    j += 1
            
        return lettersDict
        # pass #delete this line and replace with your code here
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encryptedString = ''
        for i in self.message_text:
            if i.isalpha() == True:
                encryptedString += transpose_dict[i]
            else:
                encryptedString += i
            
        return encryptedString
        # pass #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object
        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        SubMessage.__init__(self, self.message_text)
        # pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        decodedWordSuccesses = {}  # create translation success dictionary
        # wordList = decodedMessage.split()
        vowelsList = get_permutations(VOWELS_LOWER)
        for vowelsPermutation in vowelsList:
            decodedWordSuccesses[vowelsPermutation] = 0
            enc_dict = self.build_transpose_dict(vowelsPermutation)
            decodedMessage = self.apply_transpose(enc_dict)
            wordList = decodedMessage.split()
            for j in range(len(wordList)):
                if is_word(self.valid_words, wordList[j]) == True:
                    decodedWordSuccesses[vowelsPermutation] += 1

        maxFound = max(decodedWordSuccesses.values())  #find first max decoded successes
        
        for transposeKey, transposeKeySuccess in decodedWordSuccesses.items():
            if transposeKeySuccess == maxFound:
                enc_dict = self.build_transpose_dict(transposeKey)
                decodedMessage = self.apply_transpose(enc_dict)
                break
        
        
        return decodedMessage
        # pass #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
    # Encrypt the message ...
    inputString = input('Enter string to process. May contain whitespace and punctuation. : ')
    message = SubMessage(inputString)
    permutation = input('Enter vowels permutation. Example: aeiou or iuaeo. : ')
    # permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    encryptedMessage = message.apply_transpose(enc_dict)
    print('Actual encrypted message is', encryptedMessage)
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    
    # Now decrypt the encrypted message
    enc_message = EncryptedSubMessage(encryptedMessage)
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    decryptedMessage = enc_message.decrypt_message()
    if inputString == decryptedMessage:
        print('\nInput string \'', inputString, '\' successfully encypted and decrypted:', decryptedMessage)
        print('\nMessage encryption is:', encryptedMessage)
    else:
        print('\nInput string:', inputString, 'did not survive the conversion:', decryptedMessage)
        print('\nMessage encryption is:', encryptedMessage)
        
     
    #TODO: WRITE YOUR TEST CASES HERE
