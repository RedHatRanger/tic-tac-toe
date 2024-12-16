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
    Minimax algorithm:
    - board: current state of the game
    - maximizing_player: boolean, True if we are picking for X, False for O
    
    Returns: (score, move)
    score is the evaluation of the position: 
      +1 if X is winning
       0 if draw
      -1 if O is winning
    move is the best move index for the current player
    """
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
    # Represent the board as a list of length 9
    # Indices:
    # 0 | 1 | 2
    # 3 | 4 | 5
    # 6 | 7 | 8
    board = [None]*9
    
    # X usually starts. According to ideal strategy, X picks a corner first.
    # Let's pick a corner index 0 as a demonstration.
    board[0] = 'X'
    print("X chooses a corner (index 0):")
    print_board(board)
    
    current_player = 'O'  # O moves next
    
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
            _, move = minimax(board, True)
            board[move] = 'X'
            print(f"X plays at index {move}:")
            print_board(board)
            current_player = 'O'
        else:
            # O tries to minimize the score (or maximize O's perspective)
            _, move = minimax(board, False)
            board[move] = 'O'
            print(f"O plays at index {move}:")
            print_board(board)
            current_player = 'X'

if __name__ == "__main__":
    play_game()
