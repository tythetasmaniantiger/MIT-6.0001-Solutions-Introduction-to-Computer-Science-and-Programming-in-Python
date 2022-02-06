"""
Created on Thu Jan 27 02:10:31 2022

@author: tythetasmaniantiger
"""
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

# # end of helper code

# # -----------------------------------

# # Load the list of words into the variable wordlist
# # so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    return(set(secret_word) - set(letters_guessed) == set())

  
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else:
            guessed_word.append("_")
    guessed_word=" ".join(guessed_word)  
      
    return(guessed_word)
    
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for char in available_letters:
        if char in letters_guessed:
            available_letters = available_letters.replace(char,"")
            
    return(available_letters)
    
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
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    score = 0
    
    while guesses_remaining > 0:
        print("-" * 13)
        print("You have",guesses_remaining,"guesses left.")
        print("Letters remaining:",get_available_letters(letters_guessed))
        guess = (input("Please guess a letter: "))
        guess = guess.lower()
        guessed_word_before = get_guessed_word(secret_word, letters_guessed)
        
        # Checking if guessed letter is valid
        if guess not in string.ascii_lowercase or len(guess) > 1:
            warnings_remaining -= 1
            print("Oops! That is not a valid letter.")
            if warnings_remaining >= 0:
                print("You have",warnings_remaining,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("You have",guesses_remaining,"guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))    
            continue
        elif guess in letters_guessed:
            warnings_remaining -= 1
            print("Oops! You've already guessed that letter.")
            if warnings_remaining >= 0:
                print("You have",warnings_remaining,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("You have",guesses_remaining,"guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))    
            continue
        
        # Main game logic
        letters_guessed.append(guess)
        guessed_word_after = get_guessed_word(secret_word, letters_guessed)
        
        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word))
            break
        elif guessed_word_before != guessed_word_after:
            print("Good guess:",guessed_word_after)
        else:
            print("Oops! That letter is not in my word:",guessed_word_after)
            if guess in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
    #end of loop
    
    if score > 0:
        print("Congratulations, you won!")
        print("My word was:",secret_word)
        print("Your total score for this game is:",score)
    else:
        print("You are out of guesses! You lost.")
        print("My word was:",secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, letters_guessed, other_word):  #function modified from homework, uses letters_guessed
    '''
    Parameters: my_word: string with _ characters, current guess of secret word
        letters_guessed: list of strings containing all letters guessed
        other_word: string, regular English word
    Returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        "_" , and my_word and other_word are of the same length, and other_word
        contains no characters that have already been guessed
        False otherwise: 
    '''
    possible_match = True
    my_word = my_word.replace(" ","")
    if len(my_word) != len(other_word):
        possible_match = False
    else:   
        for k in range(len(other_word)):
            if my_word[k] == "_" and other_word[k] in letters_guessed:
                possible_match = False
                break
            elif my_word[k] != "_" and my_word[k] != other_word[k]:
                possible_match = False
                break
        
        return(possible_match)

    
def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    print("Possible matches:")
    for k in range(len(wordlist)):
        if match_with_gaps(my_word,letters_guessed,wordlist[k]):
            print(wordlist[k])
    return("")
    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    score = 0
    hints_remaining = 3
    
    while guesses_remaining > 0:
        print("-" * 13)
        print("You have",guesses_remaining,"guesses left.")
        print("Letters remaining:",get_available_letters(letters_guessed))
        
        # Checking if hint is available
        hint_available = False
        if hints_remaining > 0 and len(letters_guessed) > 0:
            hint_available = True
            print("Enter '*' for a hint.")
            
        guess = (input("Please guess a letter: "))
        guess = guess.lower()
        guessed_word_before = get_guessed_word(secret_word, letters_guessed)
        
        # Checking if guessed letter is valid. Invalid -> restart loop
        if guess == "*" and hint_available:
            hints_remaining -= 1
            print(show_possible_matches(guessed_word_before, letters_guessed))
            continue
        elif guess == "*" and hints_remaining == 0:
            hints_remaining -= 1
            print("Oh no! You are out of hints.")
            continue
        elif guess not in string.ascii_lowercase or len(guess) > 1:
            warnings_remaining -= 1
            print("Oops! That is not a valid letter.")
            if warnings_remaining >= 0:
                print("You have",warnings_remaining,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("You have",guesses_remaining,"guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))    
            continue
        elif guess in letters_guessed:
            warnings_remaining -= 1
            print("Oops! You've already guessed that letter.")
            if warnings_remaining >= 0:
                print("You have",warnings_remaining,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("You have",guesses_remaining,"guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))    
            continue
        
        # Main Game Logic
        letters_guessed.append(guess)
        guessed_word_after = get_guessed_word(secret_word, letters_guessed)
        
        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word))
            break
        elif guessed_word_before != guessed_word_after:
            print("Good guess:",guessed_word_after)
        else:
            print("Oops! That letter is not in my word:",guessed_word_after)
            if guess in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
    #end of loop
    
    if score > 0:
        print("Congratulations, you won!")
        print("My word was:",secret_word)
        print("Your total score for this game is:",score)
    else:
        print("You are out of guesses! You lost.")
        print("My word was:",secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)