
# Number Guessing Game 🎯

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python terminal game where players guess a secret number within a customizable range. Features score tracking, hints, and unlimited replayability!



---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features ✨
✅ **Custom Range**  
Choose any start/end numbers (e.g., `1-100` or `50-200`)  

✅ **Limited Attempts**  
5 guesses per round to keep it challenging  

✅ **Score System**  
Earn +10 points for every win (persists across games)  

✅ **Smart Hints**  
"Too high! 🔼" or "Too low! 🔽" feedback  

✅ **Input Validation**  
Handles non-integers and invalid ranges gracefully  

✅ **Replayable**  
Play infinitely without restarting  

---

## Installation ⚙️

1. **Clone the repository**  
```bash
git clone https://github.com/BASILR00T/number-guessing-game.git
cd number-guessing-game
```

2. **Run the game** (Python 3.8+ required)  
```bash
python number_guessing_game.py
```

---

## How to Play 🕹️

1. **Set your range**  
   ```
   Enter start of range: 1
   Enter end of range: 50
   ```

2. **Guess the secret number**  
   ```
   Guess (1-50): 25
   Too low! 🔽
   Attempts left: 4
   ```

3. **Win or lose**  
   - Correct guess: Earn points + replay option  
   - 5 wrong guesses: Reveal secret number  

4. **Play again?**  
   Keep your score or exit with `no`  

---

## Code Structure 🐍

```python
def gamelogic():
    # Main game loop
    while True:
        # Range selection logic
        # Secret number generation
        # Guessing mechanism
        # Win/loss handling
```

**Key Components**:
- `random.randint()`: Generates secret number  
- Nested loops: Handle game rounds + replay logic  
- Variables: `score`, `attempts`, `max_attempts`  
- Input validation: `try/except` blocks  

---

## Contributing 🤝

1. Fork the repository  
2. Create a feature branch:  
```bash
git checkout -b feature/new-feature
```
3. Commit changes & push:  
```bash
git push origin feature/new-feature
```
4. Open a pull request  

---


