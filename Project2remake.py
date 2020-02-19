Name=input("Type in your name: ")
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
                clear()
                frontOrBack()
        elif ans == "Look out the window":
                clear()
                GrabWeaponOrStare()
        else:
                Incorrect()
                downOrWindow()


def Incorrect():
    print("That isn't one of your choices!")


def frontOrBack():
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
                print(". . .")
                print("You go out the back door, and find a zombie with its back turned to you. It turns around and meets your eye.")
                print("The zombie dashes over with terrifying speed, and closes its mouth around your neck.")
                print("'What a depressing way to die,' You say to yourself")
                Begin()
        else:
                Incorrect()
                frontOrBack()
def Congrats():
        print("Type in 'Stow':")
        ans=input()
        if ans=="Stow":
                print("You stow the blaster and get out of the hospital, surviving day one of the zombie apocalypse.")
                print("Congratulations, "+Name)
                print("You beat the game! Type in 'Restart' If you wish to play again!")
        else:
                Incorrect()
                Congrats()
        ans2=input()
        if ans2=="Restart":
                Begin()
def BarricadeOrIgnore():
        print("Suddenly, you hear a bang on the door, and some low growling. the banging gets louder as more and more zombies pile upon each other.")
        print("However, you're almost done with the weapon.")
        print("Do you...")
        print("Barricade the door")
        print("Keep working")
        ans=input()
        if ans== "Barricade the door":
                clear()
                print("You barricade the door with metal rod and some tables. They won't be able to get in for a while")
                print("You finish the antidote in the shape of a blaster, and, on cue, the zombies burst open the door and come rushing in.")
                print("You shoot the zombie with the antidote, and their heads explode.")
                print("Luckily, you surive because of the gas mask, and you keep shooting until there's no one left. ")
                print(". . .")
                Congrats()
        elif ans=="Keep working":
                clear()
                print("The zombies break in and overwhelm you. You can only get one shot off of your blaster containing the antidote, before they kill you.")
                Begin()
        else:
                Incorrect()
                BarricadeOrIgnore()
def CarOrRun():
        print("Do you...")
        print("Drive")
        print("Run")
        ans=input()
        if ans=="Drive":
                clear()
                print("You start up your car and drive to the hospital. Once you get there, you start searching for the lab.")
                print("Luckily, you found the lab without any zombies spotting you, and you get to work.")
                BarricadeOrIgnore()
        elif ans=="Run":
                clear()
                print("With your backpack, you run to the hospital. Unfortunately, 5 zombies spotted you and are catching up fast")
                Shootx4OrRun()
        else:
                Incorrect()
                CarOrRun()
def RightOrLeft():
        ans=input()
        if ans=="Left":
                print("You go the house on the left, shotgun in hand, and open the door.")
                print("The house is empty and you investigate its surroundings")
                print("You find a gas mask")
                PutOnOrNot()
        elif ans=="Right":
                print("You go to the house on the right, shotgun in hand, and open the door.")
                print("A zombie appears in front of you. It turns around and charges at you.")
                ShootOrWhack()
        else:
                Incorrect()
                RightOrLeft()
                
def ShootOrWhack():
        print("Do you...")
        print("Shoot the zombie")
        print("Whack it")
        ans=input()
        if ans=="Shoot the zombie":
                clear()
                print("You shoot the zombie in the face, and it drops to the floor dead. You now have three shotgun shells left.")
                print("You start to investigate the house. You find a backpack with medical supplies and an old, rusty book.")
                print("The book reads: 'A Hypothetical Weapon For Zombies If Ever Needed' ")
                print("'Well, this is perfect!' You say")
                print("The backpack contains the materials needed to create the weapon. All you need is to get to a lab; and the hospital is the perfect place to do so. ")
                CarOrRun()
        elif ans== "Whack it":
                clear()
                print("You smack the zombie as hard as you can with the butt of your rifle multiple times. You take it down.")
                print("However, it left a large gash across your chest, and blood flows out.")
                print("You start to investigate the house. You find a backpack with medical supplies and an old, rusty book.")
                BandageOrRubOrNot()

        else:
                Incorrect()
                ShootOrWhack()
