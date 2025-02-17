import random

def GameLogic():
    choices = ["rock", "paper", "scissor"]
    rounds = 0
    WINS = 0
    LOSES = 0
    TIES = 0

    while True:
        # Get player's choice
        playerChoice = input("Enter your choice (rock, paper, scissor): ").lower()

        # Validate player's choice
        if playerChoice not in choices:
            print("Please enter a valid choice from the list [rock, paper, scissor].")
            continue  # Prompt the user again

        # Get PC's choice
        randomChoice = random.choice(choices).lower()  # Ensure case consistency
        print(f"PC's choice is: {randomChoice}, Your choice is: {playerChoice}")

        # Determine the result
        if playerChoice == randomChoice:
            rounds += 1
            TIES += 1
            print("" , 30*"-", "\nIt's a tie! 🤝\n")
        elif (playerChoice == "rock" and randomChoice == "scissor") or \
                (playerChoice == "scissor" and randomChoice == "paper") or \
                (playerChoice == "paper" and randomChoice == "rock"):
            rounds += 1
            WINS += 1
            print(30*"-", "\nYOU Win! 🎉\n")
        else:
            rounds += 1
            LOSES += 1
            print(30*"-","\nYOU Lose! 😢\n")

        # Check if 3 rounds are completed
        if rounds == 3:
            print(f"Game over! Your result:\n Wins: {WINS}\n Ties: {TIES}\n Loses: {LOSES}")
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again in ["yes", "no"]:
                    break
                print("Please enter 'yes' or 'no'.")
            if play_again == "yes":
                # Reset counters for a new game
                rounds = 0
                WINS = 0
                LOSES = 0
                TIES = 0
            else:
                print("\n""Thanks for playing! Goodbye!..♥")
                break  # Exit the game


# Start the game
GameLogic()