from game_data import data
from art import logo, vs
import random
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

# return 0 if pair1 >= pair2 else return 1


def calculateAnswer(pair1, pair2, guess, score):
  if pair1['follower_count'] >= pair2['follower_count']:
    if guess == "A" or guess == "a":
      score += 1
      return True, score
    else:
      return False, score
  else:
    if guess == "A" or guess == "a":
      return False, score
    else:
      score += 1
      return True, score


# main starts here
# first random pair
pair = random.sample(data, 2)

gameContinue = True
score = 0

while gameContinue:
  clearConsole()
  print(logo)

  if score > 0:
    print(f"You're right! Current score: {score}")

    # refresh the pair
    prev = pair[0]
    pair[0] = pair[1]
    pair[1] = random.choice(data)
    while pair[1]['name'] == pair[0]['name'] and pair[1]['name'] == prev['name']:
      pair[1] = random.choice(data)

  print(
      f"Compare A: {pair[0]['name']}, {pair[0]['description']}, from {pair[0]['country']}.")

  print(vs)

  print(
      f"Against B: {pair[1]['name']}, {pair[1]['description']}, from {pair[0]['country']}.")

  guess = input("Who has more followers? Type 'A' or 'B' (default B): ")

  gameContinue, score = calculateAnswer(pair[0], pair[1], guess, score)

clearConsole()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
