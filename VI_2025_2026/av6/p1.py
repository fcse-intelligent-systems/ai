import pygad

N = int(input())

def fitness_func(ga, solution, idx):
    return sum(solution)

params = {
    'num_generations': 200,
    'num_parents_mating': 50,
    'sol_per_pop': 100,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': [0, 1]
}


ga = pygad.GA(**params)

ga.run()
ga.plot_fitness(save_dir='p1_plot.png')

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)