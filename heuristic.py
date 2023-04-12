import random
import time

def n_queens_heuristic(n):
    def heuristic(board):
        attacking_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                    attacking_pairs += 1
        return attacking_pairs
    
    def hill_climbing(board):
        current_h = heuristic(board)
        while True:
            next_boards = []
            for i in range(n):
                for j in range(n):
                    if board[i] != j:
                        new_board = list(board)
                        new_board[i] = j
                        next_boards.append(new_board)
            if not next_boards:
                break
            next_boards.sort(key=heuristic)
            if heuristic(next_boards[0]) >= current_h:
                break
            board = next_boards[0]
            current_h = heuristic(board)
        return board
    
    start_time = time.time()
    solutions = []
    for i in range(100):
        board = hill_climbing(random.sample(range(n), n))
        if heuristic(board) == 0:
            solutions.append(board)
    end_time = time.time()
    return solutions, end_time - start_time

if __name__ == '__main__':
    n = 8
    solutions, time_taken = n_queens_heuristic(n)
    print(f"Found {len(solutions)} solutions to {n}-queens problem in {time_taken} seconds:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")
