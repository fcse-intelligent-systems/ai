from constraint import *


def sumOf4EqualsVar(sum_var, a, b, c, d):
    return sum_var == sum([a, b, c, d])


if __name__ == '__main__':
    # problem = Problem(MinConflictsSolver()) # MinConflictsSolver() is not working, returns None although a solution exists
    problem = Problem(BacktrackingSolver())

    variables = [(i, j) for i in range(4) for j in range(4)]
    domains = range(1, 17)
    problem.addVariables(variables, domains)

    sum_vars = [f"sum_row_{ind}" for ind in range(4)] + \
               [f"sum_col_{ind}" for ind in range(4)] + \
               ["sum_diag_1", "sum_diag_2"]
    sums_domain = range(1, 65)
    # sums_domain = range(34, 35) # if we further analyze the problem, we can see that the sum of each row, column and diagonal is 34, then we won't need the sum_vars at all, which will speed up the computations
    problem.addVariables(sum_vars, sums_domain)

    # The print below will help you understand the tuples
    sums_4_tuples = \
        [[(row, col) for col in range(4)] for row in range(4)] + \
        [[(row, col) for row in range(4)] for col in range(4)] + \
        [[(ind, ind) for ind in range(4)]] + \
        [[(ind, 3 - ind) for ind in range(4)]]

    for sum_var, vars_4_tuple in zip(sum_vars, sums_4_tuples):
        print(sum_var, vars_4_tuple)
        problem.addConstraint(sumOf4EqualsVar, [sum_var] + vars_4_tuple)

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(AllEqualConstraint(), sum_vars)

    solution = problem.getSolution()
    print(solution)

    for row in range(4):
        for col in range(4):
            print(solution[(row, col)], end=" ")
        print()
