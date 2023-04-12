import random
import time

def n_queens_genetic(n):
    def fitness(board):
        attacking_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                    attacking_pairs += 1
        return 1 / (attacking_pairs + 1)
    
    def crossover(parent1, parent2):
        pivot = random.randint(1, n - 1)
        child = parent1[:pivot] + parent2[pivot:]
        return child
    
    def mutate(board):
        index = random.randint(0, n - 1)
        new_val = random.randint(0, n - 1)
        board[index] = new_val
        return board
    
    start_time = time.time()
    solutions = []
    population_size = 100
    generations = 100
    mutation_prob = 0.1
    population = [random.sample(range(n), n) for _ in range(population_size)]
    for generation in range(generations):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == 1:
            solutions.append(population[0])
            break
        new_population = population[:int(population_size * 0.2)]
        while len(new_population) < population_size:
            parent1 = random.choices(population[:int(population_size * 0.4)], weights=[fitness(board) for board in population[:int(population_size * 0.4)]])[0]
            parent2 = random.choices(population[:int(population_size * 0.4)], weights=[fitness(board) for board in population[:int(population_size * 0.4)]])[0]
            child = crossover(parent1, parent2)
            if random.random() < mutation_prob:
                child = mutate(child)
            new_population.append(child)
        population = new_population
    end_time = time.time()
    return solutions, end_time - start_time

if __name__ == '__main__':
    n = 8
    solutions, time_taken = n_queens_genetic(n)
    print(f"Found {len(solutions)} solutions to {n}-queens problem in {time_taken} seconds:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")
