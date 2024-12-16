import random
from math import inf

def print_board(board):
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" | ".join(cell if cell is not None else ' ' for cell in row))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board):
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
    return all(cell is not None for cell in board) and check_winner(board) is None

def find_fork_move(board, player):
    """
    Check if 'player' can create a fork on this turn.
    A fork is defined as a move that creates two potential winning threats.
    """
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    
    for move in range(9):
        if board[move] is None:
            board[move] = player
            # Count how many lines are one-move away from winning
            winning_chances = 0
            for (a,b,c) in win_positions:
                line = [board[a], board[b], board[c]]
                # Check if this line can lead to a win next turn.
                # That happens if we have exactly one player's symbol and two empty spots
                # or two player's symbols and one empty spot - basically a potential to win next turn.
                # But for a "fork," we specifically look for lines that are still open to winning:
                # Actually, to detect a fork, we want at least two lines
                # that could become winning moves in the next move.
                
                # Another approach: count how many potential wins player can set up from here:
                # A line is "winning threat" if it contains exactly the player's mark once
                # and the rest are empty (2 empties), or if it has two player's marks and one empty (i.e. immediate win next move).
                # We'll consider lines with exactly one player's mark and two empties or two player's marks and one empty as potential threats.
                
                if line.count(player) == 1 and line.count(None) == 2:
                    # future potential to make a line of three
                    winning_chances += 1
                elif line.count(player) == 2 and line.count(None) == 1:
                    # next move would be a direct win
                    winning_chances += 1
            
            board[move] = None  # revert
            if winning_chances >= 2:
                return move
    return None

def minimax(board, maximizing_player):
    winner = check_winner(board)
    if winner == 'X':
        return (1, None)
    elif winner == 'O':
        return (-1, None)
    elif is_draw(board):
        return (0, None)
    
    if maximizing_player:
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

def play_game():
    board = [None]*9
    
    # X starts in a corner (index 0)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    current_player = 'O'
    
    # O makes a random first move (not using minimax)
    first_moves = [i for i, cell in enumerate(board) if cell is None]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"O randomly chooses index {o_first_move} for the first move:")
    print_board(board)
    current_player = 'X'
    
    while True:
        winner = check_winner(board)
        if winner:
            print(f"The winner is: {winner}")
            break
        if is_draw(board):
            print("It's a draw.")
            break
        
        if current_player == 'X':
            # Before using minimax, try to find a fork move
            fork = find_fork_move(board, 'X')
            if fork is not None:
                move = fork
            else:
                # Use minimax to find the best move
                _, move = minimax(board, True)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O’s turn. If you want O to also try to fork, do so here:
            fork = find_fork_move(board, 'O')
            if fork is not None:
                move = fork
            else:
                # Use minimax for O
                _, move = minimax(board, False)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
