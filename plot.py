from math import exp, pi
import matplotlib.pyplot as plt
from pi import desv_pad


def plot(di, p, n, li):
    med = sum(li) / len(li)

    fig, ax = plt.subplots(1, 2, figsize=(12.8, 6.4))  # matriz 1x2 de plots

    # gráfico de dispersão na primeira figura
    ax1 = ax[0]
    ax1.add_artist(plt.Circle((0, 0), radius=1, lw=0.5, fill=False))  # adiciona círculo
    ax1.add_artist(plt.Rectangle((-1, -1), 2, 2, lw=0.5, fill=False))  # adiciona quadrado
    ax1.scatter(*zip(*di.keys()), c=di.values(), s=0.5)  # scatter plot
    # montando o sistema de coordenadas cartesianas
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

    # histograma na segumda figura
    ax2 = ax[1]
    ax2.hist(li, bins=50, color='#00ffcc')
    ax2.axvline(med, color='k', ls='dashed', lw=0.7)  # plota a linha na média do histograma
    # texto na linha da média
    min_ylim, max_ylim = plt.ylim()
    ax2.text(med * 1.001, max_ylim * 0.95, f'Média: {med:.5f}', size=12)
    # título
    ax2.set_title(f'Histograma para {n} estimativas de pi\nde {p} pontos cada (ex: plot à esquerda)')
    # gaussiana
    dp = desv_pad(li, med)
    sorted_list = sorted(li)
    y = [(exp(-0.5 * ((x - med) / dp) ** 2)) / (dp * (2 * pi) ** 0.5) for x in sorted_list]
    ax2.plot(sorted_list, y, color='k', lw=0.7)

    plt.show()
