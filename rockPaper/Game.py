import random

def game_logic():
    choices = ["rock", "paper", "scissor"]
    rounds = 0
    wins = 0
    loses = 0
    ties = 0

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
        player_choice = input("Enter your choice (rock, paper, scissor) or type 'quit' to exit: ").lower()

        # Check if the player wants to quit early
        if player_choice == "quit":
            print("You chose to quit early. Here are your results:")
            print(f"wins: {wins}\n ties: {ties}\n loses: {loses}")
            # Determine overall result
            if wins > loses and wins > ties:
                print("We Have a Winner! 🎉")
            elif ties >= wins and ties >= loses or wins == loses:
                print("What we call this Tie? 🤔")
            else:
                print("You've Lost 😢")

            print("\nThanks for playing! Goodbye!..♥")
            break
        elif player_choice not in choices:
            print("Please enter a valid choice from the list [rock, paper, scissor].")
            continue  # Prompt the user again

        # Get PC's choice
        random_choice = random.choice(choices).lower()  # Ensure case consistency
        print(f"PC's choice is: {random_choice}, Your choice is: {player_choice}")

        # Determine the result
        if player_choice == random_choice:
            rounds += 1
            ties += 1
            print("", 30 * "-", "\nIt's a tie! 🤝\n")
        elif (player_choice == "rock" and random_choice == "scissor") or \
                (player_choice == "scissor" and random_choice == "paper") or \
                (player_choice == "paper" and random_choice == "rock"):
            rounds += 1
            wins += 1
            print(30 * "-", "\nYOU Win! 🎉\n")
        else:
            rounds += 1
            loses += 1
            print(30 * "-", "\nYOU Lose! 😢\n")

        # Check if the selected number of rounds is completed
        if rounds == total_rounds:
            print(f"Game over! Your result:\n wins: {wins}\n ties: {ties}\n loses: {loses}")
            # Determine overall result
            if wins > loses and wins > ties:
                print("We Have a Winner! 🎉")
            elif ties >= wins and ties >= loses or wins == loses:
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
                wins = 0
                loses = 0
                ties = 0

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
game_logic()
