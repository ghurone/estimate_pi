from pi import *

if __name__ == '__main__':
    s = 10000  # number of points

    n = int(input('Quantas vezes? '))
    pi_list = [pi(colors(s)) for i in range(n)]  # list with n values of pi

    med = sum(pi_list)/len(pi_list)
    print(f'Média: {med:.5f}')

    plot_points(colors(s))
    plot_hist(pi_list)
