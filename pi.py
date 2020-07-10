from random import uniform, choice
import matplotlib.pyplot as plt


def colors(n):  # n = Number of points
    r = 1
    d = {}

    color_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    dist = [r*k/len(color_list) if k != 0 else 0 for k in range(len(color_list), -1, -1)]

    for i in range(n):
        x = uniform(-r, r)  # point value on the x axis
        y = uniform(-r, r)  # point value on the y axis

        square_distance = x ** 2 + y ** 2

        if square_distance <= r ** 2:  # testing the points
            for j in range(len(dist)):
                if dist[j] >= square_distance >= dist[j + 1]:
                    d[(x, y)] = color_list[j]
                    break
        else:
            d[(x, y)] = 'silver'

    return d


def pi(dic):
    n_circle = 0

    for i, v in enumerate(dic):
        if dic[v] == 'red':
            n_circle += 1

    return 4 * n_circle / len(dic.values())


def plot_circle(p):
    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(*zip(*p.keys()), c=p.values(), s=0.5)
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.arrow(0, 0, 1.05, 0, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax.arrow(0, 0, 0, 1.05, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax.set_xlabel('x')
    ax.set_xticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax.xaxis.set_label_coords(0.993, 0.48)
    ax.set_ylabel('y', rotation=0)
    ax.set_yticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax.yaxis.set_label_coords(0.477, 0.98)
    ax.tick_params(labelsize=8)
    plt.show()


plot_circle(colors(100000))
