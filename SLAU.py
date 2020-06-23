from time import sleep
import sys
import determinant as det
import matrix as mx
import change_value as cv
# конвертируем число в int
# проверяет, согласен ли пользователь с введеным им вводом

def convert2int(matrix, row, column):
    for i in range(column):
        for j in range(row):
            matrix[i][j] = int(matrix[i][j])
    return matrix
if __name__ == '__main__':
    print(" Привет! Добро пожаловать в калькулятор для решения СЛАУ методом Крамера")
    print("\n Создал Денис Мустафин")

    print(" В каждом уравнение необходимо ввести 4 числа\n")
    print(" Формат примера следующий: \n")
    print(" | ?x + ?y + ?z = ?\n\n\n")
    size = int(input("Введите, количество уравнений >> "))
    print(f"\n\n\t\tВаше количество уравнений {size}\n\n")
    print(" 4 Числа надо вводить в одну строчку и через пробел! \n Число перед >>"\
          " не считается\n Для выхода надо написать exit")
    # size = 2
    matrix = list()
    for i in range(size):
        # Условие будет каждый раз обновляться, пока пользователь не даст согласие
        agree = True
        # Если проверка отключения, чтобы не давать agree быть True
        print(f" Пример {i+1} >> ", end="")
        number = input()
        if number == 'exit':
            print("Удачи!")
            sleep(3)
            sys.exit(0)
        # показать пример
        cv.show_example(number)

        matrix.append(list(tuple(number)))

    column = len(matrix)
    buff = [matrix[i][:3] for i in range(column)]
    main = mx.matrix(convert2int(buff, 4, 3))
    result = [int(matrix[i][3]) for i in range(column)]
    # находим det для основной матрицы
    a = det.det3x3(main)
    dets = list()
    # находим детерминант для остальных матриц
    for i in range(main.matrix.row):
        buff = main
        for j in range(column):
            buff.matrix[j][i] = int(result[j])
        dets.append(det.det3x3(buff))
    print("Ответ: \n х - {dets[0]/main}" +
                 "\n у - {dets[1]/main}" +
                 "\n z - {dets[2]/main}")

    print("Спасибо за использование программы :3")
