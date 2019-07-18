#importing libraries
from PIL import Image
from random import *


#functions
def main():
    print("type in 'stop' to exit the program")
    while True:
        answer = input("What will you say?")
        process(answer)


def introduction():
    while True:
        print("I'm CHATBOT!")
        names = input("What's your NAME?")
        print("Wow, ", names.upper() ," that's a pretty name!")
        break

def intro_no_name():
    print("I'm CHATBOT!")

def greeting():
    print("Hi there!")
    introduction()

def goodgirl():
    ran = randint(1,7)
    if ran == 1:
        mina = Image.open('images-for-code/mina.jpg')
        mina.show()
    elif ran == 2:
        gwen = Image.open('images-for-code/gwen.png')
        gwen.show()
    elif ran == 3:
        gwen2 = Image.open('images-for-code/gwen-2.jpg')
        gwen2.show()
    elif ran == 4:
        peni = Image.open('images-for-code/peni.jpg')
        peni.show()
    elif ran == 5:
        peni2 = Image.open('images-for-code/peni-2.jpg')
        peni2.show()
    elif ran == 6:
        zero = Image.open('images-for-code/zero.jpg')
        zero.show()
    elif ran == 7:
        mashiro = Image.open('images-for-code/mashiro.jpg')
        mashiro.show()

def goodboy():
    ran = randint(1,5)
    if ran == 1:
        shiba2 = Image.open('images-for-code/shiba-2.jpg')
        shiba2.show()
    elif ran == 2:
        shiba = Image.open('images-for-code/shiba.jpg')
        shiba.show()
    elif ran == 3:
        miles = Image.open('images-for-code/miles.jpg')
        miles.show()
    elif ran == 4:
        miles2 = Image.open('images-for-code/miles-2.jpg')
        miles2.show()
    elif ran == 5:
        miles3 = Image.open('images-for-code/miles-3.jpg')
        miles3.show()

def waifu():
    ran = randint(1,5)
    if ran == 1:
        holo = Image.open('images-for-code/holo.jpg')
        holo.show()
    elif ran == 2:
        mashiro2 = Image.open('images-for-code/mashiro-2.jpg')
        mashiro2.show()
    elif ran == 3:
        senko = Image.open('images-for-code/senko.jpg')
        senko.show()
    elif ran == 4:
        tohru = Image.open('images-for-code/Tohru.png')
        tohru.show()
    elif ran == 5:
        zero = Image.open('images-for-code/zero-waif.jpg')
        zero.show()


def oho():
    img = Image.open('images-for-code/oho.png')
    img.show()

def how():
    feelings = ['bad','good','evil','stabby','anxious','happy','excited','sad','mad']
    feeling = feelings[randint(0 , len(feelings)-1)]
    print("I'm feeling " , feeling, '!')
    you = input("How are you feeling?")
    print("Good :)")

def process(answer):
    if answer == 'hi'or answer == 'howdy':
        greeting()
    elif answer == 'stop':
        raise SystemExit
    elif answer == 'who are you' :
        intro_no_name()
    elif answer == 'show me a good girl':
        goodgirl()
    elif answer == 'show me a good boy' :
        goodboy()
    elif answer == 'ohoho' :
        oho()
    elif answer == 'skrt skrt':
        print("SKRT SKRT")
    elif answer == 'how are you':
        how()
    elif answer == 'give me a waifu':
        waifu()
    else:
        print("Cool beans!")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
