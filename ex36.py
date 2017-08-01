from sys import exit

def start():
    print "You got lost and be in a massive forest."
    print "Now which direction do you want to choose?"
    print "East or west?"

    choice = raw_input("> ")

    if choice == "east":
        east_sea()
    elif choice == "west":
        west_desert()
    else:
        dead("You idiot!")

def dead(why):
    print why
    exit(0)

def east_sea():
    print "Beautiful sea is in front of you!"
    print "Somewhere in the sea is an island named Neverland."
    print "How can you arrive Neverland?"
    cross_sea = False

    while True:
        choice = raw_input("> ")

        if choice == "swim":
            dead("You will be exausted.")
        elif choice == "find a boat" and not cross_sea:
            print "Smart boy! What else should you prepare?"
            cross_sea = True
        elif choice == "find a boat" and cross_sea:
            dead("You will be exausted!")
        elif choice == "food and water" and cross_sea:
            neverland()
        else:
            print "Sorry, you should find another way."


def neverland():
    print "Welcome to Neverland!"
    print "Do you like here?"

    choice = raw_input("> ")

    if choice == "yes":
        print "Good taste! You can stay here."
        exit(0)
    else:
        dead("Go to hell!")


def west_desert():
    print "Poor guy. You choose a tough way."
    print "Be strong and you can survive."
    print "Horse or camel? Choose one."

    choice = raw_input("> ")

    if "horse" in choice:
        print "You can go back."
        start()
    elif "camel" in choice:
        print "Bring enough water and find a guide, then you can go across the desert."
        exit(0)
    else:
        west_desert()


start()
