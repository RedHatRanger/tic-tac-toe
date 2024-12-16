# Tic-Tac-Toe Game Model

This project implements a fully automated tic-tac-toe match between two players, **X** and **O**, each making moves under certain strategic conditions. It simulates various known optimal and suboptimal strategies, while also allowing for scenario-specific rules, such as:

- X always starts in a corner.
- O’s first move cannot be the center (if desired).
- Both players attempt to win or block immediate threats before resorting to a minimax-based decision model.
- Moves and outcomes are displayed with turn-by-turn updates, including the move number and chosen index.

## How to Win at Tic-Tac-Toe 100% of the Time (if You Are X)

In standard tic-tac-toe, if both players play perfectly and O takes the center in response to X’s corner start, the game will end in a draw. However, if O fails to take the center on the first move, X can force a guaranteed win by following these steps:

1. **X starts in a corner:**  
   By choosing a corner first, X creates multiple potential winning avenues.
   
2. **O neglects the center:**  
   If O does not occupy the center initially, O loses a critical positional advantage.
   
3. **Follow the optimal strategy:**  
   With immediate threat detection (win/block) and minimax-based decision-making, X can set up forks and force O into a losing position.

Under these conditions—X starting in a corner and O not taking the center—X will achieve a 100% win rate with perfect play.

## Features

### Minimax Algorithm
The core logic for move selection uses the minimax algorithm, a well-known decision-making approach in turn-based games. If there is a forced win or a guaranteed draw outcome, minimax will find it.

### Immediate Threat Detection
Before running minimax, both players check for:
- **Winning Moves:** If they have two in a row and an empty space, they secure the win immediately.
- **Blocking Moves:** If the opponent is one move away from winning, they block it at once.

This ensures that obvious tactical moves are never missed.

### Custom Opening Scenarios
The model can be configured so that O does not pick the center on the first move, testing the principle that O’s suboptimal response allows X to force a victory.

### Turn-by-Turn Logging
Each move is printed with a turn number and the resulting board state, making it easy to follow the game’s progress.

### Consistent Outcomes
By controlling randomness and using heuristics, this model can demonstrate well-known outcomes. For example, if O doesn’t take the center at the start, X can always force a win.

## How It Works

**Initial Move:**  
X always takes a corner (e.g., index 0).

**O’s First Move (Configurable):**  
By default, O may pick any available square except the center, simulating a suboptimal start. If you allow O to pick the center, the game should end in a draw with perfect play.

**Subsequent Moves:**
- Each turn is printed as: *"Turn n: X plays at index i"* or *"Turn n: O plays at index j"*
- Immediate wins or blocks are attempted first.
- If no immediate threat exists, minimax determines the best strategic move.

**Game Conclusion:**
- The game ends when one player gets three in a row.
- If the board fills up without a winner, the game is a draw.

## Installation and Running

**Prerequisites:**
- Python 3.x installed.
- No additional libraries required.

**Clone or Download:**
- Clone this repository or download `tic-tac-toe.py`.

**Run the Game:**
```bash
python tic-tac-toe.py
