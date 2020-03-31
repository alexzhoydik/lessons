a = 987
b = 'картошечка'
c = bool(56)
print(a)
print(b)
print(c)

name = str(input('Введите свое имя: '))
surname = str(input('Введите свою фамилию: '))
age = int(input('Введите свой возраст: '))
print(f'Ваши данные: {name} {surname} {age}')

sec = int(input())
m = (sec // 60)%60
h = sec // 3600
s = (sec - h * 36 - m * 6)%60
print(f'{h}:{m}:{s}')

n = int(input('Введите число: '))
m = int(n * 11)
o = int(n * 111)
print(n + m + o)

n = int(input('Введите число: '))
current_max = 0
m = n

while m > 0:
    digit = m % 10
    if digit > current_max:
        current_max = digit
        if current_max == 9:
            # break
    m = m // 10
print('Наибольная цифра:', current_max)

rev = float(input('Введите выручку:'))
c = float(input('Введите издержки:'))

result = rev - c

if result > 0:
    print('Сальдо положительное:', rev)
    print('Рентабильность:', result/rev)
    people = int(input('Введите численность сотрудников:'))
    print(f'Прибыль на одного сотрудника: {result/people:.f2}')
elif result < 0:
    print('Убыток:', result)
else:
    print('Нулевое сальдо')

while True:
    days = 1
    start_km = int(input('Начало тренировок: '))
    last_km = int(input('Конец тренировок: '))
    if start_km > last_km:
        print('Неверно')
    else:
        while start_km < last_km
            start_km +=  start_km * 0.1
            days += 1
        print('Добьешься успеха за {} дней'.format(days))
        break

