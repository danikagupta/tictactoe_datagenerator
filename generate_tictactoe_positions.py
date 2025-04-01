import itertools
import csv

# Function to check if a player has won
# A player wins if there are 3 of their marks in a row, column, or diagonal

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function to generate all possible game paths
# A path is terminated when a player wins, the board is full, or no further moves can be made
def generate_game_paths(board, player):
    paths = [board]  # Include the current board state
    if check_winner(board, 'X') or check_winner(board, 'O'):
        return paths
    if ' ' not in board:
        return paths
    for i in range(9):
        if board[i] == ' ':
            new_board = board[:i] + player + board[i+1:]
            next_player = 'O' if player == 'X' else 'X'
            paths.extend(generate_game_paths(new_board, next_player))
    return paths

# Function to write valid game paths to a CSV file
def write_paths_to_csv(paths, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Game Path'])
        for path in paths:
            writer.writerow([path])

if __name__ == "__main__":
    # Start with an empty board and 'X' as the first player
    initial_board = ' ' * 9
    valid_game_paths = generate_game_paths(initial_board, 'X')
    # Remove duplicates by converting to a set and back to a list
    unique_game_paths = list(set(valid_game_paths))
    # Write to CSV
    write_paths_to_csv(unique_game_paths, 'valid_tictactoe_game_paths.csv')
    print(f"Generated {len(unique_game_paths)} unique game paths.")
