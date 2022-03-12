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

#Write your code below this line 👇

import random


choices = [rock, paper, scissors]
invalid = False

print("Lets play rock paper scissors!")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
try:
  print(choices[player_choice])
except:
  print("You entered invalid number. Try again... 😐")
  invalid = True
  
# if (player_choice != computer_choice):
#   if (player_choice == 0 and computer_choice == 1):
#     print("You lose")
#   elif (player_choice == 0 and computer_choice == 2):
#     print("You win")
#   elif (player_choice == 1 and computer_choice == 0):
#     print("You win")
#   elif (player_choice == 1 and computer_choice == 2):
#     print("You lose")
#   elif (player_choice == 2 and computer_choice == 0):
#     print("You lose")
#   elif (player_choice == 2 and computer_choice == 1):
#     print("You win")
    
# else:
#   print("It is a draw.")

computer_choice = random.randint(0, 2)

if (invalid == False):
  
  print("Computer chose:\n" + choices[computer_choice])
  
  if (player_choice == 0 and computer_choice == 2):
    print("You win!")
  elif (player_choice == 2 and computer_choice == 0):
     print("You lose.")
  elif ( player_choice == computer_choice ):
    print("It is a draw.")
  else:
    if ( player_choice > computer_choice ):
      print("You win!")
    elif ( player_choice < computer_choice ):
      print("You lose.")