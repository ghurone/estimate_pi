from random import uniform


def cores(p):  # p = número de pontos
    r = 1  # raio
    d = {}

    lista_cores = ['#E14E65', '#F98D52', '#EBE051', '#6DBB5B', '#5286DA', '#714EB3']
    dist = [r * k / len(lista_cores) if k != 0 else 0 for k in range(len(lista_cores), -1, -1)]

    for i in range(p):
        x = uniform(-r, r)  # coordenada x
        y = uniform(-r, r)  # coordenada y

        square_distance = x ** 2 + y ** 2
        sqrt_distance = square_distance ** 0.5

        if square_distance <= r ** 2:  # testa os pontos
            for j in range(len(dist)):
                if dist[j] >= sqrt_distance >= dist[j + 1]:
                    d[(x, y)] = lista_cores[j]
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


def desv_pad(lista, media):
    """Calcula o desvio padrão"""
    tam = len(lista)
    soma = 0

    for d in lista:
        soma += (d - media) ** 2

    desv = (soma / (tam - 1)) ** 0.5

    return desv
