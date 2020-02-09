def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
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
                print("'This is strange,'thought"" "+Name,'.')
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
                                        print("You keep staring. A few moments later, the 'man' turns and looks at you, their lifeless eyes leaving you shivering in your spine")  
                        StareOrweapon()

        else:
                print("That isn't one of your choices! Do you want to...")
                print("Go downstairs")
                print("Look out the window")
                downOrWindow()
downOrWindow()