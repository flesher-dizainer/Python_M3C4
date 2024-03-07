# вывести на экран простые чиса из диапазона
def task_1():
    try:
        fist_round = int(input('Enter first number value: '))
        end_round = int(input('Enter end number value: '))
        while fist_round < end_round:
            number_value = False
            for i in range(2, fist_round):
                if fist_round % i == 0:
                    number_value = True
                    break
            if not number_value:
                print(fist_round)
            fist_round += 1

    except ValueError:
        print('Error input value')


# показать таблицу умножения 1..10
def task_2():
    for i in range(1, 11):
        line_result = ''
        for s in range(1, 11):
            mul = i * s
            line_result += f'{i} * {s} = {mul}\t'
        print(line_result)


# показать таблицу умножения пользовательского диапазона
def task_3():
    try:
        fist_round = int(input('Enter first number value: '))
        end_round = int(input('Enter end number value: '))
        for i in range(fist_round, end_round + 1):
            line_result = ''
            for s in range(1, 11):
                mul = i * s
                line_result += f'{i} * {s} = {mul}\t'
            print(line_result)
    except ValueError:
        print('Error input value')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
