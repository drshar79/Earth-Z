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