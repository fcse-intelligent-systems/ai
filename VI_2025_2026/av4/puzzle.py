from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search

class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        '''
        "*32415678"
        0 1 2
        3 4 5
        6 7 8
        '''

        successors = dict()
        ind = state.index("*")

        #Up i-3
        if ind > 2:
            tmp = list(state)
            tmp[ind], tmp[ind-3] = tmp[ind-3], tmp[ind]
            new_state = ''.join(tmp)
            successors["Up"] = new_state

        #Down i+3
        if ind < 6:
            tmp = list(state)
            tmp[ind], tmp[ind+3] = tmp[ind+3], tmp[ind]
            new_state = ''.join(tmp)
            successors["Down"] = new_state

        #Left i-1
        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind-1] = tmp[ind-1], tmp[ind]
            new_state = ''.join(tmp)
            successors["Left"] = new_state

        #Right i+1
        if ind % 3 != 2:
            tmp = list(state)
            tmp[ind], tmp[ind+1] = tmp[ind+1], tmp[ind]
            new_state = ''.join(tmp)
            successors["Right"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        '''
        a=[1,2,3] b=['a','b','c']
        zip(a,b) = [(1,'a'), (2,'b'), (3,'c')]
        zip('*32415678', '*12345678') = [(*,*), (3,1), (2,2) ...]
        '''
        counter = 0

        for x,y in zip(node.state, self.goal):
            if x != y:
                counter += 1

        return counter

class Puzzle_h2(Puzzle):
    coordinates = {
        0: (0,2), 1: (1,2), 2: (2,2),
        3: (0,1), 4: (1,1), 5: (2,1),
        6: (0,0), 7: (1,0), 8: (2,0)
    }

    @staticmethod
    def mhd(n, m):
        x1, y1 = Puzzle_h2.coordinates[n]
        x2, y2 = Puzzle_h2.coordinates[m]

        return abs(x1-x2) + abs(y1-y2)

    def h(self, node):
        sum_value = 0

        for x in '12345678':
            val = Puzzle_h2.mhd(node.state.index(x), int(x))
            sum_value += val

        return sum_value

if __name__ == '__main__':
    puzzle = Puzzle("*32415678", "*12345678")

    result1 = astar_search(puzzle)
    print(result1.solve())
    result2 = greedy_best_first_graph_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solution())
    
    puzzle2 = Puzzle_h2("*32415678", "*12345678")

    result4 = astar_search(puzzle2)
    print(result1.solve())
    result5 = greedy_best_first_graph_search(puzzle2)
    print(result2.solve())
    result6 = recursive_best_first_search(puzzle2)
    print(result3.solution())