from searching_framework.utils import Problem
from searching_framework.informed_search import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8,6]

    def successor(self, state):
        successors = dict()

        # d = -1 down
        # d = 1  up
        #(x,y,(x_o1, y_o1, d_o1), (x_o2, y_o2, d_o2))

        man_x, man_y = state[0], state[1]
        obstacle1 = list(state[2])
        obstacle2 = list(state[3])
        max_x, max_y = self.grid_size

        #precki
        if obstacle1[2] == 1: #up
            if obstacle1[1] == max_y - 1:
                obstacle1[2] = -1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else: #down
            if obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1
        if obstacle2[2] == 1: #up
            if obstacle2[1] == max_y - 1:
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else: #down
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1
                #obstacle1 = (x,y,d)
        obstacles = [(obstacle1[0], obstacle1[1]), (obstacle2[0], obstacle2[1])]
        #covece
        #right x+1
        if man_x + 1 < max_x and (man_x+1, man_y) not in obstacles:
            successors["Right"] = (man_x+1, man_y, tuple(obstacle1), tuple(obstacle2))

        #left x-1
        if man_x - 1 >= 0 and (man_x-1, man_y) not in obstacles:
            successors["Left"] = (man_x-1, man_y, tuple(obstacle1), tuple(obstacle2))

        #up y+1
        if man_y + 1 < max_y and (man_x, man_y+1) not in obstacles:
            successors["Up"] = (man_x, man_y+1, tuple(obstacle1), tuple(obstacle2))

        #down y-1
        if man_y - 1 >= 0 and (man_x, man_y-1) not in obstacles:
            successors["Down"] = (man_x, man_y-1, tuple(obstacle1), tuple(obstacle2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == goal[0] and \
            state[1] == goal[1]

    def h(self, node):
        x_man = node.state[0]
        y_man = node.state[1]
        x_house = self.goal[0]
        y_house = self.goal[1]

        return abs(x_man - x_house) + abs(y_man - y_house)


if __name__ == '__main__':
    init = (0,2)
    goal = (7,4)
    obstacle1 = (2,5,-1) #down
    obstacle2 = (5,0,1) # up
    #(x,y,(o1x,o1y,o1d),(o2x,ob2y,o2d))
    explorer = Explorer((init[0], init[1], obstacle1,
                         obstacle2), goal)

    result = astar_search(explorer)
    print(result.solution())

