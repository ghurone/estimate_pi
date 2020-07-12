from pi import *
from plot import plot


if __name__ == '__main__':
    p = 10000  # número de pontos

    n = int(input('Quantas vezes? '))
    pi_list = [pi(cores(p)) for i in range(n)]  # lista com n valores de pi

    plot(cores(p), p, n, pi_list)
