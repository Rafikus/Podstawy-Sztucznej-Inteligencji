import numpy.random as nprnd
import numpy as npy
import random
from tkinter import *
import time

mutationProbability = 0.03
crossProbability = 0.2
populationCount = 400
population = nprnd.randint(0, 255, size=populationCount)

def genetyka(_population=[]):
    newPopulation = []
    for num in _population:
        rouletteIndex = roulette(population, grades)
        newPopulation.append(population[rouletteIndex])
    return newPopulation


def ocenaPrzystosowania(_population=[]):
    grades = []
    for pop in _population:
        grades.append(activate(pop))
    return grades


def activate(x):
    return 2 * (x * x + 1)


def cross(_population=[]):
    pairs = [random.sample(range(100), 2) for x in _population]
    for pair in pairs:
        if nprnd.ranf() < crossProbability:
            locus = nprnd.randint(0, 4)
            num1 = npy.unpackbits(npy.array([pair[0]], dtype=npy.uint8))
            num2 = npy.unpackbits(npy.array([pair[1]], dtype=npy.uint8))
            newnum1 = []
            newnum2 = []

            for i in range(0, locus):
                newnum1.append(num1[i])
                newnum2.append(num2[i])
            for i in range(locus, 8):
                newnum1.append(num2[i])
                newnum2.append(num1[i])
            for bit in newnum1:
                pair[0] = (pair[0] << 1) | bit
            for bit in newnum2:
                pair[1] = (pair[1] << 1) | bit


def roulette(_population=[], _grades=[]):
    sumOfGrades = 0
    sum = 0
    for grade in _grades:
        sumOfGrades += grade
    field = nprnd.randint(0, sumOfGrades, size=1)
    for grade in _grades:
        sum += grade
        if sum > field:
            return _grades.index(grade)


def mutation(_population=[]):
    newPopulation = []
    for num in _population:
        if nprnd.ranf() < mutationProbability:
            locus = nprnd.randint(0, 8)
            num1 = npy.unpackbits(npy.array([num], dtype=npy.uint8))

            newnum = []

            if num1[locus] == 1:
                num1[locus] = 0
            else:
                num1[locus] = 1
            for i in range(0, 8):
                newnum.append(num1[i])
            num = 0
            for bit in newnum:
                num = (num << 1) | bit
            print(newnum)
        newPopulation.append(num)
    return newPopulation


root = Tk()
root.title("Algorytm Genetyczny, wykonanie Rafał Kusy")

# Canvas

canvas = Canvas(root)

mainframe = Frame(root)
mainframe.grid(column=100, row=populationCount, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
j = 0

labels = []

for i in range(populationCount):
    if i % 50 == 0:
        j += 3
    label1 = Label(mainframe);
    label1.grid(column=j, row=i%50, sticky=W)
    label2 = Label(mainframe);
    label2.grid(column=j+1, row=i % 50, sticky=W)
    label3 = Label(mainframe);
    label3.grid(column=j+2, row=i % 50, sticky=W)
    labels.append([label1, label2, label3])
print(labels[0])
while True:
    population.sort()
    grades = ocenaPrzystosowania(population)
    i = 0
    j = 0
    for num in population:
        if i % 50 == 0:
            j += 3
        labels[i][0].configure(text=npy.binary_repr(num, width=8))
        labels[i][1].configure(text=grades[i])
        labels[i][2].configure(text="   ", bg='#%02x%02x%02x' % (num, num, num))
        i = i + 1
    population = genetyka(population)
    cross(population)
    population = mutation(population)
    canvas.update()
    time.sleep(1/10)
