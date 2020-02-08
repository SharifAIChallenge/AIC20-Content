from util import manhattanDistance
from game import Directions
from MinimaxAgentEvalUtil import minimaxAgentEval

def alphaBetaAgentAction(agent, gameState):

    maxValue = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    maxAction = Directions.STOP
    for action in gameState.getLegalActions(0):
        nextState = gameState.generateSuccessor(0, action)
        nextValue = getValue(agent, nextState, 0, 1, alpha, beta)
        if nextValue > maxValue:
            maxValue = nextValue
            maxAction = action
        alpha = max(alpha, maxValue)
    return maxAction

def getValue(agent, gameState, currentDepth, agentIndex, alpha, beta):
    if currentDepth == agent.depth or gameState.isWin() or gameState.isLose():
        return minimaxAgentEval(gameState)
    elif agentIndex == 0:
        return maxValue(agent, gameState,currentDepth,alpha,beta)
    else:
        return minValue(agent, gameState,currentDepth,agentIndex,alpha,beta)

def maxValue(agent, gameState, currentDepth, alpha, beta):
    maxValue = float("-inf")
    for action in gameState.getLegalActions(0):
        maxValue = max(maxValue, getValue(agent, gameState.generateSuccessor(0, action), currentDepth, 1, alpha, beta))
        if maxValue > beta:
            return maxValue
        alpha = max(alpha, maxValue)
    return maxValue

def minValue(agent, gameState, currentDepth, agentIndex, alpha, beta):
    minValue = float("inf")
    for action in gameState.getLegalActions(agentIndex):
        if agentIndex == gameState.getNumAgents()-1:
            minValue = min(minValue, getValue(agent, gameState.generateSuccessor(agentIndex, action), currentDepth+1, 0, alpha, beta))
        else:
            minValue = min(minValue, getValue(agent, gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex+1, alpha, beta))
        if minValue < alpha:
            return minValue
        beta = min(beta, minValue)
    return minValue
