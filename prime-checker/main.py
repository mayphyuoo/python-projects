def prime_checker(number):
  prime = True
  if (number == 0 or number == 1):
    prime = False
  else:
    i = 2
    while (i <= int(number/2)):
      if (number % i == 0):
        prime = False
        break
      i += 1

  if (prime == True):
    print(f"{number} is a prime number.")
  else:
    print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)