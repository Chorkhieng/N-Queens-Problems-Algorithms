import time

def n_queens_backtracking(n):
    start_time = time.time()
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True
    
    def backtrack(board, row):
        nonlocal solutions
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    end_time = time.time()
    return solutions, end_time - start_time

if __name__ == '__main__':
    n = 8
    solutions, time_taken = n_queens_backtracking(n)
    print(f"Found {len(solutions)} solutions to {n}-queens problem in {time_taken} seconds:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")
