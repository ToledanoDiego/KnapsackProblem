"""A Pyomo representation of the Robust Mixed 0-1 Knapsack Problem.

Run the Integer Knapsack Problem with instances found in Instances/
and write results into RobustMixed0-1KnapsackSolution.txt.

  Typical usage example:

  python3 RobustMixed0-1KnapsackModel.py
"""

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
    r = {index[i]: nominalWeight[i] + 100 / 100 * nominalWeight[i] for i in range(len(index))}

    Gamma = int(100 / 100 * len(r))
    varSep = len(r) - Gamma

    xv = dict(list(v.items())[:varSep])
    yv = (list(v.items())[varSep:])
    for i in range(len(yv)):
        tmp = list(yv[i])
        tmp[0] = tmp[0] - varSep
        yv[i] = tmp
    yv = dict(yv)

    xw = dict(list(w.items())[:varSep])
    yw = (list(w.items())[varSep:])
    for i in range(len(yw)):
        tmp = list(yw[i])
        tmp[0] = tmp[0] - varSep
        yw[i] = tmp
    yw = dict(yw)

    xr = dict(list(r.items())[:varSep])
    yr = (list(r.items())[varSep:])
    for i in range(len(yr)):
        tmp = list(yr[i])
        tmp[0] = tmp[0] - varSep
        yr[i] = tmp
    yr = dict(yr)

    M = ConcreteModel()  # Pyomo.

    M.ITEMS = Set(initialize=xv.keys())
    M.x = Var(M.ITEMS, within=pmo.Binary)
    M.ITEMSy = Set(initialize=yv.keys())
    M.y = Var(M.ITEMSy, within=pmo.NonNegativeReals)

    def ObjRule(M):
        """Objective function."""
        return pyo.sum_product(M.x, xv, index=xv) + pyo.sum_product(M.y, yv, index=yv)


    def ConRule(M):
        """Constrain function."""
        return pyo.sum_product(M.x, xw, index=xw) + pyo.sum_product(M.y, yr, index=yr) <= capacityOfKnapsack

    M.value = Objective(rule=ObjRule, sense=maximize)
    M.weight = Constraint(rule=ConRule)

    S = pyo.SolverFactory('cplex')

    results = S.solve(M)

    sol = 0

    for i in M.component_objects(Var, active=True):

        for index in i:
            if str(i) == 'x':
                if i[index].value > 0:
                    sol = sol + i[index].value * v[index + Gamma]
                    solId.append(str(index + Gamma) + ' * ' + str(i[index].value))
            if str(i) == 'y':
                if i[index].value > 0:
                    sol = sol + i[index].value * v[index]
                    solId.append(str(index) + ' * ' + str(i[index].value))

    time_elapsed = (time.perf_counter() - time_start)

    f = open("RobustMixed0-1KnapsackSolutions.txt", "a")
    f.write(str(filename) + '|' + str(sol) + '|' + str(time_elapsed) + '|' + str(("[{0}]".format(', '.join(map(str, solId))))) + '\n')

    counter = counter + 1
    print(counter)
