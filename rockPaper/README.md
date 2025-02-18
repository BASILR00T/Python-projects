# Rock-Paper-Scissors Game

A simple Python script to play Rock-Paper-Scissors against the computer with customizable rounds.

## Features
- Play Rock-Paper-Scissors against the computer
- Choose custom number of rounds
- Track wins, losses, and ties
- Quit mid-game with `"quit"`
- Play again without restarting

## How to Use
1. Run the script `Game.py`
2. Enter your desired number of rounds
3. Play by entering `rock`/`paper`/`scissor`
4. Results update after each round
5. Type `quit` to exit early
6. View final stats and replay option

## Example
```plaintext
Enter how many rounds you want: 3  
Enter choice (rock/paper/scissor): rock  
PC chose: scissor | You chose: rock  
------------------------------  
YOU Win! 🎉  

Enter choice (rock/paper/scissor): paper  
PC chose: paper | You chose: paper  
------------------------------  
It's a tie! 🤝  

Enter choice (rock/paper/scissor): scissor  
PC chose: rock | You chose: scissor  
------------------------------  
YOU Lose! 😢  

Game Over:  
Wins: 1 | Ties: 1 | Losses: 1  
Play again? (yes/no): no  
Goodbye!..♥  
```

## Notes


🔴 Emojis: 🎉 = Win | 😢 = Loss | 🤝 = Tie

🔴 Case-insensitive inputs (ROCK = rock)

🔴 Edit Game.py to customize messages

🔴 Stats reset automatically for new games
