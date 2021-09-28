# Matrix
# @author Aveocr

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        # self.column - это количество строк
        self.column = len(matrix)
        # self.row - это количество столбцов
        self.row = len(matrix[0])

    # при выводе
    def __str__(self):
        print("matrix(", end="")
        for column in range(self.column):
            for row in range(self.row):
                # Если число последнее в строке
                if row == (self.row - 1):
                    print(f'\t{str(self.matrix[column][row])}', end="")
                # Все другие числа
                else:
                    print(f'\t{str(self.matrix[column][row])}', end=", ")

            if column == (self.column - 1):
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
        if type(other) == Matrix:
            # Если self.equal == True и размер матриц совпадают
            if other.column == self.column and other.row == self.row:
                # выполняем сложение через цикл
                for column in range(other.column):
                    for row in range(other.row):
                        self.matrix[column][row] += other.matrix[column][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] += other
        return Matrix(self.matrix)

    # вычитание
    def __sub__(self, other):
        # Если other является list
        if type(other) == Matrix:
            for column in range(other.column):
                for row in range(other.row):
                    self.matrix[column][row] -= other.matrix[column][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] -= other
        return Matrix(self.matrix)

    # умножение
    def __mul__(self, other):
        # Если other является list
        if type(other) == Matrix:
            # Если количество столбцов в первой матрице и количество строк во второй матрице совпадает
            if other.row == self.column:
                # проивзодим сложение через цикл
                for column in range(other.column):
                    for row in range(other.row):
                        self.matrix[column][row] *= other.matrix[row][row]
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] *= other
        return Matrix(self.matrix)

    # Проверка размерности матрицы
    def check_dimension(self, other_matrix):
        pass
