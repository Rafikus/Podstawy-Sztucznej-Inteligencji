import random
class Perceptron:
    def __init__(self, inputCount):
        self.weights = []
        self.step = 0.01
        for n in range(inputCount):
            self.weights.append(random.uniform(-1,1))

    def FeedForward(self, inputs):
        sigma = 0
        for i, e in enumerate(inputs):
            sigma += e * self.weights[i]
        return self.Activate(sigma)

    def Activate(self, sigma):
        if sigma > 0:
            return 1
        else:
            return - 1

    def Train(self, inputs, desired):
        guess = self.FeedForward(inputs)
        errorDelta = desired - guess
        for i, w in enumerate(self.weights):
            self.weights[i] += errorDelta * inputs[i] * self.step
