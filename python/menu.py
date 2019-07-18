#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
sides = ['Fries', 'Salad' , 'Soup','Tide Pod']
main = ['Spaghetti','Pancakes','Pizza','Hamburger','Ramen','Sushi','Fish','Tide Pod']
dessert = ['Cookie','Ice Cream','Tide Pod','Macaroons','Mochi']

#Generates a random integer.
randoside = randint(0, len(sides)-1)
randomain = randint(0, len(main)-1)
randodess = randint(0, len(dessert)-1)

print(sides[randoside] + ' ' + main[randomain] + ' ' + dessert[randodess])
