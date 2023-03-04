import random
while True:
    user_action = input("Choose your weapon Warrior! (Rock?, Paper, Scissors)!")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, Sensei chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Master and student both threw {user_action}. Its a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("ROCK SMASHES SCISSORS!, The student wins!")

        else:
            print("PAPER COVERS ROCK! The master wins!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("PAPER COVERS ROCK! The master wins!")
        else:
            print("SCISSORS CUT PAPER! The student loses!")
    elif user_action == 'scissors':
        if computer_action == "paper":
            print("SCISSORS CUT! The student wins!")
        else:
            print("ROCK SMASHES SCISSORS! The master wins!")
play_again = input("Play again? (y,n): ")
if play_again.lower() != 'y':
        break

