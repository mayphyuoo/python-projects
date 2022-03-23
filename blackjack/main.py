############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Blackjack is 21
## if both dealer and player got blackjack it is a draw

import os
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def print_hands(dealer, player):
  print(f"Dealer's hands: {dealer}, sum: {sum(dealer)}")
  print(f"Player's hands: {player}, sum: {sum(player)}")


# def reset_hands(dealer_l, player_l):
#   dealer_l = []
#   player_l = []
#   return dealer_l, player_l

# 0 : player stopped the game
# -1 : natural dealer
# 1 : natural player
# 3 : player got busted
# 4 : player won
# 5 : dealer won
# 6 : draw


def normal_game(dealer, player):
  code = -2

  while (sum(dealer) < 17):
    dealer.append(random.choice(cards))

  if sum(dealer) > 21:
    code = 4
    print_hands(dealer, player)
    print("Dealer got busted.")
  elif sum(dealer) > sum(player):
    print_hands(dealer, player)
    code = 5
  elif sum(player) > sum(dealer):
    print_hands(dealer, player)
    code = 4
  elif sum(dealer) == sum(player):
    print_hands(dealer, player)
    code = 6

  return code, dealer


def play():

  dealer_hand = []
  player_hand = []

  # first 2 cards for both dealer and player
  for c in range(2):
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))

  if (player_hand[0] == 11 and player_hand[1] == 11):
    player_hand[1] = 1

  if (dealer_hand[0] == 11 and dealer_hand[1] == 11):
    dealer_hand[1] = 1

  if sum(dealer_hand) == 21:
    print_hands(dealer_hand, player_hand)
    # dealer_hand, player_hand = reset_hands(dealer_hand, player_hand)
    return -1
  elif sum(player_hand) == 21:
    print_hands(dealer_hand, player_hand)
    # dealer_hand, player_hand = reset_hands(dealer_hand, player_hand)
    return 1

  done = False
  while (done == False):
    clearConsole()
    print(f"Dealer's first card: {dealer_hand[0]}")
    print(f"Player's hands: {player_hand} , sum: {sum(player_hand)}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == 'n':
      done = True
      norm, dealer_hand = normal_game(dealer_hand, player_hand)
      return norm
    else:
      player_hand.append(random.choice(cards))
      if (sum(player_hand) > 21 and player_hand[len(player_hand)-1] == 11):
        player_hand[len(player_hand)-1] = 1

      if (sum(player_hand) > 21):
        done = True
        print_hands(dealer_hand, player_hand)
        # dealer_hand, player_hand = reset_hands(dealer_hand, player_hand)
        return 3
      elif (sum(player_hand) == 21):
        done = True
        print_hands(dealer_hand, player_hand)
        return 1


def deciding_func(argument):
    switcher = {
        0: "Sad to see you go. Come back anytime. ♥️ ♦ ♠️ ♣️",
        -1: "Dealer wins with a Blackjack! 😔",
        1: "Win with a Blackjack 😎",
        3: "You lose. You got busted.",
        4: "You won!",
        5: "Dealer won! You lose.",
        6: "It is a draw."
    }

    return switcher.get(argument, "Error")


print(logo)

game_continue = True

while game_continue:

  want_to_play = input(
      "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  
  if want_to_play == 'n':
     game_continue = False
  else:
    clearConsole()
    result = play()
    print(deciding_func(result))
