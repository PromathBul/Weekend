number_day = int(input('Введите номер дня недели: '))

if number_day < 1 or number_day > 7:
    print('Номер дня недели должен быть в диапазоне от 1 до 7')
elif number_day == 6 or number_day == 7:
    print('да')
else:
    print('нет')