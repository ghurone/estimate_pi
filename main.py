from pi import *

if __name__ == '__main__':
    p = 10000  # number of points

    n = int(input('Quantas vezes? '))
    pi_list = [pi(colors(p)) for i in range(n)]  # list with n values of pi

    med = sum(pi_list)/len(pi_list)
    print(f'Média: {med:.5f}')

    plot(colors(p), p, n, pi_list)
