from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# definition of caesar encryption/ decryption
def caesar(text, shift, direction):
  result = ""
  shift = shift % 26
  type = ""
  if (direction == "decode"):
      shift *= -1
      type = "decoded"
  else:
    type = "encoded"

  for letter in text:
    if letter in alphabet:
      i = alphabet.index(letter) + shift
      i = i % 26
      result += f"{alphabet[i]}"
    else:
      result += letter

  print(f"The {type} text is '{result}'")


# the start of program
print(logo)

loop = True

while (loop):
  # ask for inputs
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # call caesar function
  caesar(text, shift, direction)

  again = input(
      "Type 'yes or y' if you want to go again. Otherwise type anything:\n")

  if again == 'yes' or again == 'y':
    loop = True
  else:
    loop = False
    print("Good Bye!")
