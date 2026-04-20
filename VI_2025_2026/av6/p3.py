import pygad

N = 5
values = [10, 5, 15, 7, 6]
weights = [2, 3, 5, 7, 1]
C = 10


def fitness_func(ga, solution, idx):
    xs = solution
    value = 0
    weight = 0
    for x, v, w in zip(xs, values, weights):
        value += x * v
        weight += x * w

    overflow = weight - C

    if overflow < 0:  # No overflow
        return value
    else:
        # Overflow is a measure of weight
        # We want to return a measure of value
        # Penalize each unit of overflow by the best possible value you could get per unit weight
        return value - overflow * max(v / w for v, w in zip(values, weights))


params = {
    'num_generations': 500,
    'num_parents_mating': 50,
    'sol_per_pop': 100,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': [0, 1],
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)