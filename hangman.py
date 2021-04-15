import os
import random
import time

os.system("clear")

options = ["easy", "medium", "hard", "crazy"]

easywords = ["bat", "rat", "cat", "dog", "big", "hello", "word", "easy", "phone", "man", "woman", "book", "door", "wind", "tree"]

mediumwords = ["frame", "computer", "apply", "world", "wallpaper", "notebook", "ocean", "waves", "handle", "chess", "calendar", "binder", "heater"]

hardwords = ["application", "rhythm", "xylophone", "lightning", "quizzical", "radioed", "architect", "sequoia", "tyrannical", "quirkiness"]

crazywords = ["prophaeletherium", "diophantus", "supercalifragilisticexpialidocious", "teleconferencing", "deoxyribonucleic", "developmentally", "metallurgical"]

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

round_num = 0

guess = ""

guessletters = []

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
        for letter in word:
            if letter not in guessletters:
                print("_", end="")
            else:
                print(letter, end="")
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



    


       



