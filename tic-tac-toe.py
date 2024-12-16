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

def play_game():
    board = [None]*9
    
    # X starts in a corner (index 0)
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    # O makes a random first move, excluding the center (index 4)
    first_moves = [i for i, cell in enumerate(board) if cell is None and i != 4]
    o_first_move = random.choice(first_moves)
    board[o_first_move] = 'O'
    print(f"O randomly chooses index {o_first_move} for the first move (no center):")
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
            # X tries to pick the best move
            move = get_best_move(board, True)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O tries to pick the best move
            move = get_best_move(board, False)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
