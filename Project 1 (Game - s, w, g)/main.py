import random    # Importing the random module

# THE GAME FUNCTION

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


# COMPUTER'S TURN 

randNo = random.randint(1,3)

if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'

# TAKING INPUT FROM USER

you = input("\nComputer Chose\n\nYour Turn::: \nType 's' for Snake \nType 'w' for Water \nType 'g' for Gun\n\n")
a = gameWin(comp, you)

# PRINTING THE CHOICE OF BOTH

print(f"\nComputer Chose: '{comp}'")
print(f"You chose: '{you}'\n")

#PRINTING THE RESULT

if a == None:
    print(f"Match Tied!\n")
elif a:
    print(f"You Won!\n")
else:
    print(f"You Lose!\n")