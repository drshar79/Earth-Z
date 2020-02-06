def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
def Begin():
    Name=input("Enter your name: ")
    Start=input("Type in 'Start' to begin: ")
    if Start=="Start":
            clear()
    print('You wake up with a start after a long and dreamless sleep.')
    print("'Time for another greuling day of medical school...Ugh.' You groan as you get out of bed.")
    print("Do you...")
    print("Go downstairs")
    print("Look out the window")
def downOrWindow():
        ans = input()
        if ans== "Go downstairs":
                clear()
                print("as you make your way downstairs, you notice that all is silent; no cars, no birds chirping, nothing except for the soft wind blowing against the house.")
                print("Do you...")
                print("Go out the front door")
                print("Go out the back door")
        elif ans=="Look out the window":
                        clear()
                        print("You open you window blinds and look out into the foggy morning.")
                        print("You stare in horror, as you witness a zombie eating the flesh of a near-dead man; their screams becoming softer and softer.")
                        print("Do you...")
                        print("Continue to stare")
                        print("Grab a weapon")
        else: 
            Incorrect()
            downOrWindow()
def Incorrect():
    print("That isn't one of your choices!")
def BackDoor():
    ans=input()
    if ans=="Go out the back door":
        clear()
        print("You go out the back door, and find a zombie with its back turned to you. It turns around and meets your eye.")
        print("The zombie dashes over with terrifying speed, and closes its mouth around your neck.")
        Begin()
        downOrWindow()
        BackDoor()
    else:
        Incorrect()
        BackDoor()
def GrabWeapon():
    ans=input()
    if ans=="Grab a weapon":
        print("You grab a shotgun from your closet. 4 shells come with it. ")
        print("'I have to get out of here and find survivors!' You open your front door to find that the road is stranded.")
        print("There are two neighboring houses on either side. Do you go to the house on the...")
        print("Left")
        print("Right")
def RightHouse():
    print("You go the house on the left, shotgun in hand, and open the door.")
    print("You see a Woman coming at you with a knife, screaming. She looked normal.")
    print(" 'Wait! I'm not infected!' You shout.")
    print("The woman stops in her tracks and lowers her pocket knife")
    print("'Oh, I'm sorry.' She says. What's your name? You're the first person that actually looks normal.")
    print()


Begin()
downOrWindow()
BackDoor()
GrabWeapon()