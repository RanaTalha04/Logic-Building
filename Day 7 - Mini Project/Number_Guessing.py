# Mini project: Number guessing game

import random

ran_numb = random.randint(1, 100)
count = 0
flag = False

while flag == False:   
    user_guess = int(input("Guess the number between 1 and 100: "))
    count += 1

    if user_guess > ran_numb:
        print("Too high! Try again")

    elif user_guess < ran_numb:
        print("Too low! Try again")

    else:
        print(f"🎉 Correct! You guessed the nuymber in {count} attempts.")
        flag = True