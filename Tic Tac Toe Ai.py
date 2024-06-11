import math

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board: print('|'.join(row)), print('-' * 5)

def moves_left(): return any(' ' in row for row in board)

def evaluate():
    for row in board:
        if row[0] == row[1] == row[2] != ' ': return 10 if row[0] == 'X' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ': return 10 if board[0][col] == 'X' else -10
    if board[0][0] == board[1][1] == board[2][2] != ' ': return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ': return 10 if board[0][2] == 'X' else -10
    return 0

def minimax(is_max, alpha, beta):
    score = evaluate()
    if score or not moves_left(): return score
    best = -math.inf if is_max else math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X' if is_max else 'O'
                val = minimax(not is_max, alpha, beta)
                board[i][j] = ' '
                if is_max:
                    best = max(best, val)
                    alpha = max(alpha, best)
                else:
                    best = min(best, val)
                    beta = min(beta, best)
                if beta <= alpha: break
    return best

def find_best_move():
    best_val, best_move = -math.inf, (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val: best_val, best_move = move_val, (i, j)
    return best_move

def play_game():
    turn = 'human'
    while moves_left() and not evaluate():
        print_board()
        if turn == 'human':
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ': board[row][col] = 'O'; turn = 'ai'
            else: print("Invalid move. Try again.")
        else:
            row, col = find_best_move()
            board[row][col] = 'X'
            turn = 'human'
    print_board()
    score = evaluate()
    if score == 10: print("AI wins!")
    elif score == -10: print("You win!")
    else: print("It's a draw!")

play_game()
