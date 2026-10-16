import random

random_int=random.randint(1,100)
user_int=int(input("Guess the computer's number: "))

while user_int != random_int:
    if user_int > random_int:
        print("Lower...")
        user_int=int(input("Guess the computer's number: "))
    else:
        print("Higher...")
        user_int=int(input("Guess the computer's number: "))

print(f"Yes! You guessed it! The computer's number was {random_int}!")