from constraint import *

def notEqualColors(color_1, color_2):
    return color_1 != color_2

if __name__ == '__main__':
    problem = Problem()

    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    problem.addVariables(variables, ["R", "G", "B"])

    # problem.addConstraint(FunctionConstraint(notEqualColors), ("WA", "NT"))
    # # or
    # problem.addConstraint(notEqualColors, ("WA", "NT"))
    # # or
    # problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))

    # # for each pair
    # problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "NT"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
    # problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
    # problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
    # problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

    # or we could do this:
    pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"), ("Q", "NSW"), ("NSW", "V")]
    for pair in pairs:
        problem.addConstraint(notEqualColors, pair)

    print(problem.getSolution())

    print(problem.getSolutions())

    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))
