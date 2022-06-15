import random
from words import words
import string #For alphabet function below

def get_valid_word(words):
    word = random.choice(words) #Randomly chooses a value from a list
    while '-' in word or ' ' in word: #This will keep choosing a word if the chosen word has a space or dash
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) #Calling the get valid word function we created above
    word_letters = set(word) #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed 

    lives = 11

    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives remaining \n'
            'You have used these letters: ', ' '.join(used_letters)) #this will print out the letters already used
        #What current word is i.e W - R D
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Type a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #Takes away a life if the wrong letter is input
                print('Letter is not in the word, try again: ')

        elif user_letter in used_letters:
            print('You have already used that character, please try again: ')
        else:
            print('invalid character, please try again')
    #While word length is greater than 0, or lives are greater  this loop will keep running
    if lives == 0:
        print('You failed loser, the word was', word)
    else:
        print('Well done nerd, you guessed that the word was', word)

hangman()