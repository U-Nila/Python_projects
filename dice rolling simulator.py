import random
print("\nDice rolling simulator")
while True:
    user_turn=int(input("press Enter to roll the dice: "))
    if user_turn>6:
        print("thanks for playing..see you next time")
        break
    dice_value=random.randint(1,6)
    print(f"you rolled a {dice_value}") 