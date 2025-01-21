# import random

# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("Head")
# else:
#     print("Tail")


import random

# Define the game images for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of game images

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 Scissors "))

if user_choice >= 0 and user_choice <=2:
    print("You choose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer choose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It is draw!")
    elif (user_choice == 0 and computer_choice ==2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("You typed an 0invalid number. YOu lose!")

