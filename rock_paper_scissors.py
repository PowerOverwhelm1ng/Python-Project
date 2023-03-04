#import random for rps
import random
#count wins 

computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]
#           0           1       2

#create a while loop to check if user or comp wins

while True:
    user_input = input("Type Rock/Paper/Scissors to throw down or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    #rock : 0, paper: 1 scissor: 2

    computer_pick = options[random_number]
    print("Sensei Picked ", computer_pick +str(" ! "))

if user_input == "rock" and computer_pick == "scissors":
    print("Congratulations Warrior! Youve won!")
    user_wins += 1

elif user_input == "paper" and computer_pick == "rock":
        print("Congratulations Warrior! Youve won!")
        user_wins += 1

elif user_input == "scissors" and computer_pick == "paper":
    print("Congratulations Warrior! Youve won!")
    user_wins += 1

else:
    print("Victory is mine today Warrior!")
    computer_wins += 1

    print("The challenger won ," + user_wins + "times")
    print("The sensei won" + computer_wins + "times!")

    print("Until next time Warrior!")