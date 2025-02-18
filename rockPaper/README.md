# Rock-Paper-Scissors Game

A simple command-line Rock-Paper-Scissors game where you play against the computer.

## Features
- Play Rock-Paper-Scissors against the computer.
- Choose the number of rounds you want to play.
- Track wins, losses, and ties over the selected number of rounds.
- Option to quit early by typing `"quit"`.
- Option to play again after the game ends.

## How to Use
1. Run the script `Game.py`.
2. Enter the number of rounds you want to play.
3. Enter your choice (`rock`, `paper`, or `scissor`) when prompted.
   - Type `"quit"` to exit early and see your results.
4. The computer will randomly select its choice.
5. The result (win, lose, or tie) will be displayed.
6. After the selected number of rounds, the game will display your total wins, losses, and ties.
7. You can choose to play again or exit the game.

## Example

Enter how many rounds you want to play: 2
Enter your choice (rock, paper, scissor) or type 'quit' to exit: rock
PC's choice is: scissor, Your choice is: rock
------------------------------ 
YOU Win! 🎉

Enter your choice (rock, paper, scissor) or type 'quit' to exit: paper
PC's choice is: rock, Your choice is: paper
------------------------------ 
YOU Lose! 😢

Game over! Your result:
 Wins: 1
 Ties: 0
 Losses: 1
What we call this Tie? 🤔
Do you want to play again? (yes/no): no
Thanks for playing! Goodbye!..♥

## Notes
- The game uses emojis (`🎉`, `😢`, `🤝`, `🤔`) to make the results more fun.
- You can customize the number of rounds at the start of the game or when playing again.
- If you type `"quit"`, the game will end early and display your current results.
- The game resets after each session, and you can choose to play again or exit.
