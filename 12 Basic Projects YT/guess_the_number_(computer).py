# The computer will generate a random number, which we then have to guess

import random

def guess(x) : 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = input(f"Guess a number between 1 and {x}: ")
        try :
            guess = int(guess)
            if guess < random_number :
                print("Too low, try again")
            elif guess > random_number :
                print("Too high, try again") 
        except :
            print("Input a number") 
    print(f"Correct number {random_number}")
guess(1000)