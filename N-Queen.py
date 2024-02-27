import random

def read_initial_board(filename):
    """Reads the initial board configuration from a file."""
    with open(filename, 'r') as file:
        initial_board = [int(line.strip().split('#')[0]) for line in file if line.strip()]
    return initial_board

def count_conflicts(board, row, col):
    """Counts the number of conflicts for a queen at a given position."""
    conflicts = 0
    for i in range(len(board)):
        if i == row:
            continue
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            conflicts += 1
    return conflicts

def find_most_conflicted_queen(board):
    """Finds the queen with the most conflicts."""
    max_conflicts = 0
    most_conflicted_queens = []
    for row in range(len(board)):
        conflicts = count_conflicts(board, row, board[row])
        if conflicts == max_conflicts:
            most_conflicted_queens.append(row)
        elif conflicts > max_conflicts:
            max_conflicts = conflicts
            most_conflicted_queens = [row]
    if not most_conflicted_queens:
        return None
    return random.choice(most_conflicted_queens)

def minimize_conflicts(board, row):
    """Tries to place the queen in the row to a position with fewer conflicts."""
    min_conflicts = len(board)
    best_columns = []
    for col in range(len(board)):
        conflicts = count_conflicts(board, row, col)
        if conflicts == min_conflicts:
            best_columns.append(col)
        elif conflicts < min_conflicts:
            min_conflicts = conflicts
            best_columns = [col]
    if best_columns:
        board[row] = random.choice(best_columns)

def solve_n_queens(n, max_iterations=50000):
    """Solves the N-Queens problem using an iterative approach."""
    board = [random.randint(0, n - 1) for _ in range(n)]
    for _ in range(max_iterations):
        row = find_most_conflicted_queen(board)
        if row is None:
            # No conflicts found, solution is reached
            return board
        minimize_conflicts(board, row)
    for i in range(len(board)):
        board[i] +=1
    return board  # Return the last board even if not a solution

def draw_board(board):
    n = len(board)
    # Initialize blank_board with independent rows
    blank_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(board)):
        blank_board[i][board[i]] = 1

    return blank_board

    
    print(blank_board)
def main():
    n = 10  # Assuming a 10x10 board for simplicity, adjust as needed
    initial_board = read_initial_board('n-queen.txt')  # Ensure the file exists and is correctly formatted
    print("Initial board:", initial_board)
    solution = solve_n_queens(n)
    print("Solution:", solution)
    # print(draw_board(solution))

if __name__ == "__main__":
    main()
