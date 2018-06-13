# Week 3 Problem Set - Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:/Python/words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    listSecretWord = []
    for letter in secretWord:
        if letter not in listSecretWord:
            listSecretWord.append(letter)
    for letter in lettersGuessed:
        if letter in listSecretWord:
            listSecretWord.remove(letter)
            if len(listSecretWord) == 0:
                return True
    return False
        
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    dic = {}
    ans = ''
    for x in range(len(secretWord)):
        dic[x] = '_'
    for letter in lettersGuessed:
        if letter in secretWord:
            for x in range(0,len(secretWord)):
                if secretWord[x] == letter:
                    dic[x] = letter
    for letter in dic.values():
        ans = ans + ' ' + letter
    return(ans)
    
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    alphabet_ = list(string.ascii_lowercase)
    ans = ''
    
    for letter in lettersGuessed:
        for char in range(len(alphabet_)):
            if letter == alphabet_[char]:
                alphabet.remove(alphabet_[char])

    for x in alphabet:
        ans = ans + x
    
    return(ans)
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    count = 8
    
    lettersGuessed = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    ans = ''
    
    while count != 0:
        print('-----------')
        print('You have ' + str(count) + ' guesses left')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = str(input('Please guess a letter: '))
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord,lettersGuessed))
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess:' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word:' + getGuessedWord(secretWord, lettersGuessed)) 
                count -= 1
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('-----------')
            print('Congratulations, you won!')
            break
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
