# Tic-Tac-Toe Game Model
This project implements a fully automated tic-tac-toe match between two players, X and O, each making moves under certain strategic conditions. It simulates various known optimal and suboptimal strategies, while also allowing for scenario-specific rules, such as:
- X always starts in a corner.
- O’s first move cannot be the center (if desired).
- Both players attempt to win or block immediate threats before resorting to a minimax-based decision model.
- Moves and outcomes are displayed with turn-by-turn updates, including the move number and chosen index.

## Features
Minimax Algorithm:
- The core logic for choosing the best moves is based on the minimax algorithm, a classical decision-making approach used in turn-based games. Minimax ensures that if there is a winning strategy or a forced draw available, the algorithm will find it.

### Immediate Threat Detection:
- Before making a decision via minimax, both players check if there is an opportunity to:
  - Win immediately (if they have two of their marks in a line and the third cell is empty).
  - Block the opponent’s imminent win (if the opponent has two marks in a line and an empty cell that could complete a win).
  - By doing so, the game mimics more "human-like" strategic play, ensuring that obvious tactical moves are never overlooked.

### Custom Opening Scenarios:
- The game can be configured so that O cannot pick the center at the start. This scenario tests the well-known tic-tac-toe principle that if O does not take the center in response to X’s corner start, X can force a win.

### Turn-by-Turn Logging:
- After each move, the turn number is displayed, along with a printed board state. This makes it easy to follow the game’s progression, understanding who played where and when.

### Consistent Outcomes:
- By removing randomness (or controlling it), and enforcing certain heuristics, this model can demonstrate known strategic outcomes, such as guaranteeing an X win if O fails to respond optimally at the start.


## How It Works:
### Initial Move:
- X always takes a corner on the first move (e.g., index 0).

### O’s First Move (Configurable):
- By default, O may pick a random available space, excluding the center if desired. This simulates a suboptimal response scenario that X can exploit.

### Subsequent Moves:
- Each turn is printed: "Turn n: X plays at index i" or "Turn n: O plays at index j".
- Both players first attempt any immediate winning or blocking moves.
- If no immediate threat is found, minimax is used to determine the best possible move considering the entire future game tree.

### Game Conclusion:
- The game ends when:
  - A player achieves three in a row (X or O wins).
  - The board is full without a winner (draw).

Installation and Running
Prerequisites:

Python 3.x installed on your system.
No additional libraries are required for the basic model.
Clone or Download:
Clone this repository or download the tic-tac-toe.py file to your local machine.

Run the Game:
In your terminal or command prompt, navigate to the directory where tic-tac-toe.py is located and run:

bash
Copy code
python tic-tac-toe.py
Observe the Output: The script will print each move as it is made, showing the board state and the turn number. Follow along in the terminal as the game progresses.

Customization
Adjusting O’s First Move Behavior:
To test different scenarios, you can modify the code that picks O’s initial move. Allowing O to pick the center leads to a known draw scenario with perfect play, while preventing O from picking the center shows how X can force a win.

Changing Heuristics and Randomness:
You can remove or add randomness to the best-move selection when multiple equally good moves exist. Adjusting this behavior can demonstrate different possible sequences within optimal or near-optimal play.

Additional Logging or Analysis:
Add print statements or logging for deeper analysis. For example, track how often X wins under certain conditions or how quickly the game converges to a known outcome.

Known Strategic Outcomes
X Starts in a Corner and O Responds Suboptimally:
If O does not take the center initially, X can eventually force a win by following optimal strategy and setting up forks, as the model demonstrates.

Perfect Play by Both Players:
If both X and O play perfectly from the start (with O taking the center in response to X’s corner), the game will always end in a draw.

Contributing
Feel free to open issues, suggest improvements, or create pull requests. Whether it’s optimizing minimax, refining heuristics, or enhancing the readability of output, your contributions are welcome.

License
This project is released under the GPLv3 Free License. You are free to use, modify, and distribute it as permitted by the terms of the license.
