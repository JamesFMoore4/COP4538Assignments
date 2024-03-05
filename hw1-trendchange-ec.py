# James Moore 

import matplotlib.pyplot as plt
import numpy as np

# Identifies trend change points in an array and prints them
# First two values in the array are skipped, as they cannot be trend points
# Next values are compared to the previous two values and are appended to another array if conditions are met
# Trend points are then printed according to the example given in HW1.pdf (two values printed for every change in the
# trend)
def Trendchange(numbers):
    trend_points = []
    for i in range(len(numbers)):
        if i ==0:
            continue
        elif i > 0:
            if i -1 == 0:
                continue
            else:
                if numbers[i] > numbers[i-1]  and numbers[i-1] < numbers[i-2]:
                    if numbers[i-1] not in trend_points:
                        trend_points.append(numbers[i - 1])
                    if numbers[i] not in trend_points:
                        trend_points.append(numbers[i])

                elif numbers[i] < numbers[i-1] and numbers[i-1] > numbers[i-2]:
                    if numbers[i - 1] not in trend_points:
                        trend_points.append(numbers[i - 1])
                    if numbers[i] not in trend_points:
                        trend_points.append(numbers[i])

                else:
                    continue

    print("Trend change points: ", end=" ")
    for i in trend_points:
        print(str(i), end=" ")

    # matplotlib and numpy used here to plot data points by array index
    # trend points are plotted in red to highlight where a trend change occurs
    # this is accomplished by the use of two additional arrays to determine where each point needs to be plotted
    trend = np.array(trend_points)
    orig_array = np.array(numbers)
    x_points1 = []
    x_points2 = []
    for i in range(len(orig_array)):
        x_points1.append(i)
        if orig_array[i] in trend:
            x_points2.append(i)
    for j in range(len(trend)):
        plt.plot(x_points2[j], trend[j], "ro")
    plt.plot(x_points1, orig_array)
    plt.show()

def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
         values.append(int(value))
    return values




numbers = read()

Trendchange(numbers)





