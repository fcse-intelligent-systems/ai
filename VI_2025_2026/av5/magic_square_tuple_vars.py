from constraint import *
if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = [ (x,y) for x in range(4) for y in range(4) ]
    problem.addVariables(variables, range(1, 17))

    for row in range(4):
        row_vars = [(row, col) for col in range(4)]
        problem.addConstraint(ExactSumConstraint(34), row_vars)

    for col in range(4):
        col_vars = [(row, col) for row in range(4)]
        problem.addConstraint(ExactSumConstraint(34), col_vars)

    main_diag_vars = [(ind, ind) for ind in range(4)]
    minor_diag_vars = [(ind, 3 - ind) for ind in range(4)]
    problem.addConstraint(ExactSumConstraint(34), main_diag_vars)
    problem.addConstraint(ExactSumConstraint(34), minor_diag_vars)

    problem.addConstraint(AllDifferentConstraint(), variables)

    solution = problem.getSolution()
    # for clearer output
    print(solution)
    for row in range(4):
        for col in range(4):
            print(solution[(row, col)], end="\t")
        print()



