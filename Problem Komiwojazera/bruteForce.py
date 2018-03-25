import math
import matplotlib.pyplot as plt
import random
import itertools

cityCount = 9

cities = [random.sample(range(100), 2) for x in range(cityCount)]
allTours = list(itertools.permutations(random.sample(range(cityCount), cityCount), cityCount))
distance = [0] * allTours.__len__()
for i in range(cityCount):
    for j in range(allTours.__len__()):
        distance[j] += math.sqrt(
            math.pow((cities[allTours[j][i % cityCount]][0] - cities[allTours[j][(i + 1) % cityCount]][0]), 2) +
            math.pow((cities[allTours[j][i % cityCount]][1] - cities[allTours[j][(i + 1) % cityCount]][1]), 2))
print(allTours)
print(distance)
for i in range(distance.__len__()):
    if (i == 0):
        shortest = distance[i]
        index = i
    if (distance[i] < shortest):
        shortest = distance[i]
        index = i

plt.plot(list(zip(*[cities[allTours[index][i % cityCount]] for i in range(cityCount + 1)]))[0],
         list(zip(*[cities[allTours[index][i % cityCount]] for i in range(cityCount + 1)]))[1], 'xb-', )
plt.show()
