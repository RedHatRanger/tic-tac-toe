import random
from math import inf

def print_board(board):
    """Prints the board in a human-readable format."""
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" | ".join(cell if cell is not None else ' ' for cell in row))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board):
    """Check for a winner. Returns 'X', 'O', or None if no winner."""
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    for a,b,c in win_positions:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    """Check if the board is full and there is no winner."""
    return all(cell is not None for cell in board) and check_winner(board) is None

def minimax(board, maximizing_player):
    """
    Modified minimax algorithm:
    Returns (best_score, [list_of_moves_that_achieve_that_score])
    """
    winner = check_winner(board)
    if winner == 'X':
        return (1, [])
    elif winner == 'O':
        return (-1, [])
    elif is_draw(board):
        return (0, [])
    
    if maximizing_player:
        best_score = -inf
        best_moves = []
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                score, _ = minimax(board, False)
                board[i] = None
                if score > best_score:
                    best_score = score
                    best_moves = [i]
                elif score == best_score:
                    best_moves.append(i)
        return (best_score, best_moves)
    else:
        best_score = inf
        best_moves = []
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                score, _ = minimax(board, True)
                board[i] = None
                if score < best_score:
                    best_score = score
                    best_moves = [i]
                elif score == best_score:
                    best_moves.append(i)
        return (best_score, best_moves)

def play_game():
    # Start with an empty board
    board = [None]*9
    
    # X starts in a corner (index 0 for demonstration)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    current_player = 'O'  # O moves next
    
    # For O’s first move, choose randomly from all available squares
    # rather than using minimax.
    first_moves = [i for i, cell in enumerate(board) if cell is None]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"O randomly chooses index {o_first_move} for the first move:")
    print_board(board)
    current_player = 'X'  # Now back to X

    # From now on, use minimax with random selection among best moves.
    while True:
        winner = check_winner(board)
        if winner:
            print(f"The winner is: {winner}")
            break
        if is_draw(board):
            print("It's a draw.")
            break
        
        if current_player == 'X':
            # X tries to maximize the score
            _, best_moves = minimax(board, True)
            move = random.choice(best_moves)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O tries to minimize the score (from X's perspective)
            _, best_moves = minimax(board, False)
            move = random.choice(best_moves)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
