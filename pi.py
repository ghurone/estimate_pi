from random import uniform

import matplotlib.pyplot as plt


def colors(n):  # n = Number of points
    r = 1
    d = {}

    for i in range(n):
        x = uniform(-r, r)  # point value on the x axis
        y = uniform(-r, r)  # point value on the y axis

        square_distance = x ** 2 + y ** 2

        if square_distance <= r ** 2:  # testing the points
            d[(x, y)] = 'red'
        else:
            d[(x, y)] = 'blue'

    return d


def pi(dic):
    n_circle = 0

    for i, v in enumerate(dic):
        if dic[v] == 'red':
            n_circle += 1

    return 4 * n_circle / len(dic.values())


z = colors(100000)
f = plt.scatter(*zip(*z.keys()), c=z.values(), s=0.5)
plt.show()
