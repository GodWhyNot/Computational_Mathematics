# Ввод погрешности
Eps = float(input("Введите погрешность: "))
# Ввод размера СЛАУ
n = int(input("Введите размер матрицы: "))


# Ввод матрицы
matrix = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(float(input("M[{}][{}]: ".format(i, j))))
    matrix.append(a)


# Ввод вектора b
b = []
for i in range(n):
    b.append(float(input("b[{}]: ".format(i))))


# Вывод матрицы
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
for i in range(n):
    print(b[i])


# Нулевая итерация
x0 = []
for i in range(n):
    x0.append(b[i] / matrix[i][i])
print("Нулевое приближение: ", x0)


def iteration_method(matrix, b, x0, n):
    x1 = []
    sig1 = []
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i:
                sum += matrix[i][j] * x0[j]
        x1.append((b[i] - sum) / matrix[i][i])
        sig1.append(abs(x1[i] - x0[i])/abs(x1[i]))
    return x1, sig1


# Используем метод итераций в цикле до тех пор, пока не будет достигнута заданная точность
k = 1
while True:
    x1, sig1 = iteration_method(matrix, b, x0, n)
    print(k, "-ое приближение: ", x1)
    print("Погрешность: ", sig1)
    if max(sig1) < Eps:
        break
    x0 = x1
    k += 1
