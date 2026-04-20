import pygad

N, M = 20, 20

start_pos = (0, 0)
end_pos = (19, 19)

grid = [
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
[1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
[1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
[0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0],
[1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
[0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0],
[1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
[0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0],
[1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
[0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0]
]

# A guess for how many steps we will need. Worst case is visiting N * M cells
lim_num_actions = 2 * (N + M)

moves = {
    0: 'Up',
    1: 'Right',
    2: 'Down',
    3: 'Left'
}

def fitness_func(ga, solution, idx):
    i, j = 0, 0
    num_steps = 0
    num_obstacles_crossed = 0
    out_of_grid = 0
    reached_goal = 0

    for action in solution:
        action = moves[action]
        if action == 'Up':
            i -= 1
        elif action == 'Right':
            j += 1
        elif action == 'Down':
            i += 1
        elif action == 'Left':
            j -= 1

        num_steps += 1

        if (i, j) == end_pos:
            reached_goal += 1
            break

        if not (0 <= i < N and 0 <= j < M):
            out_of_grid += 1
            continue

        if grid[i][j] == 1:
            num_obstacles_crossed += 1

    # Priority:
    # first: reach goal
    # second: avoid getting out of grid
    # third: avoid obstacles
    # fourth: shorter path
    # tie-breaker: closeness to goal
    return (
        (10_000 if reached_goal else 0)  # Maximize goal obtainability
        - 1_000 * out_of_grid  # Minimize out-of-grid steps
        - 100 * num_obstacles_crossed  # Minimize number of obstacles crossed
        - 1 * num_steps  # Minimize number of steps taken
        - (abs(i - end_pos[0]) + abs(j - end_pos[1]))  # Minimize person closeness to goal
    )

params = {
    'num_generations': 300,
    'num_parents_mating': 250,
    'sol_per_pop': 500,
    'num_genes': lim_num_actions,

    'fitness_func': fitness_func,

    'gene_space': list(moves.keys())
}


ga = pygad.GA(**params)

ga.run()
ga.plot_fitness(save_dir='p5_plot.png')

solution, _, _ = ga.best_solution()
print([moves[act] for act in solution])
print(fitness_func(None, solution, None))













