from random import *

RandomNumber = randint(1,420)
print(RandomNumber)

guessnumber = 0

while guessnumber <= 3:
    guess = input("Guess a number between 1 and 420:")
    if not guess.isnumeric():
        print("thats not a number, try again")
    else:
        guess = float(guess)

    if guess == RandomNumber:
        print("you got it correct, good job!")
    elif guess != RandomNumber:
        print("you got it wrong. You have", 3 - guessnumber, "guesses left")
    guessnumber += 1

if guessnumber > 3:
    print("you ran out of guesses sorry")
