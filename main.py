from pi import *
from plot import plot


if __name__ == '__main__':
    p = 100000  # número de pontos

    n = int(input('Quantas estimativas de pi serão feitas? '))
    lista_pi = [pi(cores(p)) for i in range(n)]  # lista com n valores de pi
    media = sum(lista_pi) / len(lista_pi)
    dp = desv_pad(lista_pi, media)

    # imprime os resultados
    print(f'A melhor estimativa para pi foi: {round(media, 5)} ± {round(dp, 5)}')
    plot(cores(p), p, n, lista_pi, media)
