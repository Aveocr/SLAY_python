def convert2list(string):
    return string.split(" ")

# Меняем знак на противоложный
def change_value(string, i):
    # Когда знак отрицательный
    if string[i-1] == '-':
         string[i-1] = str(string[i-1]).replace('-', '+')
    # Когда знак положительный
    elif string[i-1] == '+':
        string[i-1] = str(string[i-1]).replace('+', '-')
    # Меняем знак у самого числа
    string[i] = str(string[i]).replace('-', '')
    return string
    # показать пример
def show_example(number):
    # Конвертируем стринг в список
    number = convert2list(number)
    # Приравниваем стринг следующему выражению
    string = f"{number[0]} + {number[1]} + {number[2]} = {number[3]}"
    string = string.split(" ")
    # Простой алгоритм смены знака на противоложный
    for i in range(1, len(string)-2):
        if i % 2 == 0 and int(string[i]) < 0: string = change_value(string, i)
    # Выводим сам пример
    print(f"| {string[0]}x {string[1]} {string[2]}y {string[3]} {string[4]}z {string[5]} {string[6]}")
