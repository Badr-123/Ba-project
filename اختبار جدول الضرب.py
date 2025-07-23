import random
import time
import sys

score = 0  # لازم يكون برا اللوب علشان يتجمع

while True:
    num_1 = random.choice(range(13)) 
    num_2 = random.choice(range(13)) 

    user_choice = int(input(f"{num_1} × {num_2} = "))      
    equal_num = num_1 * num_2

    if user_choice == equal_num:
        print("🎉 Congratulations! You won")
        score += 1
        print(f"✅ Your score: {score}")
    else:
        print("❌ Wrong answer")
        print(f"✅ Your score: {score}")

    again = input("Do you want to try again? (yes/no): ").lower()

    if again == "yes":
        continue
    elif again == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        break