import random

def GameLogic():
    choices = ["rock", "paper", "scissor"]
    rounds = 0
    WINS = 0
    LOSES = 0
    TIES = 0

    # Get the number of rounds from the player
    while True:
        try:
            total_rounds = int(input("Enter how many rounds you want to play: ").lower())
            if total_rounds > 0:
                break
            else:
                print("Please enter a positive number of rounds.")
        except ValueError:
            print("Please enter a valid number.")

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
            print("", 30 * "-", "\nIt's a tie! 🤝\n")
        elif (playerChoice == "rock" and randomChoice == "scissor") or \
                (playerChoice == "scissor" and randomChoice == "paper") or \
                (playerChoice == "paper" and randomChoice == "rock"):
            rounds += 1
            WINS += 1
            print(30 * "-", "\nYOU Win! 🎉\n")
        else:
            rounds += 1
            LOSES += 1
            print(30 * "-", "\nYOU Lose! 😢\n")

        # Check if the selected number of rounds is completed
        if rounds == total_rounds:
            print(f"Game over! Your result:\n Wins: {WINS}\n Ties: {TIES}\n Loses: {LOSES}")

            # Determine overall result
            if WINS > LOSES and WINS > TIES:
                print("We Have a Winner! 🎉")
            elif TIES >= WINS and TIES >= LOSES:
                print("What we call this Tie? 🤔")
            else:
                print("You've Lost 😢")

            # Ask if the player wants to play again
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

                # Get the number of rounds for the new game
                while True:
                    try:
                        total_rounds = int(input("Enter how many rounds you want to play: ").lower())
                        if total_rounds > 0:
                            break
                        else:
                            print("Please enter a positive number of rounds.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("\nThanks for playing! Goodbye!..♥")
                break  # Exit the game


# Start the game
GameLogic()
