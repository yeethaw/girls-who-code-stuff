from random import *

#variables
max = 7
fails = 0
sofar = []

#list of words that could be randomly picked
words = ['artist' , 'spiderman', 'multiverse' , 'science' , 'animation', "oregano", 'dog', 'skrt' , 'yeet','thicc' , 'wacc']

#picking the word from the list and converts that into a list
pickwordnum = randint(0, len(words)-1)
pickword = words[pickwordnum]
word = list(pickword)
guessword = []

#replacing letters with spaces
for letter in word:
    guessword = guessword + [' ']

#game stuff
while fails < max :
    #prints spaces
    print(guessword)
    #input for guess
    guess = input("guess a letter : ")

    #can't repeat guesses
    if guess in sofar:
        print("you've already guessed that!")
        print("Guesses so far: " , sofar)
    else:
        #shows guesses
        sofar.append(guess)
        print("Guesses so far: " , sofar )

    #replaces spaces with letters
    for idx, letter in enumerate(word):
        if letter == guess:
            guessword[idx] = guess

    #adds to fail tally if the guess is wrong
    if guess not in word :
        fails = fails + 1

    #when completed
    if guessword == word :
        print("You got it! the word was " + pickword + '!')
        break

    #prints the amount of tries left
    print("You have " + str(max - fails) + " tries left")
