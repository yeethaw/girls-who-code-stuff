#importing libraries
from PIL import Image
from random import *
import webbrowser


#functions
def main():
    print("type in 'stop' to exit the program")
    while True:
        answer = input("What will you say?")
        process(answer)

def is_valid(answer , list):
    if answer in list:
        return True
    else:
        return False


def introduction():
    while True:
        print("I'm CHATBOT!")
        names = input("What's your NAME?")
        print("Wow, ", names.upper() ," that's a pretty name!")
        intro = 'done'
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
        mashiro2 = Image.open('images-for-code/mashiro3.jpg')
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

def joke():
    jokes = ['what do you call a can opener that wont work?','What do you get when you cross a rhetorical question and a joke?','did you hear about the italian chef?','what is forest gumps email password?','did you hear about the guy who invented the knock knock joke?']
    ran = randint(0 , len(jokes)-1)
    joke = jokes[ran]
    punchlines = ['a CANT opener','...','he PASTA-way','1forest1', 'he won a NO-BELL peace prize']
    punchline = punchlines[ran]
    what = input(joke)
    if what == 'what' or what == "what?" or what == 'What' or what == 'What?':
        print(punchline)
        print("hahahahahahahah")
    else:
        print("...")
        print("you had to say 'what'...")

def oho():
    img = Image.open('images-for-code/oho.png')
    img.show()

def how():
    feelings = ['bad','good','evil','stabby','anxious','happy','excited','sad','mad']
    feeling = feelings[randint(0 , len(feelings)-1)]
    print("I'm feeling " , feeling, '!')
    you = input("How are you feeling?")
    print("Good :)")

def video():
    links = ['https://www.youtube.com/watch?v=mk9jFGtUX0Y','https://www.youtube.com/watch?v=XQsMXoxVbUM','https://www.youtube.com/watch?v=YllrAmXfrME','https://www.youtube.com/watch?v=Bge_9DsoMWI']
    ran = randint(0,len(links)-1)
    link = links[ran]
    webbrowser.open(link)

def process(answer):
    hellow = ['whats up','hello','howdy','hi','mushi mushi','guten tag','konichiwa']

    if answer == 'stop':
        raise SystemExit
    elif is_valid(answer,hellow) == True:
        introduction()
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
    elif answer == 'UwU' or answer == 'uwu':
        print('OwO')
    elif answer == 'OwO' or answer == 'owo':
        print('UwU')
    elif answer == "tell me a joke":
        joke()
    elif answer == "show me a video":
        video()
    else:
        print("Cool beans!")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
