import copy
from queue import Queue,PriorityQueue
from collections import deque # for stack
import random
#from queue import Queue
class states:
    #goal_state=[0,1,2,3,4,5,6,7,8]
    def __init__(self, representation):
        self.representation = representation

    def slide_left(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 3 or empty_space == 6:
            return new_state
        else:
            new_state.representation[empty_space - 1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space - 1]
            return new_state

    def slide_right(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 2 or empty_space == 5 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+1]
            return new_state

    def slide_up(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 1 or empty_space == 2:
            return new_state
        else:
            new_state.representation[empty_space-3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space-3]
            return new_state

    def slide_down(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 6 or empty_space == 7 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+3]
            return new_state

    def print_board(self):
        for i in range(len(self.representation)):
            if i%3 ==0:
                print('\n', end=' ')
            print(self.representation[i], end=' ')
        print('\n\n\n')

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.slide_left(), self.slide_right(), self.slide_up(), self.slide_down()]

def BFS(start_state, goal_state):

    queue = Queue() #using built-in queue
    explored = []
    queue.put(start_state) #pushing the start state into queue
    while queue:
        path = queue.get() #dequeue node and put into the path
        explored.append(path)
        entity = states(path) #make the object of class states
        leaves = entity.applyOperators() #generating the child

        if path == goal_state: #checkin' if it is the goal node
            return explored

        for child in leaves:
            if (child.representation != path):
                queue.put(child.representation) #updating

def DFS(start_state, goal_state):

    stack = deque()
    stack.append(start_state)
    explored=[]
    while stack:
        path = stack.pop()
        explored.append(path)
        entity = states(path)
        leaves = entity.applyOperators()

        if path == goal_state:
            return explored

        for child in leaves:
            if child.representation != path:
                stack.append(child.representation)

def RANDOM_HEURISTIC():
    return random.randint(1,30)
def Greedy(start, goal):
    fringe = PriorityQueue()  # setting my fringe as a priority queue
    heur = RANDOM_HEURISTIC() #generating random heuristics
    fringe.put((heur, start))  # (heuristic, root)  #random heuristic to start
    explored = []  # for explored node

    while fringe:
        greedyH, current_node = fringe.get()  # starting cost,start state
        explored.append(current_node)  # appending in explored queue to keep the track of explored node

        if current_node == goal:  # goal test
            return explored
        entity = states(current_node)
        child = entity.applyOperators()

        for leaves in child:  # generate child
            if leaves.representation not in explored:  # always check the node, beacuse we dont explored the node again
                h_value = RANDOM_HEURISTIC()
                fringe.put((h_value, leaves.representation))

def IDS(start, end):
    depth = 0
    while True:
        result = DLS(start, end, depth)
        if result == end:
            return result
        depth = depth + 1

def DLS(node, end, depth):
    if depth == 0 and node == end:
        return node
    elif depth>0:
        entity = states(node)
        child = entity.applyOperators()
        for leaves in child:
            if end == DLS(leaves.representation, end, depth - 1):
                return end


start_state = [2,8,3,1,6,4,7,0,5]

while True:
    print('MENU:')
    q1=('1. What is the current representation of the 8 puzzle problem?')
    #q2=('2. What is the goal representation you wish to achieve?')
    q3=('2.Please press 2 for entering the algorithm you want to use for the search?\n')

    print(q1)
    print(q3)
    question=input('Please select the given options(Enter 1,2:)')

    if question=='1':
        obj=states(start_state)
        print('The current representation of the 8 puzzle problem is:')
        obj.print_board()


    elif question=='2':
        a = list(map(int, input("\nEnter the goal state you wish to achieve : ").strip().split()))[:9] #using map function
        print("\nThe goal state you entered is :")
        obj1=states(a)
        obj1.print_board()

########################################################################################################

        aa = input('Enter BFS,DFS,IDS,or GREEDY\n')
        count = 0
        if aa == 'BFS':
            print('******BREADTH FISRT SEARCH ALGORITHM******')
            Final=BFS(start_state, a)

            # obj = states(Final)
            for explorr in Final:
                count+=1
                obj3=states(explorr)
                obj3.print_board()
            print('The no. of explored nodes are:',count)

            # obj.print_board()
        elif aa == 'DFS':
            print('******DEPTH FISRT SEARCH ALGORITHM******')
            Final=DFS(start_state, a)
            #obj = states(Final)

            for explorrr in Final:
                count+=1
                obj4=states(explorrr)
                obj4.print_board()
            #obj.print_board()
            print('The no. of explored nodes are:', count)

        elif aa == 'GREEDY':
            print('******GREEDY BREADTH FISRT SEARCH ALGORITHM******')
            Final=Greedy(start_state, a)
            #obj = states(Final)

            for explorrr in Final:
                count+=1
                obj5=states(explorrr)
                obj5.print_board()
            #obj.print_board()
            print('The no. of explored nodes are:', count)

        elif aa == 'IDS':
            print('******ITERATIVE DEEPINING SEARCH ALGORITHM******')
            Final=IDS(start_state, a)
            obj6 = states(Final)
            # for explorrrr in Final:
            #     count+=1
            #     obj6=states(explorrrr)
            #     obj6.print_board()
            obj6.print_board()
            #print('The no. of explored nodes are:', count)


    r=(input('Do you want to go back to menu?if yes then press y else n'))
    if r!='y':
        break


# goal_state = [2,8,3,1,6,4,7,5,0] #this goal state takes time in execution
# Final=(start_state, goal_state)
# #print(Final)
# obj=states(Final)
# obj.print_board()








