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
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return all(cell is not None for cell in board) and check_winner(board) is None

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

def get_best_move(board, player_is_x):
    _, move = minimax(board, player_is_x)
    return move

def immediate_threat(board, player):
    """
    Checks if 'player' can immediately win or needs to block an opponent's win.
    Priority: 
    1. If player can win immediately, return that move.
    2. Else, if the opponent can win next turn, return the blocking move.
    If no immediate threat or win, return None.
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
            # Player can win
            empty_index = [a,b,c][line.index(None)]
            return empty_index
    
    # If no immediate win, check if opponent can win and block.
    for a,b,c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count(None) == 1:
            # Opponent can win next turn, block it
            empty_index = [a,b,c][line.index(None)]
            return empty_index
    
    return None

def play_game():
    board = [None]*9
    turn_number = 1  # Will increment each move
    
    # X always starts at corner (index 0)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    # O makes a random first move without center
    first_moves = [i for i, cell in enumerate(board) if cell is None and i != 4]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    turn_number += 1
    print(f"Turn {turn_number}: O randomly chooses index {o_first_move} for the first move (no center):")
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
        
        turn_number += 1
        
        if current_player == 'X':
            # Check for immediate threats (win/block)
            move = immediate_threat(board, 'X')
            if move is None:
                # No immediate threat, use minimax
                move = get_best_move(board, True)
            board[move] = 'X'
            print(f"Turn {turn_number}: X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O's turn, check immediate threats
            move = immediate_threat(board, 'O')
            if move is None:
                move = get_best_move(board, False)
            board[move] = 'O'
            print(f"Turn {turn_number}: O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
