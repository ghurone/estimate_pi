import random


def pi(n):  # n = Number of points
    n_circle = 0   
    r = 1  # radius value

    for i in range(n):
        x = random.uniform(0, r)  # point value on the x axis
        y = random.uniform(0, r)  # point value on the y axis

        square_distance = x ** 2 + y ** 2

        if square_distance <= r**2:  # testing the points
            n_circle += 1

    return 4 * n_circle / n
