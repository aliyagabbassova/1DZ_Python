# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right
            print (x, y, z, result)
           


