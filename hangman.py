import os
import random
import time

os.system("clear")

options = ["easy", "medium", "hard", "crazy"]

easywords = ["bat", "rat", "cat", "dog", "big", "hello", "word", "easy", "phone", "man", "woman", "book", "door", "wind", "tree"]

mediumwords = ["frame", "computer", "apply", "world", "wallpaper", "notebook", "ocean", "waves", "handle", "chess", "calendar", "binder", "heater"]

hardwords = ["application", "rhythm", "xylophone", "lightning", "quizzical", "radioed", "architect", "sequoia", "tyrannical", "quirkiness"]

crazywords = ["prophaeletherium", "diophantus", "supercalifragilisticexpialidocious", "teleconferencing", "deoxyribonucleic", "developmentally", "metallurgical"]

print("Let's play hangman!")
choice = input("Choose a level: 1 is easy, 2 is medium, 3 is hard, and don't choose 4. " )
print("You chose the", options[int(choice) - 1], "level. Good luck!")
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

ropelist = ["\n\n\n\n\n\n\n", ropezero, ropeone, ropetwo, ropethree, ropefour, ropefive, ropesix]

for rope in ropelist:
    os.system("clear")
    print(rope)
    print(gallows)
    time.sleep(1)

       



