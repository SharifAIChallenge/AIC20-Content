from util import manhattanDistance
from game import Directions
from MinimaxAgentEvalUtil import minimaxAgentEval
def minimaxAgentAction(agent, gameState):
    agent.depth = 2
    maxValue = float("-inf")
    maxAction = Directions.STOP
    for action in gameState.getLegalActions(0):
        nextState = gameState.generateSuccessor(0, action)
        nextValue = getValue(agent, nextState, 0, 1)
        if nextValue > maxValue:
            maxValue = nextValue
            maxAction = action
    return maxAction

def getValue(agent, gameState, currentDepth, agentIndex):
    if currentDepth == agent.depth or gameState.isWin() or gameState.isLose():
        return minimaxAgentEval(gameState)
    elif agentIndex == 0:
        return maxValue(agent, gameState,currentDepth)
    else:
        return minValue(agent, gameState,currentDepth,agentIndex)

def maxValue(agent, gameState, currentDepth):
    maxValue = float("-inf")
    for action in gameState.getLegalActions(0):
        maxValue = max(maxValue, getValue(agent, gameState.generateSuccessor(0, action), currentDepth, 1))
    return maxValue

def minValue(agent, gameState, currentDepth, agentIndex):
    minValue = float("inf")
    for action in gameState.getLegalActions(agentIndex):
        if agentIndex == gameState.getNumAgents()-1:
            minValue = min(minValue, getValue(agent, gameState.generateSuccessor(agentIndex, action), currentDepth+1, 0))
        else:
            minValue = min(minValue, getValue(agent, gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex+1))
    return minValue
