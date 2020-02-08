import random
def reflexAgentAction(reflexAgent, gameState):
    legalMoves = gameState.getLegalActions()
    # Choose one of the best actions
    scores = [reflexAgent.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
    return legalMoves[chosenIndex]
