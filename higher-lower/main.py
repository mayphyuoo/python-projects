from game_data import data
from art import logo, vs
import random
import os


def clearConsole():
    """clear out console terminal"""
    return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


# return 0 if pair1 >= pair2 else return 1
def calculateAnswer(pair1, pair2, guess, score):
    """Checks followers against user's guess
  and returns True and add 1 to score if they got it right.
  Or False if they got it wrong."""

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


def printData(celeb):
    """input: pair, return fstring: celeb's name, description and country"""
    # print(f'{celeb['name']}: {celeb["follower_count"]}')
    return f" {celeb['name']}, a {celeb['description']}, from {celeb['country']}."

# main starts here
# first random pair
pair = random.sample(data, 2)

gameContinue = True
score = 0

# start game
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

    print("Compare A:" + printData(pair[0]))

    print(vs)

    print("Against B:" + printData(pair[1]))

    guess = input("Who has more followers? Type 'A' or 'B' (default B): ")

    gameContinue, score = calculateAnswer(pair[0], pair[1], guess, score)

# out of while loop
# end of game
clearConsole()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
