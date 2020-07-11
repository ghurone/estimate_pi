from random import uniform
import matplotlib.pyplot as plt


def colors(p):  # p = number of points
    r = 1  # radius value
    d = {}

    color_list = ['#E14E65', '#F98D52', '#EBE051', '#6DBB5B', '#5286DA', '#714EB3']
    dist = [r * k / len(color_list) if k != 0 else 0 for k in range(len(color_list), -1, -1)]

    for i in range(p):
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
        if dic[v] != 'silver':
            n_circle += 1

    return 4 * n_circle / len(dic.values())


def plot(di, p, n, li):
    """Plots both circle/square example scatter plot and histogram with pi value estimates"""
    mean = sum(li) / len(li)

    fig, ax = plt.subplots(1, 2, figsize=(12.8, 6.4))  # 1x2 matrix of plots

    # scatter plot for the left plot
    ax1 = ax[0]
    ax1.add_artist(plt.Circle((0, 0), radius=1, lw=0.5, fill=False))  # add circle
    ax1.add_artist(plt.Rectangle((-1, -1), 2, 2, lw=0.5, fill=False))  # add square
    ax1.scatter(*zip(*di.keys()), c=di.values(), s=0.5)  # scatter plot
    # creating the cartesian coordinate system
    ax1.spines['top'].set_color('none')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['left'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.arrow(0, 0, 1.05, 0, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax1.arrow(0, 0, 0, 1.05, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax1.set_xlabel('x', size=12)
    ax1.set_xticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax1.xaxis.set_label_coords(0.998, 0.488)
    ax1.set_ylabel('y', size=12, rotation=0)
    ax1.set_yticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax1.yaxis.set_label_coords(0.477, 0.98)
    ax1.tick_params(labelsize=10)
    # add pi text
    ax1.text(0.05, 1.02, f'Pi estimado para esse círculo: {pi(di)}', size=11)

    # histogram for the right plot
    ax2 = ax[1]
    ax2.hist(li, bins=50, color='#00ffcc')
    ax2.axvline(mean, color='k', ls='dashed', lw=0.7)  # plots the mean line
    # add text for the mean line
    min_ylim, max_ylim = plt.ylim()
    ax2.text(mean * 1.001, max_ylim * 0.95, f'Média: {mean:.5f}', size=12)
    # title
    ax2.set_title(f'Histograma para {n} estimativas de pi\nde {p} pontos cada (ex: plot à esquerda)')

    plt.show()
