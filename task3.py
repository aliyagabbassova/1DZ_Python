# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x > 0 and y > 0:
    print ('Данная точка находится в I четверти')
elif x < 0 and y > 0:
    print ('Данная точка находится во II четверти')
elif x < 0 and y < 0:
    print ('Данная точка находится в III четверти')   
elif x > 0 and y < 0:
    print ('Данная точка находится в IV четверти')
elif x == 0 and y == 0:
    print ('Некорректные данные')
