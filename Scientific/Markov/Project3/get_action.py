def get_action(self, state):
    is_random = util.flipCoin(self.epsilon)
    if is_random:
        return random.choice(mdp.getPossibleActions(state))
    else:
        return self.computeActionFromQValues(self, state)