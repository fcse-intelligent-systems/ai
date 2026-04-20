from constraint import *


def notAttacking(cannon1, cannon2):
    row1, col1 = cannon1
    row2, col2 = cannon2
    return row1 != row2 and col1 != col2  # for "queens" we would also add this `and abs(row1 - row2) != abs(col1 - col2)`


if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())

    variables = ["cannon_" + str(i) for i in range(8)]
    domain = [(row, col) for row in range(8) for col in range(8)]

    problem.addVariables(variables, domain)

    for cannon1 in variables:
        for cannon2 in variables:
            if cannon1 != cannon2:
                problem.addConstraint(notAttacking, (cannon1, cannon2))

    res = problem.getSolution()
    print(res)

    # for clearer output
    for row in range(8):
        for col in range(8):
            print("T" if (row, col) in res.values() else "_", end="")
        print()
