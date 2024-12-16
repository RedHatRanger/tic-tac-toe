# Tic-Tac-Toe
This is a tic-tac-toe python script to show the ideal outcome of a given set with X starting in its optimal move, the CORNER.


## What this code does:
- Each move prints the turn number and shows who played and where.
- Before deciding on a move with minimax, both X and O check for immediate threats (either to win or to block).
- If a threat is found, they immediately take that move.
- If no threat is found, they revert to the minimax strategy to pick the best possible move.


The exact count of how many ways X can win, O can win, or the game can end in a draw in tic-tac-toe (assuming all possible sequences of moves by both players, without any additional restrictions) is well known from exhaustive computer analysis. These numbers assume each unique sequence of moves (rather than just distinct final board states) is counted separately, and that both players may make any legal moves (not necessarily optimal):
- Total possible games: 255,168
- X wins: 131,184 games
- O wins: 77,904 games
- Draws (ties): 46,080 games
These figures come from enumerations of all possible move sequences. Note that any constraints or additional rules (such as forcing O to avoid the center on the first move, or requiring immediate blocking moves) would alter these numbers. The numbers above are the classical, standard results for unrestricted tic-tac-toe.
