import pygad

'''
Task scheduler:
Each task needs a:
    - room (satisfy reqs)
    - duration (time)
    - mode of completion (slow, normal, fast)

There is a deadline for each task.
The mode of completion speeds up the duration.
However, it wastes more energy. Energy is given as a param E.

Encoding:
[room1, time_start1, mode1, is_used ...]

Fitness function:
+ how many tasks are completed 
- overlap between tasks
- energy is consumed over the specified limit
- wrong room is chosen
- the deadline has passed
'''


num_tasks, num_rooms = map(int, input().split())

tasks = {}
for i in range(num_tasks):  # duration num_allowed_rooms rooms...
    data = {}
    data_string = input().split()
    data['duration'] = float(data_string[0])
    data['rooms'] = list(map(int, data_string[2:]))

    tasks[i] = data

deadlines = list(map(int, input().split()))

distance = []
for _ in range(num_rooms):
    row = list(map(int, input().split()))
    distance.append(row)

modes = {
    0: (1.0, 1.0),   # (speed multiplier, energy rate)
    1: (0.75, 2.0),
    2: (0.5, 4.0)
}

E_MAX = 50


def fitness_func(ga, solution, idx):
    used_tasks = []
    num_unused = 0

    for i in range(num_rooms):
        loc  = int(solution[4*i])
        start = solution[4*i + 1]
        mode = int(solution[4*i + 2])
        use  = int(solution[4*i + 3])

        if use == 0:
            num_unused += 1
            continue

        speed, energy_rate = modes[mode]
        duration = tasks[i]['duration'] * speed
        end = start + duration

        used_tasks.append((i, loc, start, end, duration, energy_rate))

    num_used = len(used_tasks)

    if num_used == 0:
        return 0

    used_tasks_sorted = sorted(used_tasks, key=lambda x: x[2])

    hard_violations = 0

    current_loc = None
    current_end = None

    for task in used_tasks_sorted:
        i, loc, start, end, duration, energy_rate = task

        if end > deadlines[i]:
            hard_violations += 1

        if current_loc is not None:
            travel = distance[current_loc][loc]
            earliest_start = current_end + travel
            if start < earliest_start:
                hard_violations += 1

        current_loc = loc
        current_end = end

    if hard_violations > 0:
        return -10_000 * hard_violations


    penalty = 0
    reward = 0

    reward += 100 * num_used

    total_energy = sum(t[4] * t[5] for t in used_tasks)
    if total_energy > E_MAX:
        penalty += 20 * (total_energy - E_MAX)

    return reward - penalty


gene_space = []

for i in range(num_tasks):
    """
    room, start_time, energy_mode, is_used
    """
    gene_space.append(tasks[i]['rooms'])
    gene_space.append({'low': 0, 'high': deadlines[i]})
    gene_space.append([0, 1, 2])
    gene_space.append([0, 1])


ga = pygad.GA(
    num_generations=1000,
    num_parents_mating=25,
    sol_per_pop=50,
    num_genes=4 * num_tasks,

    fitness_func=fitness_func,
    gene_space=gene_space
)


ga.run()

solution, fitness, _ = ga.best_solution()

print("Fitness:", fitness)

for i in range(num_tasks):
    loc  = int(solution[4 * i])
    start = solution[4 * i + 1]
    mode = int(solution[4 * i + 2])
    use  = int(solution[4 * i + 3])

    print(f"Task {i}: use={use}, loc={loc}, start={start:.2f}, mode={mode}, duration={tasks[i]['duration']}, allowed={tasks[i]['rooms']}")

