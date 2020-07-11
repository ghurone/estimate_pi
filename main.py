from pi import *
from plot import plot


if __name__ == '__main__':
    p = 100000  # number of points

    n = int(input('Quantas vezes? '))
    pi_list = [pi(colors(p)) for i in range(n)]  # list with n values of pi

    plot(colors(p), p, n, pi_list)
