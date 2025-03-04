from constraint import *

if __name__ == '__main__':
    # problem = Problem(MinConflictsSolver()) # this sometimes provides no solution due to an error in the MinConflictsSolver class
    problem = Problem(BacktrackingSolver())

    variables = range(16)
    domain = range(1, 17)
    problem.addVariables(variables, domain)

    suma = 34  # after analyzing the problem, we can see that the sum of each row, column and diagonal is 34

    for first in [0, 4, 8, 12]:  # in range(0, n*n, n)
        row_vars = [first + move for move in range(4)]
        problem.addConstraint(ExactSumConstraint(suma), row_vars)
    for first in [0, 1, 2, 3]:  # in range(0, n, 1)
        col_vars = [first + move for move in range(0, 16, 4)]  # in range(0, n*n, n)
        problem.addConstraint(ExactSumConstraint(suma), col_vars)

    main_diag_vars = [move for move in range(0, 16, 5)]  # in range(0, n*n, n+1)
    minor_diag_vars = [3 + move for move in range(0, 12, 3)]  # in range(n-1, n*n-1, n-1)
    problem.addConstraint(ExactSumConstraint(suma), main_diag_vars)
    problem.addConstraint(ExactSumConstraint(suma), minor_diag_vars)

    problem.addConstraint(AllDifferentConstraint(), variables)

    print(problem.getSolution())
