
print("Hello there OLIVER THE DUCK, how are you doing? Good? Bad? Doesnt matter to me really...")

room = "main room"
alive = True

while(True):
    if alive == False :
        break

    while room == "main room":
            mainmove = input("would you like to go to the up room , outside, or the right room ")
            if mainmove == "up room":
                room = "up room"
            elif mainmove == "outside":
                room = "outside"
            elif mainmove == "right room":
                room = "right room"
            else:
                print("that's not an option ")


    while room == "up room":
        print("You enter an empty room with a desk and chair... nothing to see here")
        uproomex = input("would you like to go back?")
        if uproomex == "yes":
            print("a demon appears before you!")
            print("demon: you're gonna have a bad time, kid")
            escape = input("would you like to escape this hell?")
            if escape == "yes":
                print("you can't escape this hell")
            elif escape == "no, demons are hot":
                print("demon: screw that")
                room = "main room"
                print("you're back in the main room")
        if uproomex == "no":
            print("you stay in the room")
            uproomex = input("would you like to go back?")

    while room == "outside":
        print("you're in space, you cant breathe. I recommend going back inside.")
        inside = input("Go back inside?")
        if inside == "yes":
            print("you're back in the main room")
            room = "main room"
        elif inside == "no":
            print("you died")
            alive = False
            break


    while room == "right room":
        print("There is a dog. You've never seen him before. They look kinda sad.")
        dog = input("Do you pet the dog?")
        if dog == "yes":
            print("the dog looks happy now")
        elif dog == "no":
            print("the dog somehow looks sadder")
        rightex = input("Would you like to go back?")
        if rightex == "yes":
            print("You're back in the main room")
            room = "main room"
        if rightex == "no":
            if dog == "yes":
                print("you share an awkard silence with the dog")
            elif dog == "no":
                print("the dog attacks you. you've died")
                alive = False
                break
