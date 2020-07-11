from random import uniform


def colors(p):  # p = number of points
    r = 1  # radius value
    d = {}

    color_list = ['#E14E65', '#F98D52', '#EBE051', '#6DBB5B', '#5286DA', '#714EB3']
    dist = [r * k / len(color_list) if k != 0 else 0 for k in range(len(color_list), -1, -1)]

    for i in range(p):
        x = uniform(-r, r)  # point value on the x axis
        y = uniform(-r, r)  # point value on the y axis

        square_distance = x ** 2 + y ** 2
        sqrt_distance = square_distance ** 0.5

        if square_distance <= r ** 2:  # testing the points
            for j in range(len(dist)):
                if dist[j] >= sqrt_distance >= dist[j + 1]:
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


def desv_pad(lista):
    """Calcula o desvio padrão"""
    tam = len(lista)
    media = sum(lista) / tam
    soma = 0

    for d in lista:
        soma += (d - media) ** 2

    desv = (soma / (tam - 1)) ** 0.5

    return desv

