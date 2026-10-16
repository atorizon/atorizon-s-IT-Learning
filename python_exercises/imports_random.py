import random
import time
# random_int=random.randint(1,100)
# user_int=int(input("Guess the computer's number: "))

# while user_int != random_int:
#     if user_int > random_int:
#         print("Lower...")
#         user_int=int(input("Guess the computer's number: "))
#     else:
#         print("Higher...")
#         user_int=int(input("Guess the computer's number: "))

# print(f"Yes! You guessed it! The computer's number was {random_int}!")

comp_score=0
user_score=0

def choice():
    user_choice=input("What do you choose?: ")
    return user_choice.upper()

while True:
    if comp_score == 5 or user_score==5:
        if comp_score == 5:
            print("Computer wins!")
            break
        elif user_score==5:
            print("User wins!")
            break
    else:
        comp_choice=random.choice(["ROCK","PAPER","SCISSORS"])
        print("===== ROCK PAPER SCISSORS GAME! =====")
        user_choice=choice()
        print("Rock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoo!\n")
        time.sleep(0.5)
        print(f"User's Choice: {user_choice} | Computer's Choice: {comp_choice}")
        match comp_choice:
            case "ROCK":
                if user_choice == "ROCK":
                    print("Neutral.")
                elif user_choice == "PAPER":
                    print("User wins.")
                    user_score+=1
                elif user_choice == "SCISSORS":
                    print("Computer wins.")
                    comp_score+=1
            case "SCISSORS":
                if user_choice == "ROCK":
                    print("User wins.")
                    user_score+=1
                elif user_choice == "PAPER":
                    print("Computer wins.")
                    comp_score+=1
                elif user_choice == "SCISSORS":
                    print("Neutral.")
            case "PAPER":
                if user_choice == "ROCK":
                    print("Computer wins.")
                    comp_score+=1
                elif user_choice == "PAPER":
                    print("Neutral.")
                elif user_choice == "SCISSORS":
                    print("User wins.")
                    user_score+=1
        print(f"Current Score - User({user_score}) | Computer({comp_score})\n")
