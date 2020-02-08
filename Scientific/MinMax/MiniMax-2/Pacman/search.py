# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s, s, w, s, w, w, s, w]

class SearchNode:
    def __init__(self, stateTuple, previousNode):
        self.stateData = stateTuple
        self.prev = previousNode
    
    def fullActionInfo(self):
        return self.stateData
    
    def stateInfo(self):
        return self.stateData[0]
    
    def directionToReach(self):
        return self.stateData[1]
    
    def cost(self):
        return self.stateData[2]

    def previousNode(self):
        return self.prev

def graphSearch(problem, queueingStructure):   
    covered = set([])
    
    firstTuple = (problem.getStartState(), 'Stop', 0)
    startNode = SearchNode(firstTuple, None)
    
    queueingStructure.push(startNode)
    covered.add(startNode.stateInfo())
    
    while not queueingStructure.isEmpty():
        n = queueingStructure.pop()
       
        if problem.isGoalState(n.stateInfo()):
            searchResult = []
            while True:
                if n.previousNode() is None: break
                searchResult.append(n.directionToReach())
                n = n.previousNode()
            searchResult.reverse()
            return searchResult
        
        for sTuple in problem.getSuccessors(n.stateInfo()):
            if not (sTuple[0] in covered):
                queueingStructure.push(SearchNode(sTuple, n))
                covered.add(sTuple[0])
        
    return []
        
    
def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  Start: (34, 16)
  Is the start a goal? False
  Start's successors: [((34, 15), 'South', 1), ((33, 16), 'West', 1)]
  """
  stack = util.Stack()
  results = graphSearch(problem, stack)
  return results

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  queue = util.Queue()
  results = graphSearch(problem, queue)
  return results
      
def getNodeCost(searchNode):
    if searchNode == None:
        return 0;
    
    return searchNode.cost() + getNodeCost(searchNode.previousNode())

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  priorityQueue = util.PriorityQueueWithFunction(getNodeCost)
  results = graphSearch(problem, priorityQueue)
  return results

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0
  
def aStarPriorityFunction(problem, node, heuristic):
    currentValue = getNodeCost(node) + heuristic(node.stateInfo(), problem)
    return currentValue

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  priorityQueue = util.PriorityQueueWithFunction(lambda node: aStarPriorityFunction(problem, node, heuristic))
  results = graphSearch(problem, priorityQueue)
  return results
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
