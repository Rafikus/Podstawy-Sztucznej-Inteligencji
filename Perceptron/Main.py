import random
import matplotlib.pyplot as plt
import Perceptron
import Inputs

def f(x):
    return x + 1

def Set(width, height, pointCount):
    set = []
    for i in range(pointCount):
        x = random.uniform(-width, width)
        y = random.uniform(-height, height)
        answer = 1
        if y < f(x):
            answer = -1
        set.append(Inputs.Inputs(x,y,answer))
    return set

if __name__ == '__main__':
    _width = 500
    _height = 1000
    _trainingPoints = 700
    _testingPoints = 250

    training = Set(_width, _height, _trainingPoints)
    testing = Set(_width, _height, _testingPoints)
    perceptron = Perceptron.Perceptron(3)

    score = []
    for t in training:
        perceptron.Train(t.inputs, t.answer)

    data_ones_x = []
    data_ones_y = []

    data_minusones_x = []
    data_minusones_y = []

    for t in testing:
        guess = perceptron.FeedForward(t.inputs)
        if guess > 0:
            data_ones_x.append(t.inputs[0])
            data_ones_y.append(t.inputs[1])
        else:
            data_minusones_x.append(t.inputs[0])
            data_minusones_y.append(t.inputs[1])

        correct = 1
        if t.inputs[1] < f(t.inputs[0]):
            correct = -1

        if guess == correct:
            score.append(1)
        else:
            score.append(0)

    print("Score:", sum(score), "/", len(score), "(" + str((float(sum(score))/float(len(score)))*100) + "% accuracy)")

#Plot the true classification line
    xMin = -_width
    xMax = _width
    yMin = f(xMin)
    yMax = f(xMax)
    plt.plot([xMin, xMax], [yMin, yMax], linestyle='-', linewidth=1, color='#6dbe1b')

    axes = plt.gca()
    axes.set_xlim([xMin, xMax])
    axes.set_ylim([yMin/2, yMax/2])

#Plot 1 & -1 scores
    plt.scatter(data_ones_x, data_ones_y, marker='+', color='#1381be')
    plt.scatter(data_minusones_x, data_minusones_y, marker='.', color='#eb2352')
	
    fig = plt.gcf()
    fig.canvas.set_window_title('Perceptron Linear Classifier')
    plt.show()
	
