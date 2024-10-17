import sys
import random

# Player data
player = {
    "name" : "Player1",
    "items" : [],
    "location" : "room1"
}

rooms = {
    "room1" : "deep forest",
    "room2" : "rush",
    "room3" : "lake"
    }

# Story elements
def printGraphic(name):
    if name == "tree":
        print("         _-_         ")
        print("      /~~   ~~\\      ")
        print("   /~~         ~~\\   ")
        print("  {               }  ")
        print("   \\  _-     -_  /   ")
        print("    ~    \\ //  ~     ")
        print("  _- -   | | _- _    ")
        print("    _ -  | |   -_.   ")
        print("        //  \\.       ")
        print("                     ")
        print("   It's a tree.")

    if name == "mirror":
        print("     _______        ")
        print("    /       \\       ")
        print("   /         \\      ")
        print("  |           |     ")
        print("  |           |     ")
        print("  |   MIRROR   |    ")
        print("   \\         /      ")
        print("    \\_______/       ")
        print("                   ")
        print("  A shiny mirror!")

    if name == "witch":
        print("        /\\         ")
        print("       /  \\        ")
        print("      /    \\       ")
        print("     /______\\      ")
        print("     | WITCH |     ")
        print("     |      /      ")
        print("     |     /       ")
        print("     |____/        ")
        print("                   ")
        print("  A mysterious witch!")

    if name == "rabbit":
        print("   (\\(\\            ")
        print("   ( -.-)          ")
        print("   o_(\"\")        ")
        print("                   ")
        print(" A rabbit!")


# Dice roll logic
def rollDice(minNum, maxNum, difficulty):
    result = random.randint(minNum, maxNum)
    print("You roll:" + str(result) + " out of " + str(maxNum))

    if result >= difficulty: 
        print("You succeeded!")
        return True
    else:
        print("You failed! Trying again...")
        input("Press Enter to roll again >")
        return rollDice(minNum, maxNum, difficulty)

# End the game
def gameOver():
    print("You are lost in the forest, never to find your way out. Game over.")
    sys.exit()

#Forest story with rooms and dice roll
def enterForest():
    print("You step into " + str(rooms["room1"]) + ". After walking for a while, you find a large tree,")
    printGraphic("tree")
    input("Press Enter to continue > ")

    print("As you continue walking, you notice a small, shiny mirror on the ground")
    printGraphic("mirror")

    pcmd = input("Do you want to pick up the mirror? (yes or no) > ")

    if pcmd == "yes":
        print("You pick up the mirror. Suddenly, the mirror begins to speak...")
        pcmd = input("Do you respond to the mirror? (yes or no) > ")
        
        if pcmd == "yes":
            print("The mirror tells you it can help you escape the forest, but it may be risky.")
            input("Press Enter to continue > ")
            success = rollDice(1, 6, 3) 
            
            if success:
                print("You successfully follow the mirror's advice.")
                player["location"] = "room2"
                encounterWitch()
            else:
                print("You couldn't follow the mirror's advice. You're still lost.")
                lostInForest()
                
        else:
            print("You ignore the mirror and keep walking.")
            lostInForest()
            
    else:
        print("You decide to leave the mirror and keep walking.")
        lostInForest()

# Get lost in the forest
def lostInForest():
    print("You walk aimlessly through " + str(rooms["room1"]) + " and find yourself back at the tree. You're lost.")
    gameOver()

# Encounter with the witch
def encounterWitch():
    print("You move along the path and suddenly enter " + str(rooms["room2"]) + ". There, you encounter a mysterious witch.")
    printGraphic("witch")

    pcmd = input("The witch offers to buy the mirror from you. Do you want to sell it? (yes or no) > ")

    if pcmd == "yes":
        print("The witch gives you a pile of gold, but you cannot carry it out of the forest. You die next to the treasure.")
        gameOver()
    else:
        print("You refuse to sell the mirror and continue your journey.")
        success = rollDice(1, 4, 2)  

        if success:
            rabbitAppears()
        else:
            print("You wander into another part of the forest and get lost.")
            lostInForest()

# Rabbit appears
def rabbitAppears():
    print("As you move towards " + str(rooms["room3"]) + ", the mirror suddenly transforms into a rabbit!")
    printGraphic("rabbit")
    input("Press Enter to continue > ")

    print("The rabbit leads you out of the forest. Congratulations, you've escaped!")
    sys.exit()

# Game intro
def intro():
    print("Welcome to the Deep Deep Forest!")
    player["name"] = input("What's your name? > ")

    print("Hello, " + player["name"] + "! You are about to enter the mysterious forest. Are you ready?")
    pcmd = input("Do you want to enter the forest? (yes or no) > ")

    if pcmd == "yes":
        enterForest()
    else:
        print("You cannot avoid your fate.")
        intro()

def main():
    intro()

main()
