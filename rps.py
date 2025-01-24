import random

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
game_images = [rock, paper, scissors]

user_input = int(input("What do you choose to play? (0 is for rock,1 is for paper and 2 is for scissors) "))
if user_input >= 0 and user_input <= 2:
    print("You chose: ")
    print(game_images[user_input])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0:
    print("You entered an invalid input. You lose!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose!")
elif user_input > computer_choice:
    print("You win!")
elif computer_choice > user_input:
    print("You lose!")
elif computer_choice == user_input:
    print("It's a draw!")