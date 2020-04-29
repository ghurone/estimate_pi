import random


def pi(n):  # n = Número de pontos
    n_total = 0
    n_circulo = 0
    r = 1  # deixei o raio constante, mas só alterar para o raio de sua escolha

    for i in range(n):
        x = random.uniform(0, r)  # valor do ponto no eixo x
        y = random.uniform(0, r)  # valor do ponto no eixo y

        square_distance = x ** 2 + y ** 2

        if square_distance <= r**2:  # testando se o ponto está dentro da circuferência
            n_circulo += 1

        n_total += 1

    return 4 * n_circulo / n_total
