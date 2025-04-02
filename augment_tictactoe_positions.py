import csv

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Minimax algorithm to determine the best move for the next player
def minimax(board, depth, is_maximizing, player):
    opponent = 'O' if player == 'X' else 'X'
    if check_winner(board, player):
        return 10 - depth
    elif check_winner(board, opponent):
        return depth - 10
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                potential_board = board[:i] + player + board[i+1:]
                score = minimax(potential_board, depth + 1, False, player)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                potential_board = board[:i] + opponent + board[i+1:]
                score = minimax(potential_board, depth + 1, True, player)
                best_score = min(score, best_score)
        return best_score

# Function to determine the best move using Minimax
def determine_best_move(board, player):
    best_score = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            potential_board = board[:i] + player + board[i+1:]
            score = minimax(potential_board, 0, False, player)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move, 'OPTIMAL'

# Function to process each board position
def process_board_positions(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Pos0', 'Pos1', 'Pos2', 'Pos3', 'Pos4', 'Pos5', 'Pos6', 'Pos7', 'Pos8', 'Result'])
        next(reader)  # Skip header
        for row in reader:
            board = ''.join(row[:9])
            if check_winner(board, 'X'):
                result = 'X won'
            elif check_winner(board, 'O'):
                result = 'O won'
            elif ' ' not in board:
                result = 'Draw'
            else:
                next_player = 'X' if board.count('X') == board.count('O') else 'O'
                best_move, _ = determine_best_move(board, next_player)
                result = f'{next_player}{best_move}'
            writer.writerow(list(board) + [result])

if __name__ == "__main__":
    process_board_positions('valid_tictactoe_game_paths.csv', 'augmented_tictactoe_positions.csv')
