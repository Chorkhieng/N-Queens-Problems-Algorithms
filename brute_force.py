import itertools
import time

def n_queens_brute_force(n):
    start_time = time.time()
    solutions = []
    for permutation in itertools.permutations(range(n)):
        if n == len(set(permutation[i] + i for i in range(n))) \
             == len(set(permutation[i] - i for i in range(n))):
            solutions.append(permutation)
    end_time = time.time()
    return solutions, end_time - start_time

if __name__ == '__main__':
    n = 8
    solutions, time_taken = n_queens_brute_force(n)
    print(f"Found {len(solutions)} solutions to {n}-queens problem in {time_taken} seconds:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")
