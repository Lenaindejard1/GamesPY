import random
from colorama import init, Fore

from Games.Rami import JeuDeRami


def play_game():
    init(autoreset=True)
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_input = input("Enter 1 for rock, 2 for paper, 3 for scissors or 0 to quit: ")
        if user_input == "0":
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break
        if user_input not in ["1", "2", "3"]:
            print("Invalid input. Please enter 1, 2, 3, or 0.")
            continue

        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(Fore.YELLOW + "It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print(Fore.GREEN + "You win!")
            user_score += 1
        else:
            print(Fore.RED + "You lose!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        replay = input("Do you want to play again? (yes/no): ").lower()
        print('---------------------------------------------')
        if replay != "yes":
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break