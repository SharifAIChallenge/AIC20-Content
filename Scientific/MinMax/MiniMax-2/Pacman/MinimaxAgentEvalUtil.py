import util
from bfs import find_closest_dot
def minimaxAgentEval(gameState):
    pos = gameState.getPacmanPosition()
    ghostStates = gameState.getGhostStates()
    # scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]

    if gameState.isWin():
        return float("inf")

    for ghostState in ghostStates:
        if util.manhattanDistance(ghostState.getPosition(), pos) < 2 and ghostState.scaredTimer < 3:
            return float("-inf")

    foodDist = find_closest_dot(gameState)
    return gameState.getScore() - 1000 * foodDist - 5000000*gameState.getNumFood()

