# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
number = int(input('Введите номер четверти: '))
if number < 1 or number > 4:
    print('Некорректный номер')
elif number == 1:
    print('X > 0; Y > 0')
elif number == 2:
    print('X < 0; Y > 0')
elif number == 3:
    print('X < 0; Y < 0')
else:
    print('X > 0; Y < 0')