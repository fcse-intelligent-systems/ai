from constraint import *

# def notBothOne(a, b):
#     return not (a == 1 and b == 1)

# eg:
# 0 1 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 1 0

if __name__ == '__main__':
    problem = Problem()

    variables = [(x, y) for x in range(8) for y in range(8)]
    domains = [1, 0]

    problem.addVariables(variables, domains)

    # for row in range(8):
    #   for col1 in range(8):
    #     for col2 in range(col1 + 1, 8):
    #       problem.addConstraint(notBothOne, [(row, col1), (row, col2)])
    # # or instead we can do this:
    for row in range(8):
        row_vars = [(row, col) for col in range(8)]
        problem.addConstraint(ExactSumConstraint(1), row_vars)

    # for col in range(8):
    #   for row1 in range(8):
    #     for row2 in range(row1 + 1, 8):
    #       problem.addConstraint(notBothOne, [(row1, col), (row2, col)])
    # # or instead we can do this:
    for col in range(8):
        col_vars = [(row, col) for row in range(8)]
        problem.addConstraint(ExactSumConstraint(1), col_vars)

    # problem.addConstraint(ExactSumConstraint(8), variables)

    solution = problem.getSolution()
    print(solution)

    # for clearer output
    for row in range(8):
        for col in range(8):
            print(solution[(row, col)], end="\t")
        print()
