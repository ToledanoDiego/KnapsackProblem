"""A representation of the Greedy Algorithm for the Knapsack Problem.

Run the Decoupling Branch & Bound Algorithm for the Robust Knapsack Problem with instances found in Instances/
and write results into Greedy0-1KnapsackSolution.txt.

  Typical usage example:

  python3 Greedy0-1KnapsackModel.py
"""

import random
import pyomo.environ as pyo
from pyomo.environ import *
import pyomo.kernel as pmo
import os
import warnings
import time

time_start = time.perf_counter()

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore")

counter = 0

for filename in os.listdir('Instances'):

    time_start = time.perf_counter()

    file = open('Instances/' + filename, "r")
    content = file.read()
    data = content.splitlines()

    index = []
    profit = []
    nominalWeight = []
    robustWeight = []
    solId = []

    numberOfItems = int(data[0])
    data.pop(0)
    capacityOfKnapsack = int(data[-1])
    data.pop(-1)

    for item in data:
        index.append(int(item.split()[0]) + 1)
        profit.append(int(item.split()[1]))
        nominalWeight.append(int(item.split()[2]))
        robustWeight.append(int(item.split()[3]))

    v = {index[i]: profit[i] for i in range(len(index))}
    w = {index[i]: nominalWeight[i] for i in range(len(index))}
    r = {index[i]: robustWeight[i] for i in range(len(index))}
    r = {index[i]: nominalWeight[i] + 100 / 100 * nominalWeight[i] for i in range(len(index))}

    Gamma = 0
    tmp = random.sample(range(numberOfItems), Gamma)
    tmp = [i + 1 for i in tmp]
    for i in range(len(r)):
        if i not in tmp:
            r[i] = 0

    x = {index[i]: profit[i]/nominalWeight[i] for i in range(len(index))}

    x = sorted(x.items(), key=lambda x: x[1], reverse=True)
    totw = 0

    while len(x) != 0 and totw < capacityOfKnapsack:
        if totw + w[x[0][0]] < capacityOfKnapsack:
            solId.append(x[0][0])
            totw = totw + w[x[0][0]]
            x.pop(0)
        else:
            break

    sol = 0
    for i in solId:
        sol = sol+v[i]

    time_elapsed = (time.perf_counter() - time_start)

    f = open("Greedy0-1KnapsackSolutions.txt", "a")
    f.write(str(filename) + '|' + str(sol) + '|' + str(time_elapsed) + '|' + str(solId) + '\n')

    counter = counter + 1
    print(counter)
