import matrix as mx

def tringle(a, b, c):
    return a * b * c

def det2x2(a):
    if type(a) == mx.matrix:
        det = a.matrix[0][0] * a.matrix[1][1] - a.matrix[0][1] * a.matrix[1][0]
        return det
    elif type(a) == list:
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return det
    else :
        print("Error! Use matrix or list!")

# Нахождение детерминанта с помощью методом Саррюса
def det3x3(a):
    if type(a) == mx.matrix:
        f = tringle(a.matrix[0][0], a.matrix[1][1], a.matrix[2][2])
        g = tringle(a.matrix[0][0], a.matrix[0][2], a.matrix[2][0])
        c = tringle(a.matrix[0][1], a.matrix[1][0], a.matrix[2][1])
        res1 = f + g + c

        f = tringle(a.matrix[0][2], a.matrix[1][1], a.matrix[2][0])
        g = tringle(a.matrix[0][0], a.matrix[1][2], a.matrix[2][1])
        c = tringle(a.matrix[0][1], a.matrix[2][0], a.matrix[2][2])
        res2 = f + g + c

        return res1-res2
    elif type(a) == list:
        f = tringle(a[0][0], a[1][1], a[2][2])
        g = tringle(a[0][0], a[0][2], a[2][0])
        c = tringle(a[0][1], a[1][0], a[2][1])
        res1 = f + g + c

        f = tringle(a[0][2], a[1][1], a[2][0])
        g = tringle(a[0][0], a[1][2], a[2][1])
        c = tringle(a[0][1], a[2][0], a[2][2])
        res2 = f + g + c

        return res1-res2
    else :
        print("Error! Use matrix or list!")
# не должно равняться x

# Нахождение детерминанта с помощью алгеброического добавления
def det3x3_2(a):
    if type(a) == mx.matrix:
        for x in range(3):
            if x==0:
                c = a.matrix[0][0] * \
                        det2x2([a.matrix[1][1:], a.matrix[2][1:]])
            elif x==2:
                d = a.matrix[0][2] * \
                        det2x2([a.matrix[1][:2], a.matrix[2][:2]])
            else:
                f = a.matrix[0][1] * \
                        det2x2([[a.matrix[1][0], a.matrix[1][2]],\
                                [a.matrix[2][0], a.matrix[2][2]]])

        return c - d + f
    elif type(a) == list:
        for x in range(3):
            if x==0:
                c = a[0][0] * \
                        det2x2([a[1][1:], a[2][1:]])
            elif x==2:
                d = a[0][2] * \
                        det2x2([a[1][:2], a[2][:2]])
            else:
                f = [0][1] * \
                        det2x2([[a[1][0], a[1][2]],\
                                [a[2][0], a[2][2]]])

        return c - d + f
    else :
        print("Error! Use matrix or list!")

# def minor(a, x, column, row):
#     #     Если это первый элемент матрицы
#     result = []
#     if x==0:
#         for y in range(1, row):
#             result.extend([a.matrix[1:][y][1:]])
#         return result
#     # если это последний элемент матрицы
#     elif (x == (a.column-1)):
#         for y in range(row-1):
#             result.extend([a.matrix[1:][y][:row]])
#         return result
#     # в других случаях
#     else:
#         for y in range(1, x):
#             result.extend([a.matrix[1:][y][:x]])
#         for y in range(x+1, row):
#             result.extend([a.matrix[x+1:][y][:row]])
#         return result
