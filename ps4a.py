# Problem Set 4A
# Name: Clarke A Homan
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    string = sequence.lower()
    
    stringList = get_strings(string)
    
    return stringList
    
def permeate(string, character):
    '''
    Generates N+1 unique permutation strings fashioned from "string" with the 
    character added to each string in a unique position. 
    
    An example:
        
        string:    'ab'
        N:         len('ab') which is 2
        character: 'c'
        
        Generates:  'cab', 'acb', 'abc'
        

    Args:
        string (str): string of characters to pivot character into generating 
                      unique strings
        character (str): 1 character string that is pivoted into each unique
                       string

    Returns:
        list of N+1 strings

    '''
    
    charLen = len(character)
    N = len(string) + 1
    stringList = []
    
    if charLen > 1:
        return stringList
    
    firstString = character + string
    lastString = string + character
    stringList.append(firstString)  # add first string permutation to list
    stringList.append(lastString)   # add last string permutation to list
    
    #  add remainder (if any) string permutions to list
    middleStringsCount = N - 2     # the - 2 accounts for first and last strings already defined
    
    if middleStringsCount > 0:
        i = 1
        for j in range(middleStringsCount):
            tempstr = string[0:i] + character + string[i:]
            stringList.append(tempstr)
            i += 1
    
    return stringList

            

def get_strings(string):
    '''
    Generates permutated strings based upon passed in string of length 3 
    characters or more. Assume string is non-empty or greater than 1 character.
    
      - If it receives a 2 character string, returns the 2 string permutation of a
    string.
      - If it receives a string longer than 2 characters, holds out (saves) the 1st 
      character and calls itself with the remainder string, passing it the remainder
      string.
      - returns a list of strings which is a permutation of the string it received
     when called

    Args:
        string (TYPE: str): alphanumeric string of characters to permeate and
        return list of strings which are string's permutations.

    Returns:
        list of strings [] containing permutated strings of input string

    '''
    retStringList = []

    stringLen = len(string)
    if stringLen < 2:
        if stringLen == 1:
            retStringList.append(string)
        return retStringList
        
    if stringLen == 2:
        string1 = string[0] + string[1]
        retStringList.append(string1)
        string2 = string[1] + string[0]
        retStringList.append(string2)
        return retStringList
        
    if stringLen > 2:
        leftChar = string[0:1]  # capture and save 1st character
        remainderString = string[1:]
        stringList = get_strings(remainderString)
        for stringListItem in stringList:
            stringList = permeate(stringListItem, leftChar)
            retStringList.extend(stringList)
        return retStringList
    


    # pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

