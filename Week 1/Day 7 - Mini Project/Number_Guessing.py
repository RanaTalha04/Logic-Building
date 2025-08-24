# Mini project: Number guessing game

import random

ran_numb = random.randint(1, 100)
count = 0
limit = 5

while limit > 0:   
    user_guess = int(input("Guess the number between 1 and 100: "))
    count += 1
    
    if user_guess > ran_numb:
        print("Too high! Try again")
        limit -= 1

    elif user_guess < ran_numb:
        print("Too low! Try again")
        limit -= 1

    else:
        print(f"🎉 Correct! You guessed the number in {count} attempts. Your remaining attempts {limit}.")
        break
    
    
if limit == 0:
        print(f"😢 Game Over! The correct number was {ran_numb}.")