def GrabWeaponOrStare():
        print("You open you window blinds and look out into the foggy morning.")
        print("You stare in horror, as you witness a zombie eating the flesh of a near-dead man; their screams becoming softer and softer.")
        print("Do you...")
        print("Keep staring")
        print("Grab a weapon")
        ans = input()
        if ans == "Grab a weapon":
                clear()
                print("You grab a shotgun from your closet. 4 shells come with it. ")
                print("'I have to get out of here and find survivors!' You open your front door to find that the road is stranded.")
                print("You see a dead man across the street, with his head severed from his body.")
                print("There are two neighboring houses on either side. Do you go to the house on the...")
                print("Left")
                print("Right")
                RightOrLeft()
        elif ans == "Keep staring":
                clear()
                print("You keep staring. A few moments later, the 'man' turns and looks at you, its lifeless eyes leaving you a shiver down your spine") 
                print("You yelp and leap away from the window. You hear a shrill scream and footsteps getting closer. They're coming to your house!")
                OpenwindowOrDown()
        else:
                Incorrect()
                GrabWeaponOrStare()
def OpenwindowOrDown():
        print("Do you...")
        print("Open window and escape")
        print("Go downstairs")
        ans=input()
        if ans=="Open window and escape":
                clear()
                print("You open your window and jump down the two story house.")
                print("You land on your ankle with a sickening crack. You can't put weight on it.")
                print("You notice the zombie is a few yards to your left, but is too preoccupied on the house to notice you.")
                AttackOrRight()
        elif ans=="Go downstairs":
                frontOrBack()
def AttackOrRight():
        print("Do you...")
        print("Attack the zombie")
        print("Flee")
        ans=input()
        if ans=="Attack the zombie":
                clear()
                print("You limp towards the zombie and punch it in the face")
                print("The zombie is unfazed and grabs your neck")
                print("You suffocate until your life is no more")
                Begin()
        elif ans=="Flee":
                clear()
                print("You limp to the house on your right, and find out the door is unlocked.")
                print("Once you open the door, you find a zombie and it rushes at you.")
                print("You try your best to fend it off, despite the fact that you're injured and defenceless.")
                print("The zombie closes its jaws around your neck.")
                Begin()
        else:
                Incorrect()
                AttackOrRight()
def PutOnOrNot():
        print("Do you...")
        print("Put it on")
        print("Ignore it")
        ans=input()
        if ans=="Put it on":
                clear()
                print("You put the gas mask on.")
                print("You walk out of the house and decide to investigate the one on the right.")
                print(". . .")
                print("You open the door, and a zombie appears. It charges at you.")
                ShootOrWhack()
        elif ans=="Ignore it":
                clear()
                print("You ignore the mask and walk out of the house. You decide to investigate the one on the right.")
                print(". . .")
                print("You open the door, and a zombie appears. It charges at you.")
                ShootOrWhack()
        else:
                Incorrect()
                PutOnOrNot()
def BandageOrRubOrNot():
        print("Do you...")
        print("Bandage the wound")
        print("Apply rubbing alcohol")
        print("Ignore it")
        ans=input()
        if ans=="Bandage the wound":
                clear()
                print("You bandage the wound")
                print("The wound gets infected and you die from bacterial infection")
                Begin()
        elif ans=="Apply rubbing alcohol":
                clear()
                print("You put on some rubbing alcohol you found in the backpack and bandage it up.")
                print("The book reads: 'Death for Zombies If Ever Needed' ")
                print("'Well, this is perfect!' You say")
                print("The backpack contains the materials needed to create the vaccine. All you need is to get to a lab; and the hospital is the perfect place to do so. ")
                CarOrRun()
        elif ans=="Ignore it":
                clear()
                print("You ignore the wound and it gets infected")
                print("You die from bacterial infection")
                Begin()
        else:
                Incorrect()
                BandageOrRubOrNot()
def Shootx4OrRun():
        print("Do you...")
        print("Shoot the zombies")
        print("Keep running")
        ans=input()
        if ans=="Shoot the zombies":
                clear()
                print("You turn around and shoot the zombies")
                print("Unfortunately, you ran out of bullets and perished to the remaining left")
                Begin()
        elif ans=="Keep running":
                clear()
                print("You keep running and the zombies catch up to you. You try to raise your gun but they bite your arm off.")
                print("You die from septic shock before they actually kill you.")
                Begin()
        else:
                Incorrect
                Shootx4OrRun()
Begin()