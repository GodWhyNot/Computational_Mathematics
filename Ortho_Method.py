# A example for matrix input from user
def Ortho_Method():
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))

    # Initialize empty matrix
    matrix = []
    print("Enter the entries row wise:")

    # For user input
    for i in range(row):  # A outer for loop for row entries
        a = []
        for j in range(column):  # A inner for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    b = []
    for i in range(row):
        b.append(int(input("Enter the B's value:")))

    # Searching t12
    t12_1 = 0
    t12_2 = 0
    for i in range(row):
        t12_1 += matrix[i][0] * matrix[i][1]
        t12_2 += matrix[i][0] ** 2
    print("t12: ", t12_1, "/", t12_2)

    # Searching r2
    r2 = []
    for i in range(row):
        r2.append(matrix[i][1] - (t12_1 / t12_2) * matrix[i][0])
    print("r2: ", r2)

    # Searching t13
    t13_1 = 0
    t13_2 = 0
    for i in range(row):
        t13_1 += matrix[i][0] * matrix[i][2]
        t13_2 += matrix[i][0] ** 2
    print("t13: ", t13_1, "/", t13_2)

    # Searching t23
    t23_1 = 0
    t23_2 = 0
    for i in range(row):
        t23_1 += r2[i] * matrix[i][2]
        t23_2 += r2[i] ** 2
    print("t23: ", t23_1, "/", t23_2)

    # Searching r3
    r3 = []
    for i in range(row):
        r3.append(matrix[i][2] - (t13_1 / t13_2) * matrix[i][0] - (t23_1 / t23_2) * r2[i])
    print("r3: ", r3)

    # Creating matrix R
    R = []
    for i in range(row):
        a = []
        for j in range(column):
            a.append(matrix[i][0])
            a.append(r2[i])
            a.append(r3[i])
        R.append(a)

    # For printing the R
    print("matrix R")
    for i in range(row):
        for j in range(column):
            print(R[i][j], end=" ")
        print()

    # Creating matrix T
    T = []
    a = []
    a.append(1)
    a.append(t12_1 / t12_2)
    a.append(t13_1 / t13_2)
    T.append(a)
    a1 = []
    a1.append(0)
    a1.append(1)
    a1.append(t23_1 / t23_2)
    T.append(a1)
    a2 = []
    a2.append(0)
    a2.append(0)
    a2.append(1)
    T.append(a2)

    # For printing the T
    print("matrix T")
    for i in range(row):
        for j in range(column):
            print(T[i][j], end=" ")
        print()

    # Searching x3
    x3_1 = 0
    x3_2 = 0
    for i in range(row):
        x3_1 += (r3[i] * b[i])
        x3_2 += (r3[i] * matrix[i][2])
        x3 = x3_1 / x3_2
    #for i in range(row):
    #    print("r3: ", r3[i], "b: ", b[i], "matrix ", matrix[i][2])

    print("x3: ", x3)

    # Serching new b
    b1 = []
    for i in range(row):
        b1.append(b[i] - (matrix[i][2] * x3))
    print("b1: ", b1)

    # Searching x2
    x2_1 = 0
    x2_2 = 0
    for i in range(row):
        x2_1 += (r2[i] * b1[i])
        x2_2 += (r2[i] * matrix[i][1])
        x2 = x2_1 / x2_2
    #for i in range(row):
    #    print("r2: ", r2[i], "b1: ", b1[i], "matrix ", matrix[i][1])
    print("x2: ", x2)

    # Serching new b
    b2 = []
    for i in range(row):
        b2.append(b1[i] - (matrix[i][1] * x2))
    print("b2: ", b2)

    # Searching x1
    x1_1 = 0
    x1_2 = 0
    for i in range(row):
        x1_1 += (matrix[i][0] * b2[i])
        x1_2 += (matrix[i][0] * matrix[i][0])
        x1 = x1_1 / x1_2
    #for i in range(row):
    #    print("matrix: ", matrix[i][0], "b2: ", b2[i], "matrix ", matrix[i][0])
    print("x1: ", x1)
