# Вводится два числа с клавиатуры. Выведите диапазон между этими двумя числами.
# num1 = int(input("Введите первое число: "))
# num2 = int(input('Введите второе число: '))
# i = num1
# while i <= num2:
#     print(i)
#     i+=1
# Выведите все нечетные числа, которые делятся на 3 в диапазоне от 100 до 250.
# i = 100
# while i <= 250:
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
#     i += 1

# Вводится n натуральных чисел с клавиатуры. Найти сумму чисел и максимальное их них.
n = int(input('Введите целое число: '))
sum = 0
while n > 0:
    n // 10
    sum += n
print(sum)
