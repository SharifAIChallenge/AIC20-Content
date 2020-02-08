import util
def reflexAgentEval(reflexAgent, currentGameState, action):
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    if successorGameState.isWin():
        return float("inf")

    for ghostState in newGhostStates:
        if util.manhattanDistance(ghostState.getPosition(), newPos) < 2 and ghostState.scaredTimer < 3:
            return float("-inf")

    foodDist = []
    for food in list(newFood.asList()):
        foodDist.append(util.manhattanDistance(food, newPos))

    foodSuccessor = 0
    if (currentGameState.getNumFood() > successorGameState.getNumFood()):
        foodSuccessor = 300

    return successorGameState.getScore() - 5 * min(foodDist) + foodSuccessor
