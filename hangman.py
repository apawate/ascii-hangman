'''

ASCII Hangman by Agastya Pawate

A simple game of hangman implemented with ASCII characters.

@author: Agastya Pawate

April 15, 2021

'''




import os
import random
import time
from wordlists import words

os.system("clear")

options = ["easy", "medium", "hard", "crazy"]

hangman_words = words()

easywords = hangman_words.easywords

mediumwords = hangman_words.mediumwords

hardwords = hangman_words.hardwords

crazywords = hangman_words.crazywords

optionwords = [easywords, mediumwords, hardwords, crazywords]

print("Let's play hangman!")
choice = input("Choose a level: 1 is easy, 2 is medium, 3 is hard, and don't choose 4. " )
choice = int(choice) - 1
print("You chose the", options[choice], "level. Good luck!")
time.sleep(1)
os.system("clear")

gallows = "____________\n|__________|"

ropezero = " ______\n/      |\n|\n|\n|\n|\n|\n|"

ropeone = " ______\n/      |\n|     [_]\n|\n|\n|\n|\n|"

ropetwo = " ______\n/      |\n|     [_]\n|      | \n|\n|\n|\n|"

ropefour = " ______\n/      |\n|     [_]\n|      | \n|    -- --\n|\n|\n|"

ropethree = " ______\n/      |\n|     [_]\n|      | \n|    --\n|\n|\n|"

ropesix = " ______\n/      |\n|     [_]\n|      | \n|    -- --\n|      |\n|     / |\n|    /  |"

ropefive = " ______\n/      |\n|     [_]\n|      | \n|    -- --\n|      |\n|     / \n|    /  "

ropelist = ["\n\n\n\n\n\n\n", "\n\n\n\n\n\n\n", ropezero, ropeone, ropetwo, ropethree, ropefour, ropefive, ropesix]

gallows_state = False

guessed = True

round_num = 0

guess = ""

guessletters = []

def list_to_string(lst):
    string = ""
    newstring = ""
    for item in lst:
        string = string + item
    for letter in string:
        newstring = newstring + letter + ", "
    return newstring

word = random.choice(optionwords[choice])

while guess != "quit":
    os.system("clear")
    print(ropelist[round_num])
    if gallows_state:
        print(gallows)
    else:
        print()
    if round_num == 8:
        print("Game over!")
        print("The word was", word)
        guess = "quit"
    else:
        print()
        print("Guesses so far:", list_to_string(guessletters))
        print()
        for letter in word:
            if letter not in guessletters:
                print("_", end="")
                guessed = False
            else:
                print(letter, end="")
        if guessed:
            print()
            print("You won!")
            guess = "quit"
            break
        if not guessed:
            guessed = True
        print()
        guess = input("Enter a guess: ")
        if len(guess) == 1:
            guessletters.append(guess)
            if guess not in word:
                if not gallows_state:
                    gallows_state = True
                round_num = round_num + 1
        else:
            if guess != word:
                if not gallows_state:
                    gallows_state = True
                round_num = round_num + 1
            else:
                os.system("clear")
                print("You won!")
                guess = "quit"



    


       



