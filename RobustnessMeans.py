"""A mean calculation.

Compute the mean calculation of a solution grouped by perturbation factors
and write results into Solutions/[Model]/Robustness[Model]Means.txt.

  Typical usage example:

  python3 RobustnessMean.py
"""

import os
from statistics import mean

meanValues10 = []
meanTimes10 = []
meanValues20 = []
meanTimes20 = []
meanValues50 = []
meanTimes50 = []
meanValues75 = []
meanTimes75 = []
meanValues100 = []
meanTimes100 = []

directory = 'RMIKP'

for filename in os.listdir('Solutions/' + directory):

    file = open('Solutions/' + directory + '/' + filename, "r")
    content = file.read()
    data = content.splitlines()

    names = []
    values = []
    times = []
    items = []

    for item in data:
        names.append(item.split('|')[0])
        values.append(float(item.split('|')[1]))
        times.append(float(item.split('|')[2]))
        items.append(item.split('|')[3])

    if '_10%_' in filename:
        meanValues10.append(mean(values))
        meanTimes10.append(mean(times))

    if '_20%_' in filename:
        meanValues20.append(mean(values))
        meanTimes20.append(mean(times))

    if '_50%_' in filename:
        meanValues50.append(mean(values))
        meanTimes50.append(mean(times))

    if '_75%_' in filename:
        meanValues75.append(mean(values))
        meanTimes75.append(mean(times))

    if '_100%_' in filename:
        meanValues100.append(mean(values))
        meanTimes100.append(mean(times))

f = open("Solutions/RMIKP/RobustnessMixedIntegerMeans.txt", "a")

f.write(str(10) + '%' + '|' + str(mean(meanValues10)) + '|' + str(mean(meanTimes10)) + '\n')
f.write(str(20) + '%' + '|' + str(mean(meanValues20)) + '|' + str(mean(meanTimes20)) + '\n')
f.write(str(50) + '%' + '|' + str(mean(meanValues50)) + '|' + str(mean(meanTimes50)) + '\n')
f.write(str(75) + '%' + '|' + str(mean(meanValues75)) + '|' + str(mean(meanTimes75)) + '\n')
f.write(str(100) + '%' + '|' + str(mean(meanValues100)) + '|' + str(mean(meanTimes100)) + '\n')
