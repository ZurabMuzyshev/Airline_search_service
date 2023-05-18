def validate_input(prompt, length=None):
    while True:
        user_input = input(prompt)
        if length is not None and len(user_input) != length:
            print(f"Длина должна быть равна {length} символам")
        else:
            return user_input


def validate_float_input(prompt):
    while True:
        user_input = input(prompt)
        if not user_input.replace('.', '').isdigit():
            continue
        value = float(user_input)
        if value < 0:
            print("Некорректное значение стоимости. Введите неотрицательное число (целое или дробное)")
        elif value.is_integer():
            return int(value)
        else:
            return value


def add_flight():
    flight_number = validate_input('XXXX - номер рейса: ', length=4).upper()
    flight_date = validate_input('ДД/ММ/ГГГГ - дата рейса: ', length=10)
    departure_time = validate_input('ЧЧ:ММ - время вылета: ', length=5)
    flight_duration = validate_input('ХХ.ХХ - длительность перелета: ')
    departure_airport = validate_input('ХХХ - аэропорт вылета: ', length=3).upper()
    destination_airport = validate_input('ХХХ - аэропорт назначения: ', length=3).upper()
    ticket_price = validate_float_input('.ХХ - стоимость билета: ')
    flight_info = f'{flight_number} {flight_date} {departure_time} {flight_duration} {departure_airport}' \
                  f' {destination_airport} {ticket_price}'
    print(f'Информация о рейсе: {flight_info} добавлена')
    return flight_info


def print_flight_info(flight_info):
    if flight_info:
        flights = flight_info.split('\t')
        for i in flights:
            print(i)
    else:
        print('Информация о рейсах отсутствует')


def search_flight(flight_info, search_number):
    flights = flight_info.split('\n')
    for flight in flights:
        if search_number in flight:
            print('Информация о рейсе:', flight)
            return
    print('Такого номера рейса не существует')


def main():
    flight_info = ''
    while True:
        print('\nСервис поиска авиабилетов\n')
        print('Главное меню:')
        print('\t1 - ввод рейса')
        print('\t2 - вывод рейсов')
        print('\t3 - поиск рейсов по номеру')
        print('\t0 - завершение работы')
        action_choice = int(input('Введите номер пункта меню: '))
        if action_choice == 0:
            print('Работа завершена')
            break
        elif action_choice == 1:
            flight_info += 'Информация о рейсе: ' + add_flight() + '\n'
        elif action_choice == 2:
            print_flight_info(flight_info)
        elif action_choice == 3:
            search_number = validate_input('Введите номер рейса в формате - ХХХХ: ', length=4)
            search_flight(flight_info, search_number)
        else:
            print('Введите корректное число!')


main()
