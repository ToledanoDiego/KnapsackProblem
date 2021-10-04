"""A Pyomo representation of the 0-1 Knapsack Problem.

Run the 0-1 Knapsack Problem with instances found in Instances/ and write results into 0-1KnapsackSolution.txt.

  Typical usage example:

  python3 0-1KnapsackModel.py
"""

import random
import pyomo.environ as pyo
from pyomo.environ import *
import pyomo.kernel as pmo
import os
import warnings
import time

time_start = time.perf_counter()

print(type(time_start))

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

    M = ConcreteModel()  # Pyomo.

    M.ITEMS = Set(initialize=v.keys())
    M.x = Var(M.ITEMS, within=pmo.Binary)
    M.value = Objective(expr=sum(v[i] * M.x[i] for i in M.ITEMS), sense=maximize)
    M.weight = Constraint(expr=sum(w[i] * M.x[i] for i in M.ITEMS) <= capacityOfKnapsack)

    S = pyo.SolverFactory('cplex')

    results = S.solve(M)

    sol = 0

    for i in M.component_objects(Var, active=True):
        print(i)
        for index in i:

            sol = sol + i[index].value * v[index]
            if i[index].value > 0:
                solId.append(index)

    time_elapsed = (time.perf_counter() - time_start)

    f = open("0-1KnapsackSolutions.txt", "a")
    f.write(str(filename) + '|' + str(sol) + '|' + str(time_elapsed) + '|' + str(solId) + '\n')

    print(type(f))

    counter = counter + 1
    print(counter)
