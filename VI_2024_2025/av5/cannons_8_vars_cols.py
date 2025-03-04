from constraint import *

if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())

    variables = ["cannon_" + str(i) for i in range(8)]
    domain = range(8)

    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables)

    res = problem.getSolution()
    print(res)

    # for clearer output
    for row in range(8):
        chosen_column = res["cannon_" + str(row)]
        for col in range(8):
            print("T" if col == chosen_column else "_", end="")
        print()