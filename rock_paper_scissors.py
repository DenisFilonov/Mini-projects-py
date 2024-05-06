import random as ran


def get_user_choice():
    while True:
        user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()
        if user_input == "q":
            return None
        elif user_input in ("rock", "paper", "scissors"):
            return user_input
        else:
            print("Invalid input, please try again.")


def determine_winner(user_choice, computer_choice):
    outcomes = {
        "rock":
        {
            "rock": "tie",
            "paper": "lose",
            "scissors": "win"
        },

        "paper":
        {
            "rock": "win",
            "paper": "tie",
            "scissors": "lose"
        },

        "scissors":
        {
            "rock": "lose",
            "paper": "win",
            "scissors": "tie"
        }
    }
    return outcomes[user_choice][computer_choice]


def play_game():
    user_score = 0
    computer_score = 0
    ties = 0
    options = ("rock", "paper", "scissors")

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            break

        computer_choice = ran.choice(options)
        print(f"Computer picked: '{computer_choice}'")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("You won!\n")
            user_score += 1
        elif result == "lose":
            print("Computer won!\n")
            computer_score += 1
        else:
            print("Tie, restart\n")
            ties += 1

    if user_score != 0 or computer_score != 0 or ties != 0:
        print(f"\nResults:\nUser Score: {user_score}\nComputer Score: {computer_score}\nTies: {ties}\n")
    print("Thanks for playing!")


# Get started from here
play_game()
