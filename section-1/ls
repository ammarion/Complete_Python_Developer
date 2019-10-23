import sys
from random import randint


x = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = input("What is your guess: ")
        if 0 < int(guess) < 10:
            if int(guess) == x:
                print("Your are good!")
                break
        else:
            print("Please enter a number between 1 and")
            break
    except ValueError:
        print("Please enter a number")
        continue
