print("введите 3 стороны треугольника ") #Получаем ввод от пользователя
a = float(input("первая: ")) # Первая сторона
b = float(input("вторая: ")) # Вторая сторона
c = float(input("третья: ")) # Третья сторона
 # Проверяем неравенство треугольника
if a + b > c and b + c > a and c + a > b:
    print("треугольник существует") 
else: print("такого треугольника не существует")
