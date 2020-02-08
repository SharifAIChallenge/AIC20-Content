def qlearning_update(self, state, action, nextState, reward):
    estimatedQ = self.alpha * (reward + self.discount * self.computeValueFromQValues(nextState)) + (1-self.alpha)*self.qValues[(state,action)]
    self.qValues[(state,action)] = estimatedQ
    self.epsilon = (self.epsilon)*0.999
    self.alpha = (self.alpha*999+1)/1000
    print(self.epsilon)