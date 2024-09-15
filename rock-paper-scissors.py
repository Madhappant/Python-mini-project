import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # Rock = 0 , Paper = 1 , Scissors = 2

    computer_pick = options[random_number]
    
    print("Computer picked", computer_pick + ".")

    if user_input == "Rock" and computer_pick == "Scissors":
        print("you won!")
        user_input += 1
    elif user_input == "Paper" and computer_pick == "Rock":
        print("you won!")
        user_input += 1
    elif user_input == "Scissors" and computer_pick == "Paper":
        print("you won!")
        user_input += 1
    else:
        print("you lost!")
        computer_wins += 1

print("you won", user_wins , "times")
print("The computer won", computer_wins ,"times")
print("Goodbye!")