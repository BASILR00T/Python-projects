import random

def gamelogic():
    print("Welcome to the Number Guessing Game! 🎯\n")
    score = 0

    while True:  # Main game loop
        # Difficulty setup
        while True:
            try:
                num1 = int(input("Enter start of range: "))
                num2 = int(input("Enter end of range: "))
                if num1 >= num2:
                    print("⚠ Error: End must be > Start!")
                else:
                    break
            except ValueError:
                print("Invalid input. Use integers.")


        secret_number = random.randint(num1, num2)
        max_attempts = 5
        attempts = 0
        game_won = False

        # Single round
        while attempts < max_attempts and not game_won:
            try:
                guess = int(input(f"Guess ({num1}-{num2}): "))
                attempts += 1

                if guess == secret_number:
                    score += 10
                    game_won = True
                    print(f"🎉 Correct! You won in {attempts} attempts!")
                    print(f"Score: {score}")
                elif guess < secret_number:
                    print("Too low! 🔽")
                else:
                    print("Too high! 🔼")

                print(f"Attempts left: {max_attempts - attempts}\n")

            except ValueError:
                print("Please enter a valid number.\n")

        # Game over actions
        if not game_won:
            print(f"❌ Game over! The number was {secret_number}.")

        # Play again with full reset
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing! Final score: {score}")
            break

# Start the game
gamelogic()