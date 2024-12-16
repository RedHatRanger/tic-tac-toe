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
    # Simple wrapper to run minimax and return the best move deterministically
    _, move = minimax(board, player_is_x)
    return move

def can_win_next(board, player):
    # Check if 'player' can win in one move
    for i in range(9):
        if board[i] is None:
            board[i] = player
            if check_winner(board) == player:
                board[i] = None
                return i
            board[i] = None
    return None

def block_or_win(board, player):
    # If player can win immediately, do it. Otherwise, block opponent if they can win next turn.
    opp = 'O' if player == 'X' else 'X'
    # Win if possible
    win_move = can_win_next(board, player)
    if win_move is not None:
        return win_move
    # Block opponent's win if possible
    block_move = can_win_next(board, opp)
    if block_move is not None:
        return block_move
    return None

def play_game():
    board = [None]*9
    
    # X starts in a corner (index 0)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    # O makes a random first move (not using minimax yet)
    first_moves = [i for i, cell in enumerate(board) if cell is None]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"O randomly chooses index {o_first_move} for the first move:")
    print_board(board)
    
    current_player = 'X'
    
    # If O did not choose center, X takes another corner immediately
    if o_first_move != 4:
        # Find an available corner other than 0
        corners = [2,6,8]
        available_corners = [c for c in corners if board[c] is None]
        if available_corners:
            chosen_corner = available_corners[0]  # pick the first available corner
            board[chosen_corner] = 'X'
            print(f"O did not choose center, X takes another corner at index {chosen_corner}:")
            print_board(board)
            current_player = 'O'
    
    # Now both players will attempt optimal play.
    # Remove randomization: O will just pick the best minimax move or block immediate threats.
    # X will also pick the best moves and attempt forks via minimax and immediate checks.
    
    while True:
        winner = check_winner(board)
        if winner:
            print(f"The winner is: {winner}")
            break
        if is_draw(board):
            print("It's a draw.")
            break

        if current_player == 'X':
            # X tries to win or block O if needed
            immediate_move = block_or_win(board, 'X')
            if immediate_move is not None:
                move = immediate_move
            else:
                # Use minimax for the best move
                move = get_best_move(board, True)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O tries to play optimally after the initial mistake
            # Check if O can win or must block X immediately
            immediate_move = block_or_win(board, 'O')
            if immediate_move is not None:
                move = immediate_move
            else:
                # If the center is available and beneficial, take it
                # (You could add heuristics here. For now, rely on minimax if no immediate threat.)
                
                # Use minimax for O's best move
                move = get_best_move(board, False)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
