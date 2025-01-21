print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.''There is island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arived at the island unharmed."
                        "There is house with three doors. One red,"
                        "One yellow and blue."
                        "Which color do you choose?\n ").lower()
        if choice3 == "red":
            print("It's is room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over")
else:
    print("You fell in to the hole. Game Over.")
