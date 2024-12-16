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

def find_fork_move(board, player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    for move in range(9):
        if board[move] is None:
            board[move] = player
            winning_chances = 0
            for (a,b,c) in win_positions:
                line = [board[a], board[b], board[c]]
                # Count potential future wins
                # A "threat" line: line with player marks and empties that could become a win soon.
                if line.count(player) == 2 and line.count(None) == 1:
                    # Immediate winning move next turn
                    winning_chances += 1
                elif line.count(player) == 1 and line.count(None) == 2:
                    # Potential future threat
                    winning_chances += 1
            board[move] = None
            
            # Adjust the fork criteria if you want stricter definition.
            # Typically, a fork means at least two distinct winning opportunities created.
            # We'll say winning_chances >= 2 here.
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

def get_available_corners(board):
    corners = [0,2,6,8]
    return [c for c in corners if board[c] is None]

def play_game():
    board = [None]*9
    
    # X starts in a corner (index 0)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    # O makes a random first move
    first_moves = [i for i, cell in enumerate(board) if cell is None]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"O randomly chooses index {o_first_move} for the first move:")
    print_board(board)
    
    current_player = 'X'
    
    # If O did not take the center, enforce X to take another corner now.
    if o_first_move != 4:
        # O missed the center, X should now take another corner if available.
        second_corners = get_available_corners(board)
        if second_corners:
            move = random.choice(second_corners)  # or pick a specific corner to be consistent
            board[move] = 'X'
            print(f"O did not choose center, X takes another corner at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # If somehow no corner is available (unlikely), proceed normally.
            current_player = 'X'
    
    # Continue the game with fork and minimax logic
    while True:
        winner = check_winner(board)
        if winner:
            print(f"The winner is: {winner}")
            break
        if is_draw(board):
            print("It's a draw.")
            break
        
        if current_player == 'X':
            # Check for fork
            fork_move = find_fork_move(board, 'X')
            if fork_move is not None:
                move = fork_move
            else:
                _, move = minimax(board, True)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O’s turn (if you want O to also try to fork, add fork logic here)
            _, move = minimax(board, False)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
