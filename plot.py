from math import exp, pi
import matplotlib.pyplot as plt
from pi import desv_pad


def plot(di, p, n, lista, media):
    """Plota dois gráficos em uma mesma imagem. O primeiro ilustra o processo de estimativa do número pi,
    plotando pontos aleatórios em um sistema cartesiano de coordenadas contendo uma circunferência de raio 1 e um
    quadrado de lado 2. O segundo é um histograma das n estimativas de pi realizadas, ajustado por uma curva
    gaussiana """

    fig, ax = plt.subplots(1, 2, figsize=(12.8, 6.4))  # cria 2 plots em linha

    # gráfico de dispersão na primeira figura
    ax1 = ax[0]
    ax1.add_artist(plt.Circle((0, 0), radius=1, lw=0.5, fill=False))  # adiciona círculo
    ax1.add_artist(plt.Rectangle((-1, -1), 2, 2, lw=0.5, fill=False))  # adiciona quadrado
    ax1.scatter(*zip(*di.keys()), c=di.values(), s=0.5)  # plota os pontos
    # montando o sistema cartesiano de coordenadas
    ax1.spines['top'].set_color('none')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['left'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.arrow(0, 0, 1.05, 0, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax1.arrow(0, 0, 0, 1.05, head_width=0.04, head_length=0.05, fc='k', ec='k', lw=0.001)
    ax1.set_xlabel('x', size=14)
    ax1.set_xticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax1.xaxis.set_label_coords(0.998, 0.488)
    ax1.set_ylabel('y', size=14, rotation=0)
    ax1.set_yticks([-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1])
    ax1.yaxis.set_label_coords(0.477, 0.98)
    ax1.tick_params(labelsize=10)

    # histograma na segumda figura
    ax2 = ax[1]
    hist = ax2.hist(lista, bins=50, color='#00ffcc')
    ax2.set_xlabel('Pi estimado')
    ax2.axvline(media, color='k', ls='dashed', lw=0.7)  # plota a linha na média do histograma
    # texto na linha da média
    min_ylim, max_ylim = plt.ylim()
    ax2.text(media * 1.001, max_ylim * 0.95, f'Média: {media:.5f}', size=12)
    # título
    ax2.set_title(f'Histograma para {n} estimativas de pi\nde {p} pontos cada (ex: plot à esquerda)', size=14)
    # curva gaussiana ajustada ao histograma
    lista_cresc = sorted(lista)
    dp = desv_pad(lista, media)
    x_bin = [0.5 * (hist[1][r] + hist[1][r + 1]) for r in range(len(hist[1]) - 1)]  # posições médias dos bins
    tam_bin = (max(x_bin) - min(x_bin)) / len(hist[1])  # largura dos bins
    y = [len(lista) * tam_bin * (exp(-0.5 * (((x - media) / dp) ** 2)) / (dp * (2 * pi) ** 0.5)) for x in lista_cresc]
    ax2.plot(lista_cresc, y, color='k', lw=0.7)

    plt.show()
