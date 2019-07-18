#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
first = ['Jason', 'Alison', 'Tim','Abcde', 'Luna','Harry','John' ,'Gabriel']
last = ['Todd', 'Nikols','Lovegood','Morozov','Reyes','Malfoy','Amari']

#Generates a random integer.
randofirst = randint(0, len(first)-1)
randolast = randint(0, len(last)-1)

print(first[randofirst] + ' ' + last[randolast])
