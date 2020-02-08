def find_closest_dot(gameState):
    queue = [gameState]
    dis = dict()
    dis[gameState.getPacmanPosition()] = 0
    number_of_food = gameState.getFood()
    while queue:
        x = queue[0]
        if x.getFood() != number_of_food:
            return dis[x.getPacmanPosition()]
        queue = queue[1:]
        for action in x.getLegalActions(0):
            nextState = x.generateSuccessor(0, action)
            if nextState.getPacmanPosition() not in dis:
                dis[nextState.getPacmanPosition()] = dis[x.getPacmanPosition()] + 1
                queue.append(nextState)

    return float('inf')
