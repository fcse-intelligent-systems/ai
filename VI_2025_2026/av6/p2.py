import pygad


def fitness_func(ga, solution, idx):
    x, y = solution
    return x * y - (x - 3) ** 2 - (y - 6) ** 2

params = {
    'num_generations': 50,
    'num_parents_mating': 50,
    'sol_per_pop': 100,
    'num_genes': 2,

    'fitness_func': fitness_func,

    'gene_space': {'low': 0, 'high': 10},
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()
# ga.plot_fitness(save_dir='p2_plot.png')

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)