import matplotlib.pyplot as plt
from numpy import matrix
def Some_func():

    def f(x):
        return (x + 1.6) / (x ** 2 + x + 3.2)


    X = []
    N = [4, 6, 8]

    for nn in range(3):
        if (nn == 0):
            n = 4
            b = 4.8
            a = 0.8

            ansX = 1.34064

            h = (b - a) / n
            x = []
            for i in range(1,n):
                x.append(a + i * h)

            fx = []
            fa = f(a)
            fx.append(fa)
            for i in range(n-1):
                fx.append(f(x[i]))
            fb = f(b)
            fx.append(fb)

            Itrap = (h / 2) * (fa + fb + 2 * (sum(fx[1:n])))
            X.append(Itrap)

        if (nn == 1):
            n = 6
            b = 4.8
            a = 0.8

            ansX = 1.34064

            h = (b - a) / n
            x = []
            for i in range(1, n):
                x.append(a + i * h)

            fx = []
            fa = f(a)
            fx.append(fa)
            for i in range(n - 1):
                fx.append(f(x[i]))
            fb = f(b)
            fx.append(fb)

            Itrap = (h / 2) * (fa + fb + 2 * (sum(fx[1:n])))
            X.append(Itrap)

        if (nn == 2):
            n = 8
            b = 4.8
            a = 0.8

            ansX = 1.34064

            h = (b - a) / n
            x = []
            for i in range(1, n):
                x.append(a + i * h)

            fx = []
            fa = f(a)
            fx.append(fa)
            for i in range(n - 1):
                fx.append(f(x[i]))
            fb = f(b)
            fx.append(fb)

            Itrap = (h / 2) * (fa + fb + 2 * (sum(fx[1:n])))
            X.append(Itrap)

    plt.plot(N, X)
    plt.show()