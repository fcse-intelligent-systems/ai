import pygad


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

    # CAREFUL: `solution` is a numpy array and the values are continuous
    solution = solution.argsort()
    # solutions = sorted(enumerate(solution), key=lambda x: x[1])
    # solution = [idx for idx, value in solutions]

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

    'gene_space': {'low': 0, 'high': 1},
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)




