"""A representation of the Decoupling Branch & Bound Algorithm for the Robust Knapsack Problem.

Run the Decoupling Branch & Bound Algorithm for the Robust Knapsack Problem with instances found in Instances/
and write results into Branch&BoundRobustKnapsackSolution.txt.

  Typical usage example:

  python3 Branch&BoundRobustKnapsackModel.py
"""

import random
import os
import warnings
import time


class Node:
    """Classic Node class.

      Attributes:
          level: An integer count of the level of the Node.
          profit: An integer count of the profit of the Node.
          bound: An integer count of the bound of the Node.
          weight: An integer count of the weight of the Node.
      """

    def __init__(self, level, profit, bound, weight):
        """Inits Node"""
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

    def comp(self, a, b):
        """Compare the value per weight of two Nodes."""
        r1 = a.value / a.weight
        r2 = b.value / b.weight
        return r1 > r2

time_start = time.perf_counter()

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore")

counter = 0

for filename in os.listdir('Instances'):

    solList = []
    solIdList = []
    solTimeList = []

    for i in range(100):

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
        tmp = random.sample(range(numberOfItems), Gamma)
        tmp = [i + 1 for i in tmp]
        for i in range(len(r)):
            if i not in tmp:
                r[i] = 0

        del r[0]

        x = {index[i]: v[i + 1] / (w[i + 1] + r[i + 1]) for i in range(len(v))}
        x = sorted(x.items(), key=lambda x: x[1], reverse=True)

        Q = []
        dummyNode = Node(-1, 0, 0, 0)
        print(type(dummyNode))
        tmp = Node(0, 0, 0, 0)
        Q.append(dummyNode)
        maxProfit = 0


        def bound(u):
            """Compute the bound of a given Node.

               Compute the profit of a given Node without by taking into account the profits of partial items.

                Args:
                  u:
                    A Node.
                  keys:

                Returns:
                  The bound of u.
                """

            if u.weight >= capacityOfKnapsack:
                return 0

            profitBound = u.profit

            counter = u.level + 1
            totw = u.weight

            while counter < numberOfItems and totw + w[counter+1] <= capacityOfKnapsack:

                totw = totw + w[counter+1]
                profitBound = profitBound + v[counter+1]

                counter = counter + 1

            if counter < numberOfItems:
                profitBound = profitBound + (capacityOfKnapsack - totw) * v[counter+1]/w[counter+1]

            return profitBound


        while len(Q) != 0:

            u = Q[0]
            Q.pop(0)

            if u.level == -1:
                tmp.level = 0

            if u.level == numberOfItems-1:
                break
            else:
                tmp.level = u.level + 1

            tmp.weight = u.weight + w[x[tmp.level][0]]
            tmp.profit = u.profit + v[x[tmp.level][0]]

            if tmp.weight <= capacityOfKnapsack and tmp.profit > maxProfit:
                maxProfit = tmp.profit
                solId.append(x[tmp.level][0])

            tmp.bound = bound(tmp)

            if tmp.bound > maxProfit:
                Q.append(tmp)

            tmp.weight = u.weight
            tmp.profit = u.profit
            tmp.bound = bound(tmp)
            if tmp.bound > maxProfit:
                Q.append(tmp)

        sol = 0
        for i in solId:
            sol = sol + v[i]

        time_elapsed = (time.perf_counter() - time_start)

        solIdList.append(solId)
        solList.append(sol)
        solTimeList.append(time_elapsed)

    avgSol = sum(solList) / len(solList)
    maxSol = max(solList)
    maxIdSol = solIdList[solList.index(maxSol)]
    avgTimeSol = sum(solTimeList) / len(solTimeList)

    f = open("Branch&BoundRobustKnapsackSolution.txt", "a")
    f.write(str(filename) + '|' + str(avgSol) + '|' + str(maxSol) + '|' + str(avgTimeSol) + '|' + str(maxIdSol) + '\n')

    counter = counter + 1
    print(counter)
