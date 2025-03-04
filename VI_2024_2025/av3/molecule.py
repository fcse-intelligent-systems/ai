from searching_framework import Problem, breadth_first_graph_search


class Molecules(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.rows = 7
        self.cols = 9
        self.matrix = (
            (0, 0, 0, 1, 0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0, 0, 0, 0, 1),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 1, 1, 0),
            (0, 0, 0, 0, 1, 0, 1, 0, 0),
            (1, 1, 0, 1, 0, 0, 1, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
        )

    def goal_test(self, state):
        atom1, atom2, atom3 = state
        return atom1[0] + 1 == atom2[0] and atom2[0] + 1 == atom3[0] \
            and atom1[1] == atom2[1] and atom2[1] == atom3[1]
        # i.e.:
        # (x0, y0), (x1, y1), (x2, y2) = state #  depending on python version
        # return x0 + 1 == x1 and x1 + 1 == x2 and y0 == y1 and y1 == y2

    def successor(self, state):
        neighbors = dict()

        actions = ("Right", "Left", "Up", "Down")
        directions = ((+1, 0), (-1, 0), (0, -1), (0, +1))
        for action, direction in zip(actions, directions):
            for ind in range(3):
                action_name = action + str(ind)
                rez = self.move(state, direction, ind)
                if rez != None:
                    neighbors[action_name] = rez

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move(self, state, direction, ind):
        atom_to_move = state[ind]
        new_atom = self.move_atom_dir(atom_to_move, direction)

        new_state = list(state)
        new_state[ind] = new_atom
        new_state = tuple(new_state)

        if not self.is_valid_state(new_state): return None

        """ p.s. first see end_state line below comments
        At this point we can safely return `new_state` since it is not `None`.
        But we want to see if we can further move the atom in
        this direction, and with recursion we'll ask the atom to
        be moved as far as possible. The last of the recursive calls
        will be unable to move the atom and it will return `None`.
        Then the parent recursive call will return `new_state` 
        instead of `end_state` (because `end_state` was returned 
        as `None` from the last call). This returned `new_state` 
        will be the result `end_state` for all the recursive calls
        above, effectively moving the atom to the last possible place.
        If it is not possible to perform at least one move
        then it would've returned `None` in the previous `if` condition.
        """

        end_state = self.move(new_state, direction, ind)
        if end_state == None:
            return new_state  # we already performed the check that new_state is valid
        else:
            return end_state

    def move_atom_dir(self, atom, direction):
        atom = list(atom)
        atom[0] += direction[0]
        atom[1] += direction[1]
        return tuple(atom)

    def is_valid_state(self, state):
        for atom in state:
            x, y = atom
            if not (0 <= x < self.cols and 0 <= y < self.rows):
                return False
            "Whether the coordinates are valid must be checked before"
            "accessing the matrix with those coordinates"
            if self.matrix[y][x] == 1:
                return False

        "If all three atoms are distinct then the set of atoms will have 3 unique values"
        if len(set(state)) == 3:
            return True
        return False
        # i.e.: return len(set(state)) == 3


""" example
2 5
7 4
2 0
"""
if __name__ == '__main__':
    atom_1 = tuple(map(int, input().split()))
    atom_2 = tuple(map(int, input().split()))
    atom_3 = tuple(map(int, input().split()))
    # i.e.:      atom_1,atom_2,atom_3 = \
    #   map( lambda _: map(int, input().split()), range(3) )

    problem = Molecules((atom_1, atom_2, atom_3))
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
        actions, states = node.solution(), node.solve()
        print(states[0])
        for action, state in zip(actions, states[1:]):
            print(action, state, sep="\n")
    else:
        print("Nema Resenie")
