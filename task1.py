# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day = int(input('Введите цифру, обозначающую день недели:'))
if day == 6 or day == 7:
    print ('этот день выходной? -> да')
elif day < 1 or day > 7:
    print ('Это не день недели')
else: 
    print ('этот день выходной? -> нет ')
