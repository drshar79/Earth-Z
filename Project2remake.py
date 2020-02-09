Name = input("Enter your name: ")


def clear():
    from os import system, name
    # for windows
    if name == 'nt':
        _ = system('cls')


def Begin():
    Start = input("Type in 'Start' to begin: ")
    if Start == "Start":
        clear()
    print('You wake up with a start after a long and dreamless sleep.')
    print("'Time for another greuling day of medical school...Ugh.' You groan as you get out of bed.")
    
    downOrWindow()


def downOrWindow():
        print("Do you...")
        print("Go downstairs")
        print("Look out the window")
        ans = input()
        if ans == "Go downstairs":
                frontOrBack()
        elif ans == "Look out the window":
                GrabWeaponOrStare()
        else:
                Incorrect()
                downOrWindow()


def Incorrect():
    print("That isn't one of your choices!")


def frontOrBack():
        clear()
        print("as you make your way downstairs, you notice that all is silent; no cars, no birds chirping, nothing except for the soft wind blowing against the house.")
        print("Do you...")
        print("Go out the front door")
        print("Go out the back door")
        ans = input()
        if ans == "Go out the back door":
                clear()
                print("You go out the back door, and find a zombie with its back turned to you. It turns around and meets your eye.")
                print("The zombie dashes over with terrifying speed, and closes its mouth around your neck.")
                Begin()
        elif ans == "Go out the front door":
                print("You open the front door and go outside. There, you see a zombie eating the flesh of a dead man, their blood spilling on the ground around them.")
                print("They turn around and look at you, a severed arm in their mouth.")
                print("You scream and slam the door shut. Your only option is to go out the back door. ")
                clear()
                print("You go out the back door, and find a zombie with its back turned to you. It turns around and meets your eye.")
                print("The zombie dashes over with terrifying speed, and closes its mouth around your neck.")
                print("'What a depressing way to die,' You say to yourself")
                Begin()
        else:
                Incorrect()
                frontOrBack()





def RightOrLeft():
        ans=input()
        if ans=="Left":
                print("You go the house on the left, shotgun in hand, and open the door.")
                print("You see a woman coming at you with a knife, screaming. She looked normal.")
                print("'Wait! I'm not infected!' You shout.")
                print("The woman stops in her tracks and lowers her pocket knife")
                print("'Oh, I'm sorry.' She says. What's your name? You're the first person i've seen that actually looks normal.")
        elif ans=="Right":
                print("You go to the house on the right, shotgun in hand, and open the door.")
                ShootOrWhack()
                
def ShootOrWhack():
        print("Do you...")
        print("Shoot the zombie")
        print("Whack it")
        ans=input()
        if ans=="Shoot the zombie":
                print("You shoot the zombie in the face, and it drops to the floor dead. You now have three shotgun shells left.")
                print("You start to investigate the house. You find a backpack with medical supplies and an old, rusty book.")
        elif ans== "Whack it":
                print("You smack the zombie as hard as you can with the butt of your rifle multiple times. You take it down.")
                print("However, it left a large gash across your chest, and blood flows out.")
def GrabWeaponOrStare():
        clear()
        print("You open you window blinds and look out into the foggy morning.")
        print("You stare in horror, as you witness a zombie eating the flesh of a near-dead man; their screams becoming softer and softer.")
        print("Do you...")
        print("Continue to stare")
        print("Grab a weapon")
        ans = input()
        if ans == "Grab a weapon":
                print("You grab a shotgun from your closet. 4 shells come with it. ")
                print("'I have to get out of here and find survivors!' You open your front door to find that the road is stranded.")
                print("You see a dead man across the street, with his head severed from his body.")
                print("There are two neighboring houses on either side. Do you go to the house on the...")
                print("Left")
                print("Right")
                RightOrleft()
        elif ans == "Continue to stare":
                pass
Begin()
ddsfdf