import csv

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function to determine the best move for the next player
def determine_best_move(board, player):
    opponent = 'O' if player == 'X' else 'X'
    # Check for a winning move
    for i in range(9):
        if board[i] == ' ':
            potential_board = board[:i] + player + board[i+1:]
            if check_winner(potential_board, player):
                return i, 'WIN'
    # Block opponent's winning move
    for i in range(9):
        if board[i] == ' ':
            potential_board = board[:i] + opponent + board[i+1:]
            if check_winner(potential_board, opponent):
                return i, 'BLOCK'
    # Choose center if available
    if board[4] == ' ':
        return 4, 'DEFAULT'
    # Choose a corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i, 'DEFAULT'
    # Choose any available move
    for i in range(9):
        if board[i] == ' ':
            return i, 'DEFAULT'
    return -1, 'DEFAULT'  # No move possible

# Function to process each board position
def process_board_positions(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Board Position', 'Game Status', 'Next Player', 'Best Move', 'Strategy'])
        next(reader)  # Skip header
        for row in reader:
            board = row[0]
            if check_winner(board, 'X'):
                game_status = 'X won'
                next_player = ''
                best_move = ''
                strategy = ''
            elif check_winner(board, 'O'):
                game_status = 'O won'
                next_player = ''
                best_move = ''
                strategy = ''
            elif ' ' not in board:
                game_status = 'Draw'
                next_player = ''
                best_move = ''
                strategy = ''
            else:
                game_status = 'In Progress'
                next_player = 'X' if board.count('X') == board.count('O') else 'O'
                best_move_index, strategy = determine_best_move(board, next_player)
                best_move = best_move_index
            writer.writerow([board, game_status, next_player, best_move, strategy])

if __name__ == "__main__":
    process_board_positions('valid_tictactoe_game_paths.csv', 'augmented_tictactoe_positions.csv')
