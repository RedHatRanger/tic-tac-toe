# Tic-Tac-Toe Game Model

This project implements a fully automated tic-tac-toe match between two players, **X** and **O**, each making moves under certain strategic conditions. It simulates various known optimal and suboptimal strategies, while also allowing for scenario-specific rules, such as:

- X always starts in a corner.
- O’s first move cannot be the center (if desired).
- Both players attempt to win or block immediate threats before resorting to a minimax-based decision model.
- Moves and outcomes are displayed with turn-by-turn updates, including the move number and chosen index.

## How to Win at Tic-Tac-Toe 100% of the Time (if You Are X)

In standard tic-tac-toe, if both players play perfectly and O takes the center in response to X’s corner start, the game will end in a draw. However, if O fails to take the center on the first move, X can force a guaranteed win by following these steps:

1. **X starts in a corner:**  
   By choosing a corner first, X creates multiple potential winning paths.

2. **O neglects the center:**  
   If O doesn’t occupy the center initially, O surrenders a critical positional advantage.

3. **Optimal strategy (immediate threats + minimax):**  
   With immediate threat detection to secure quick wins or blocks, combined with the minimax algorithm to ensure long-term success, X can set up forks and leave O defenseless.

Under these conditions, X will achieve a 100% win rate with perfect play.

## Playing Board Layout

Below is the layout of the board with the index of each cell. These indices are used in the program output to indicate where each move is played:

```
0 | 1 | 2
--+---+---
3 | 4 | 5
--+---+---
6 | 7 | 8
```

Where:
- Index 0 is the top-left corner.
- Index 4 is the center.
- Index 8 is the bottom-right corner.

## Features

### Minimax Algorithm
The core logic uses minimax to ensure that if there is a forced win or inevitable draw, the algorithm will find it, giving both players optimal or near-optimal strategies.

### Immediate Threat Detection
Before running minimax, each player:
- Attempts an immediate win if possible.
- Blocks the opponent if the opponent is about to win on their next turn.

This ensures no obvious tactical opportunities are missed.

### Custom Opening Scenarios
The model can prohibit O from taking the center on the first move, reflecting a suboptimal start that X can exploit to guarantee victory.

### Turn-by-Turn Logging
Each move is printed with its turn number, the player who moved, the index chosen, and the updated board state. This transparency helps you follow the game’s progression step-by-step.

### Consistent Outcomes
By controlling when O can pick the center and by using predefined heuristics, this model can demonstrate known theoretical outcomes, including scenarios where X always wins given O’s suboptimal play.

## How It Works

**Initial Move:**  
X always takes a corner (e.g., index 0).

**O’s First Move (Configurable):**  
By default, O may pick any available square except the center. This simulates a suboptimal start and allows X to eventually force a win. If you re-enable O’s ability to choose the center, perfect play by both sides results in a draw.

**Subsequent Moves:**
- Each turn is printed as: *"Turn n: X plays at index i"* or *"Turn n: O plays at index j"*.
- Immediate wins or blocks are chosen first.
- If no immediate threat exists, minimax determines the best next move.

**Game Conclusion:**
- The game ends when one player forms a line of three identical marks.
- If the board fills with no winner, the result is a draw.

## Installation and Running

**Prerequisites:**
- Python 3.x installed.
- No additional libraries are required.

**Clone or Download:**
- Clone this repository or download `tic-tac-toe.py` to your local machine.
- cd into that directory and run the game.

**Run the Game:**
```bash
python tic-tac-toe.py
```
