# 1. Вводится два слова с клавиатуры. Нужно вывести какое слово длиннее.
# Учесть вариант, что они могут быть равны.
# str1 = input('Введите первое слово: ')
# str2 = input('Введите второе слово: ')
# a = len(str1)
# b = len(str2)
# if a > b:
#     print (str1)
# elif a < b:
#     print(str2)
# else:
#     print('Слова одиноковые по количеству букв ')
# 2. Вводится число, как строка, в клавиатуры. Необходимо проверить делится ли оно на 5 и вывести «Yes» или «No».
# Также проверить делится ли оно на 4 и вывести «Yes» или «No».
# Подсказка: Число делится на 5, если оканчивается на 0 или 5.
# Число делится на 4, если две последние его цифры — нули или образуют число, которое делится на 4.
# str1 = input('Введите число: ')
# num1 = int(str1[-1 :])
# num2 = int(str1[-2: ])
# if num1 == 5 or num1 ==0:
#     print('Yes')
# else:
#     print('No')
# if num2 % 4 == 0:
#     print('Yes')
# else:
#     print('No')
#3. Случайное число от 1 до 12 (номер месяца), использовать random.
# Нужно вывести какой это сезон года (зима, весна, лето, осень).
# import random
# age = random.randint(1, 12)
# print(age)
# if age >=3 and age <=5:
#     print('Весна')
# elif age >=6 and age <=8:
#     print('Лето')
# elif age >=9 and age <=11:
#     print('Осень')
# else:
#     print('Зима')


# 4. *Вводитcя четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки на шахматной доске. Ладья ходит по горизонтали или вертикали.
# Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Пример:
# входные данные:
# Введите номер столбца: 4
# Введите номер строки: 4
# Введите номер столбца: 5
# Введите номер строки: 5
# выходные данные: No
# print('Введите четыре числа от 0 до 8.')
# num1 = int(input('Введите номер столбца '))
# num2 = int(input('Введите номер строки '))
# num3 = int(input('Введите номер столбца '))
# num4 = int(input('Введите номер строки '))
# if num2 == num4 and num1 != num4:
#     print("yes")
# elif num1 == num3 and num2 !=num4:
#     print('Yes')
# else:
#     print("no")

# Яша плавал в бассейне размером N×M метров и устал. В этот момент он обнаружил, что находится
# на расстоянии X метров от одного из длинных бортиков (не обязательно от ближайшего)
# и Y метров от одного из коротких бортиков.
# Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
# Входные данные: 23 52 8 43
# Выходные данные: 8
age1 = int(input('Введите ширину басейна: '))
age2 = int(input('Введите длину бассейна: '))
age3 = int(input('Введите расстояние до длинного бортика бассейна: '))
age4 = int(input('Введите расстояние до короткого бортика бассейна: '))
#Вывести минимальное вводимое значение
if age3 < age4:
    print(age3)
elif age3 == age4:
    print("Одинаково плыть до любого бортика")
else:
    print(age4)

#3. Задается окружность с радиусом R. Можно ли вписать туда прямоугольник a на b.
r = int(input('Введите длину радиуса: '))
a = int(input('Введите длину прямоугольника: '))
b = int(input('Введите ширину прямоугольника: '))
gip1 = a**2 + b**2
if r*2>=gip1**0.5:
    print("Прямоугольник можно вписать в окружность")
else:
    print('Прямоугольник нельзя вписать в окружность')

# 1. Обычно в языках программирования есть множество различных фреймворков, и каждый из них относится
# к определенному языку программирования и специальности.
# Напишите программу, которая по названию фреймворка будет определять язык и профессию человека.
#
# Flask, Django, Fast-API – Python(<framework>),Backend-dev
# Angular, React, Vue – JavaScript/TypeScript(<framework>),Frontend-dev
# Flutter, React Native – JavaScript(<framework>),Cross-Mobile-dev
# Pandas, skit-learn, keras – Python(<framework>),Data-Scientist
# В случае если фреймворк еще не известен – выведете "модель еще не обучена"
#
# nam1 = input('Введите название фреймворка: ')
# if nam1 == 'Python' and nam1 =='Python':
#     print("Профессия: Backend-dev")
#     print('Языки программирования:Flask, Django, Fast-API')
# #elif nam1 == pyt2:
#     print('Профессия: Data-Scientist')
#     print('Языки программирования: Pandas, skit-learn, keras')
# elif nam1 == 'JavaScript/TypeScript':
#     print('Профессия: Frontend-dev')
#     print('Языки программирования: Angular, React, Vue')
# elif nam1 == 'JavaScript':
#     print('Профессия: Cross-Mobile-dev')
#     print('Языки программирования: Flutter, React Native')
# else:
#     print('модель еще не обучена')