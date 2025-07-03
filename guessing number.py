import random
num=random.randint(1,1000)
original_number=1234
guess=int(input("Guess the number:"))
while original_number!=guess:
    if original_number >= guess:
        print("It's wrong , too small")
    elif original_number <= guess:
        print("It's wrong , too big")
    guess=int(input("Guess the number:"))
print("congratulation!you guessed the number!")

