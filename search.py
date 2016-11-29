"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def graphSearch(problem, fringe):
    closed = []
    fringe.push(Node(None,problem.getStartState(), "Stop", 0))
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node.state):
            action = []
            while node.parent is not None:
                action.append(node.action)
                node = node.parent
            action.reverse()
            return action
        if node.state not in closed:
            closed.append(node.state)
            for something in expand(node, problem):
                fringe.push(something)
    print "FAIL"
    return []


def expand(node, problem):
    successors = []
    for succ in problem.getSuccessors(node.state):
        successors.append(Node(node, succ[0], succ[1], succ[2] + node.pathCost))
    return successors


class Node:
    def __init__(self, parent, state, action, pathCost):
        self.parent = parent
        self.state = state
        self.action = action
        self.pathCost = pathCost
    def displayAll(self):
        return self.state, self.parent, self.action, self.pathCost

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    return graphSearch(problem, fringe)
    """util.raiseNotDefined()"""


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    return graphSearch(problem, fringe)
    #util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def priorityFunction(node):
        return node.pathCost
    fringe = util.PriorityQueueWithFunction(priorityFunction)
    return graphSearch(problem, fringe)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def priorityFunction(node):
        #return node.pathCost + searchAgents.manhattanHeuristic(node.state, problem)
        return node.pathCost + heuristic(node.state, problem)
    fringe = util.PriorityQueueWithFunction(priorityFunction)
    return graphSearch(problem, fringe)
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
