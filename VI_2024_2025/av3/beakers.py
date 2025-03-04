from searching_framework import Problem, breadth_first_graph_search


class Beakers(Problem):
    def __init__(self, capacity, initial, goal):
        super().__init__(initial, goal)
        self.capacity = capacity

    def successor(self, state):
        neighbors = dict()

        # # Empty0
        # rez1 = self.action_empty_0(state)
        # if rez1 is not None: neighbors["Empty_from_0"] = rez1

        rez1 = self.action_empty(state, 0)
        if rez1 is not None: neighbors["Empty_from_0"] = rez1

        rez2 = self.action_empty(state, 1)
        if rez2 is not None: neighbors["Empty_from_1"] = rez2

        rez3 = self.action_transfer(state, 0, 1)
        if rez3 is not None: neighbors["Transfer_from_0_to_1"] = rez3

        rez4 = self.action_transfer(state, 0, 1)
        if rez4 is not None: neighbors["Transfer_from_1_to_0"] = rez4

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    # def action_empty_0(self, state):
    def action_empty(self, state, _from):
        if state[_from] == 0: return None
        # if state[0] == 0: return None # for `def action_empty_0`
        new_state = list(state)
        new_state[_from] -= 1
        # new_state[0] -= 1 # for `def action_empty_0`
        return tuple(new_state)

    def action_transfer(self, state, _from, _to):
        if state[_from] == 0 or state[_to] == self.capacity[_to]:
            return None
        new_state = list(state)
        new_state[_from] -= 1
        new_state[_to] += 1
        return tuple(new_state)


""" example:
12 8
6 4
8 3
"""
if __name__ == '__main__':
    capacity = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    initial = tuple(map(int, input().split()))
    problem = Beakers(capacity, initial, goal)
    node = breadth_first_graph_search(problem)
    print(node)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
