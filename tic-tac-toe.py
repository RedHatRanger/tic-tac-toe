import random
from math import inf

def print_board(board):
    """
    Prints the current state of the tic-tac-toe board.
    Each cell will show 'X', 'O', or a blank space if empty.
    """
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" | ".join(cell if cell is not None else ' ' for cell in row))
        if i < 6:
            print("--+---+---")
    print()

def check_winner(board):
    """
    Checks the board for a winner.
    Returns 'X' or 'O' if there's a winner, or None if there's no winner yet.
    """
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # Horizontal lines
        (0,3,6), (1,4,7), (2,5,8),  # Vertical lines
        (0,4,8), (2,4,6)            # Diagonal lines
    ]
    for a,b,c in win_positions:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    """
    Checks if the game is a draw.
    Returns True if all cells are filled and there's no winner, otherwise False.
    """
    return all(cell is not None for cell in board) and check_winner(board) is None

def minimax(board, maximizing_player):
    """
    The minimax algorithm:
    - If maximizing_player is True, we are choosing a move for 'X'.
    - If False, we are choosing a move for 'O'.

    Returns a tuple (score, move):
    - score: the best achievable outcome from the current board state
    - move: the index where the player should move to achieve that outcome
    """
    winner = check_winner(board)
    if winner == 'X':
        return (1, None)
    elif winner == 'O':
        return (-1, None)
    elif is_draw(board):
        return (0, None)
    
    if maximizing_player:
        # Try to maximize the score for X
        best_score = -inf
        best_move = None
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                score, _ = minimax(board, False)
                board[i] = None
                if score > best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)
    else:
        # Try to minimize the score for O
        best_score = inf
        best_move = None
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                score, _ = minimax(board, True)
                board[i] = None
                if score < best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)

def get_best_move(board, player_is_x):
    """
    Wrapper for minimax to directly return just the best move.
    If player_is_x is True, we get the best move for X; otherwise for O.
    """
    _, move = minimax(board, player_is_x)
    return move

def immediate_threat(board, player):
    """
    Checks if the current player can either:
    - Win immediately (two player's marks in a line and one empty spot).
    - Or needs to block the opponent's impending win (opponent has two in a line).

    Returns the index of the cell to play if there's an immediate threat to address,
    otherwise returns None.
    """
    opponent = 'O' if player == 'X' else 'X'
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    # First, check if the player can win immediately.
    for a,b,c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count(None) == 1:
            return [a,b,c][line.index(None)]
    
    # Next, check if the opponent can win next turn and block it.
    for a,b,c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count(None) == 1:
            return [a,b,c][line.index(None)]
    
    return None

def play_game():
    # Initialize an empty board
    board = [None]*9
    turn_number = 1  # Keep track of which turn it is

    # Turn 1: X chooses a corner (index 0)
    board[0] = 'X'
    print(f"Turn {turn_number}: X chooses a corner (index 0):")
    print_board(board)
    
    # Turn 2: O makes a random first move, excluding the center (index 4)
    turn_number += 1
    first_moves = [i for i, cell in enumerate(board) if cell is None and i != 4]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"Turn {turn_number}: O randomly chooses index {o_first_move} for the first move (no center):")
    print_board(board)
    
    current_player = 'X'
    
    # Continue the game until there's a winner or a draw
    while True:
        winner = check_winner(board)
        if winner:
            print(f"The winner is: {winner}")
            break
        if is_draw(board):
            print("It's a draw.")
            break
        
        turn_number += 1

        if current_player == 'X':
            # X checks for immediate threats first
            move = immediate_threat(board, 'X')
            if move is None:
                # If no immediate threat, use minimax
                move = get_best_move(board, True)
            board[move] = 'X'
            print(f"Turn {turn_number}: X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O checks for immediate threats first
            move = immediate_threat(board, 'O')
            if move is None:
                # If no immediate threat, use minimax
                move = get_best_move(board, False)
            board[move] = 'O'
            print(f"Turn {turn_number}: O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
