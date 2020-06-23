# матрица
# Денис Мустафин
# 05.06.2020
class matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.column = len(matrix)
        self.row =  len(matrix[0])
        self.equal = (self.row == self.column)
    # при выводе
    def __str__(self):
        print("matrix(", end="")
        for column in range(self.column):
            for row in range(self.row):
                # Если число последнее в строке
                if (row == (self.row-1)):
                     print(f'\t{str(self.matrix[column][row])}', end="")
                # Все другие числа
                else :
                    print(f'\t{str(self.matrix[column][row])}', end=", ")

            if column == (self.column-1):
                print(")")
            else:
                print()
        return ''
    # когда надо вернуть итем
    def __getitem__(self, item):
        return self.matrix[item]
    # сложение
    def __add__(self, other):
        # Если other является списком
        if type(other) == list or type(other) == matrix:
            other_column = other.column
            other_row = other.row
            # Если self.queal == True и размер матриц совпадают
            if (self.equal\
            and other_column == self.column\
            and other_row == self.row):
                # проивзодим сложение через цикл
                for column in range(other_column):
                    for row in range(other_row):
                        self.matrix[column][row] += other.matrix[column][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                    for row in range(self.row):
                        self.matrix[column][row] += other
        return matrix(self.matrix)


    # вычитание
    def __sub__(self, other):
        # Если other является list
        if type(other) == list or type(other) == matrix:
            other_column = other.column
            other_row = other.row
            # Если self.queal == True и размер матриц совпадают
            if (self.equal \
            and other_column == self.column\
            and other_row == self.row):
                # проивзодим сложение через цикл
                for column in range(other_column):
                    for row in range(other_row):
                        self.matrix[column][row] -= other.matrix[column][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                    for row in range(self.row):
                        self.matrix[column][row] -= other
        return matrix(self.matrix)
    # умножение
    def __mul__(self, other):
        # Если other является list
        if type(other) == list or type(other) == matrix:
            other_column = other.column
            other_row = other.row
            # Если self.queal == True и размер матриц совпадают
            if (self.equal \
            and other_column == self.column\
            and other_row == self.row):
                # проивзодим сложение через цикл
                for column in range(other_column):
                    for row in range(other_row):
                        self.matrix[column][row] *= other.matrix[column][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                    for row in range(self.row):
                        self.matrix[column][row] *= other
        return matrix(self.matrix)
