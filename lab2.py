a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

average = (a + b + c) / 3

print("Среднее арифметическое:", average)


number = int(input("Введите целое число: "))

if number % 3 == 0 and number % 5 == 0:
    print("Число делится на 3 и на 5 одновременно")
else:
    print("Число не делится на 3 и на 5 одновременно")



n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)


n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        count += 1

print("Количество чётных чисел:", count)