from cgitb import handler
import os
from art import logo
import random


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


print(logo)

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

done = False

while done == False:

  number = random.randint(0, 100)
  # just for debugging purpose
  print(f"Pssst, the correct answer is {number}.")

  diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
  chances = 0

  if diff == "easy":
    chances = 10
  else:
    chances = 5

  guessed = False

  while chances > 0 and guessed == False:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number:
      print("Too high.\nGuess again.")
      chances -= 1
    elif guess < number:
      print("Too low.\nGuess again.")
      chances -= 1
    elif guess == number:
      print(f"You got it! The answer was {number}")
      guessed = True

  if (chances == 0 and guessed == False):
    print("You are out of guesses, You lose.")

  again = input("Do you want to play again? Type 'y' or 'n': ")
  if again == "n" or again == "no":
    done = True

  clearConsole()
