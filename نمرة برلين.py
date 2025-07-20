import time
import sys
import random

print("Welcome to Berline Tag:")
time.sleep(1)
tag_question = input("Do you want to make your Tag?\n").upper()

if tag_question == "NO":
    print("finished")
    sys.exit()

elif tag_question == "YES":
    # English letters
    words = ["A","B","C","D","E","F","G","H","I",
             "J","K","L","M","N","O","P","Q","R","S","T","U",
             "V","W","X","Y","Z"]
    # English numbers
    numbers = ["1","2","3","4","5","6","7","8","9"]

    # Generate parts
    rm1_w = "B"
    rm2_w = random.choice(words)
    rm3_w = random.choice(words)

    rm1_n = random.choice(numbers)
    rm2_n = random.choice(numbers)
    rm3_n = random.choice(numbers)
    rm4_n = random.choice(numbers)

    rm_words = rm1_w + " " + rm2_w + rm3_w
    rm_numbers = rm1_n + rm2_n + rm3_n + rm4_n

    all_rm = rm_words + "//" + rm_numbers

    # Save generated tags
    random_all = []

    if all_rm not in random_all:
        random_all.append(all_rm)
        print("Generated Tag:", all_rm)
    else:
        print("We are sorry, a problem happened. Try again please.")

else:
    print("Please try again")