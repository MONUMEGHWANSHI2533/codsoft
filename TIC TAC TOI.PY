import math

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Winning combinations
WIN_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Print the board
def print_board(board):
    for i in range(3):
        print(f"{board[i * 3]}|{board[i * 3 + 1]}|{board[i * 3 + 2]}")
        if i < 2:
            print("-----")

# Check for a win
def check_win(board, player):
    for combo in WIN_COMBINATIONS:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Check for a draw
def check_draw(board):
    return all(space != EMPTY for space in board)

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, AI):
        return 1
    if check_win(board, HUMAN):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

# Main game loop
def play_game():
    board = [EMPTY] * 9
    current_player = HUMAN

    while True:
        print_board(board)
        if check_win(board, HUMAN):
            print("Human wins!")
            break
        elif check_win(board, AI):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        if current_player == HUMAN:
            move = int(input("Enter your move (0-8): "))
            if board[move] == EMPTY:
                board[move] = HUMAN
                current_player = AI
        else:
            move = find_best_move(board)
            board[move] = AI
            current_player = HUMAN

# Start the game
play_game()