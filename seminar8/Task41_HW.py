SIMPLE_EXPRESSION = '22 * 300 + 10 * 10'


def simple_expression(string_expression: str) -> None:
    '''парсер простого выражения без скобок.
        продолжение работы на семинаре'''

    start_list = string_expression.split()
    intermediate_list = []

    if start_list[0].isdigit():
        start_list.insert(0, '+')

    result = 0

    for i in range(0, len(start_list)-1, 2):
        if start_list[i] == '*':
            multyply = int(intermediate_list[-1]) * int(start_list[i+1])
            intermediate_list[-1] = multyply
        elif start_list[i] == '/':
            division = int(intermediate_list[-1]) / int(start_list[i+1])
            intermediate_list[-1] = division
        else:
            intermediate_list.append(start_list[i])
            intermediate_list.append(start_list[i+1])

    for i in range(0, len(intermediate_list)-1, 2):
        if intermediate_list[i] == '+':
            result += int(intermediate_list[i+1])
        elif start_list[i] == '-':
            result = result - int(intermediate_list[i-1])
        else:
            continue
    print(string_expression + ' = ' + str(result))


simple_expression(SIMPLE_EXPRESSION)