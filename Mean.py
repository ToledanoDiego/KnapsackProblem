"""A mean calculation.

Compute the mean calculation of a solution
and write results into Solutions/[Model]/Gamma[Model]Means.txt.

  Typical usage example:

  python3 Mean.py
"""

import os
from statistics import mean

meanValues = []
meanTimes = []

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

    meanValues.append(mean(values))
    meanTimes.append(mean(times))

    f = open("Solutions/RMIKP/RobustMixedIntegerMeans.txt", "a")
    f.write(str(filename) + '|' + str(mean(values)) + '|' + str(mean(times)) + '\n')
