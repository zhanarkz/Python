def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            line = line.replace('\n', '')
            result.append(line.split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def print_bus():
    buses_list = read_data_from_file('bus.txt')
    print('|№ |\tавтобус ID |\t тип  |\t гос. номер')
    print('-'*60)
    for num, bus in enumerate(buses_list):
        print(f'|{num+1} |\t     {bus[0]} |\t {bus[2]}|\t{bus[1]}')

def add_bus():
    save_data_to_file('bus.txt', input("введите параметры автобуса "))

def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("введите данные водителя "))

from operator import itemgetter
def get_data(request: str, data_list: list) -> list:
    '''возвращает нужную строку, содержащую запрос'''
    for line in data_list:
        if request == itemgetter(0)(line):
            return line
    return ['None', 'None', 'None', 'None']

def print_route():
    routes_list = read_data_from_file('route.txt')
    buses_list = read_data_from_file('bus.txt')
    print('|№ |\tмаршрут |\tавтобус |\tгос.номер | маршрут')
    print('-'*70)
    for num, route in enumerate(routes_list):
        bus_request = route[1]
        bus_data = get_data(bus_request, buses_list)
        print(
             f'|{num+1} |\t{route[0]} |\t{bus_data[0]}|'
             f'\t{bus_data[1]} | {route[1]}')
   

def add_route():
    save_data_to_file('route.txt', input("введите данные маршрута "))