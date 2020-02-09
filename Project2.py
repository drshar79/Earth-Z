def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
Name=input("Enter your name")
Start=input("Type in 'Start' to begin: ")
if Start=="Start":
        clear()
def downOrWindow():
        ans = input()
        if ans== "Go downstairs":
                print("as you make your way downstairs, you notice that all is silent; no cars, no birds chirping, nothing except for the wind blowing against the house")
                print("'This is strange,'thought"" "+Name,'.')
<<<<<<< HEAD
=======
                print("Do you...")
                print("Go out the front door")
                print("Go out the back door")
        elif ans=="Look out the window":
                        clear()
                        print("You open you window blinds and look out into the foggy morning.")
                        print("You stare in horror, as you witness a man eating the flesh of a near-dead man; their screams becoming softer and softer. ")
                        print("Do you...")
                        print("Continue to stare")
                        print("Grab a weapon")
                        def StareOrweapon():
                                ans=input()
                                if ans=="Continue to stare":
                                        clear()
                                        print("You keep staring. A few moments later, the 'man' turns and looks at you, their lifeless eyes leaving you a shiver down your spine") 
                                        print("You yelp and leap away from the window. You hear a shrill scream and footsteps getting closer. They're coming to your house!")
                                elif ans== "Grab a weapon":
                                        clear()
                                        print("You picked up a shotgun that was lying in your closet. four shells came with it.")
                                        print("You run downstairs to your basement and hide behind a couch. You hear faint screams of victims faraway.") 
                        StareOrweapon()
>>>>>>> 94fd6781a8e369438898af9ecd4581337d3dde59
        else:
                print("That isn't one of your choices! Do you want to go downstairs, or look out the window?")
                downOrWindow()
print('You wake up with a start after a long and dreamless sleep.')
print("'Time for another greuling day of medical school...Ugh.' You groan as you get out of bed")
print("Do you...")
print("Go downstairs")
print("Look out the window")
if ans=="Look out the window":
        print("You open you window blinds and look out into the foggy morning.")
        print("")

downOrWindow()