import pygad
import numpy as np

N = 5

dist = [
    [0,  2,  9, 10, 7],
    [2,  0,  6,  4, 3],
    [9,  6,  0,  8, 5],
    [10, 4,  8,  0, 6],
    [7,  3,  5,  6, 0]
]

def fitness_func(ga, solution, idx):
    total = 0

    # CAREFUL: Solution is a numpy array
    solution = solution.astype(int)
    # solution = [int(el) for el in solution]

    i = solution[0]
    for j in solution[1:]:
        total += dist[i][j]
        i = j
    total += dist[solution[-1]][solution[0]]

    return -total


params = {
    'num_generations': 500,
    'num_parents_mating': 25,
    'sol_per_pop': 50,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': list(range(N)),
    'allow_duplicate_genes': False,
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)




