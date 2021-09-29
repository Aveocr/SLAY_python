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
        print("\nmatrix(", end="")
        for column in range(self.column):
            for row in range(self.row):
                # Если число в первой строке
                if column == 0 and row != (self.row - 1):
                    print(str(self.matrix[column][row]), end=", ")
                # Если число последнее в строке
                elif row == (self.row - 1):
                    print(str(self.matrix[column][row]), end="")
                # Все другие числа
                else:
                    print("\t",str(self.matrix[column][row]), end=", ")

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
        if self.check_matrix(other):
                # выполняем сложение через цикл
                for column in range(other.column):
                    for row in range(other.row):
                        self.matrix[column][row] += other.matrix[column][row]
                return Matrix(self.matrix)
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] += other
            return Matrix(self.matrix)
        else:
            return "Невозможно произвести вычесления! "

    # вычитание
    def __sub__(self, other):
        # Если other является list
        if self.check_matrix(other):
            for column in range(other.column):
                for row in range(other.row):
                    self.matrix[column][row] -= other.matrix[column][row]
            return Matrix(self.matrix)
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] -= other
            return Matrix(self.matrix)

        else:
            return "Невозможно произвести вычесления! "

    # умножение
    def __mul__(self, other):
        # Если other является list
        if type(other) == Matrix and self.row == other.column:
            # Если количество столбцов в первой матрице и количество строк во второй матрице совпадает
            # создаем новую матрицу
            C = []
            # выполняем умножение
            for i in range(self.column):
                C.append([])
                for j in range(other.row):
                    _sum = 0
                    for k in range(self.row):
                        _sum += (self.matrix[i][k] * other.matrix[k][j])
                    C[i].append(_sum)
            return Matrix(C)
        # Если other является целый числом
        elif type(other) == int:
            for column in range(self.column):
                for row in range(self.row):
                    self.matrix[column][row] *= other

            return Matrix(self.matrix)
        else:
            return "Невозможно произвести вычисления"

    # Проверка на тип, а так же что размер матриц совпадает
    def check_matrix(self, other):
        if type(other) == Matrix and (other.column == self.column and other.row == self.row):
            return True
        return False