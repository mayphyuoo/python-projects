#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for n in range(nr_letters):
    rnd_index = random.randint(0, len(letters) - 1)
    password += letters[rnd_index]

for n in range(nr_symbols):
    rnd_index = random.randint(0, len(symbols) - 1)
    password += symbols[rnd_index]

for n in range(nr_numbers):
    rnd_index = random.randint(0, len(numbers) - 1)
    password += numbers[rnd_index]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

len_pw = len(password)
hard_password = ""

for n in range(len(password)):
    rnd_index = random.randint(0, (len_pw - len(hard_password)) - 1)
    hard_password += password[rnd_index]
    # password = password.replace(password[rnd_index1],"")
    password = password[0: rnd_index:] + password[rnd_index + 1::]

# or can use random.shuffle()

print(hard_password)