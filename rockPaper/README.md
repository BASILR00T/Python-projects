# Rock-Paper-Scissors Game

A Python command-line game to play Rock-Paper-Scissors against the computer with customizable rounds.

## Features
- 🎮 Best-of-N rounds (choose any number)
- 📊 Real-time win/loss/tie tracking
- 🚪 Mid-game exit with `quit`
- 🔄 Play again without restarting
- 😄 Emoji feedback system (🎉/🤝/😢)

## How to Use
1. Run the script:
   ```bash
   python Game.py

##  Full Example


Enter how many rounds you want: 2


Enter your choice (rock, paper, scissor) or type 'quit' to exit: rock


PC chose: scissor | You chose: rock

YOU Win! 🎉

Enter your choice (rock, paper, scissor) or type 'quit' to exit: quit


You chose to exit early!


Final results:
Wins: 1 | Ties: 0 | Losses: 0


Play again? (yes/no): no

Goodbye!..♥


## Customization
✏️ Edit choices = ["rock", "paper", "scissor"] to add/remove options

🎨 Modify emojis in print statements

🔢 Change default round count in code

📛 Replace "PC" with any name

##  Notes


🔄 Stats auto-reset when replaying

🔠 Case-insensitive input (ROCK = rock = Rock)

📁 No external dependencies needed
