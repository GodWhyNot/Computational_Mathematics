def Gauss_Method():
    # A example for matrix input from user
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))

    # Initialize empty matrix
    matrix = []
    print("Enter the entries row wise:")

    ###__First iteration__###

    # For user input
    for i in range(row):  # A outer for loop for row entries
        a = []
        for j in range(column):  # A inner for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    b = []
    for i in range(row):
        b.append(int(input("Enter the B's value:")))

    # For printing the matrix
    print("matrix")
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()

    # For printing the B
    print("b: ", b)

    # Поиск коэффициента С
    C = []
    for j in range(column):
        C.append(matrix[0][j] / matrix[0][0])

    matrix1 = []
    for i in range(row):
        a1 = []
        a2 = []
        for j in range(column):
            a1.append(matrix[1][j] - (matrix[1][0] * C[j]))
            a2.append(matrix[i][j] - C[j] * matrix[i][0])
    matrix1.append(C)
    matrix1.append(a1)
    matrix1.append(a2)

    g1 = b[0] / matrix[0][0]

    b1 = []
    b1.append(g1)
    b1.append(b[1] - (matrix[1][0] * g1))
    b1.append(b[2] - (matrix[2][0] * g1))

    print("matrix1""\n")
    # For printing the matrix
    for i in range(row):
        for j in range(column):
            print(matrix1[i][j], end=" ")
        print()

    print("C: ", C)
    print("g1: ", g1)

    print("b1: ", b1)

    ###__Second iteration__###

    C1 = []
    for j in range(column):
        C1.append(matrix1[1][j] / matrix1[1][1])

    g2 = b1[1] / matrix1[1][1]

    matrix2 = []
    for i in range(row):
        a3 = []
        for j in range(column):
            a3.append(matrix1[2][j] - C1[j] * matrix1[2][1])

    matrix2.append(C)
    matrix2.append(C1)
    matrix2.append(a3)

    b2 = []
    b2.append(g1)
    b2.append(g2)
    b2.append(b1[2] - (matrix1[2][1] * g2))

    print("C1: ", C1)
    print("g2: ", g2)
    print("matrix2""\n")
    # For printing the matrix2
    for i in range(row):
        for j in range(column):
            print(matrix2[i][j], end=" ")
        print()
    print("b2: ", b2)

    ###__Third iteration__###
    C2 = []
    for j in range(column):
        C2.append(matrix2[2][j] / matrix2[2][2])

    g3 = b2[2] / matrix2[2][2]
    print("C2: ", C2)
    print("g3: ", g3)

    # Reverse step
    x3 = g3
    x2 = g2 - (C1[2] * x3)
    x1 = g1 - (C[1] * x2) - (C[2] * x3)

    print("x1: ", x1)
    print("x2: ", x2)
    print("x3: ", x3)
