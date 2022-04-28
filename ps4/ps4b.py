# Problem Set 4B
# Name: G.A.
# Collaborators:
# Time Spent: x:xx

import string
import numpy as np

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
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        words = self.valid_words
        return words.copy()


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
         assert shift <= 26, "invalid shift value"
         assert type(shift) == int, "shift must be type: int"
         
         let = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
         values = list(let + let.upper())
         shift_dict = dict(zip(string.ascii_letters, values))
         shift_dict[" "] = " "  #this line maybe not necessary
         return shift_dict
 
     
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
        shift_dict = self.build_shift_dict(shift)
        shifted_word = ""
        for char in self.get_message_text():
            if char in string.ascii_letters:
                shifted_word += shift_dict[char]
            else:
                shifted_word += char
        
        return shifted_word[0:]
    
    def __str__(self):
        return self.text


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
        assert type(text) == str, "arg1 must be of type: str"
        assert type(shift) == int, "arg2 must be of type: int"
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift


    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        edict = self.encryption_dict
        return edict.copy()


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(shift)
        self.message_text_encrypted = Message.apply_shift(shift)

    def __str__(self):
        return "Text:", self.message_text, "Shift:", self.shift
    
    
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
        self.valid_words = load_words(WORDLIST_FILENAME)


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
        
        shift_scores = []
        for k in range(26):
            shift_scores.append(0) 
            decrypt = self.apply_shift(26 - k)
            words = decrypt.split(" ")
            
            for elt in words:
                if elt == "":
                    continue
                elif is_word(self.valid_words, elt):
                    shift_scores[k] += 1
                    
        real_shift = 26 - shift_scores.index(max(shift_scores))
        return (real_shift, self.apply_shift(real_shift)) 
    
    
    def __str__(self):
        return self.message_text
      

if __name__ == '__main__':

    
    #Example test case (PlaintextMessage)
    print("\n")
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    print("\n")
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    
    #Test Case 1 (PlaintextMessage)
    print("\n")
    plaintext = PlaintextMessage('Ah yes, my monkey booze', 17)
    print('Expected Output: Ry pvj, dp dfebvp sffqv')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    #Test Case 1 (CiphertextMessage)
    print("\n")
    ciphertext = CiphertextMessage('Ry pvj, dp dfebvp sffqv')
    print('Expected Output:', (9, 'Ah yes, my monkey booze'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    #Test Case 2 (PlaintextMessage)
    print("\n")
    plaintext = PlaintextMessage('zebra!@#$%^&*_', 6)
    print('Expected Output: fkhxg!@#$%^&*_')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    #Test Case 2 (CiphertextMessage)
    print("\n")
    ciphertext = CiphertextMessage('fkhxg!@#$%^&*_')
    print('Expected Output:', (20, 'zebra!@#$%^&*_'))   #bug prints wrong shift number
    print('Actual Output:', ciphertext.decrypt_message())
    
    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
