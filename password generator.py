import random
import string

print(" Welcome to Password Generator")
length = int(input("Enter password length: "))
include_uppercase = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

character_pool = ""
if include_uppercase:
    character_pool += string.ascii_uppercase 
if include_lowercase:
    character_pool += string.ascii_lowercase  
if include_digits:
    character_pool += string.digits          
if include_symbols:
    character_pool += string.punctuation      


if character_pool == "":
    print("You must choose at least one character type!")
else:
  
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print(f"Your secure password is: {password}")

  