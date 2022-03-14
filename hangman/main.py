import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}. Just for testing purposes.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

lives = 6

while ('_' in display) and lives != 0:
    guessed = False
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed {guess}.")
    else:
      #Check guessed letter
      for position in range(word_length):

          if chosen_word[position] == guess:
              display[position] = chosen_word[position]
              guessed = True

      if guessed == False:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if (lives == 0):
      print("You lose.")
    print(stages[lives])
