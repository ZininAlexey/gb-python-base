# 1) Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 5
b = 10
c = a + b

d = input("Введите текст: ")
e = input("Введите число: ")

print("Вы ввели текст: ", d)
print("Вы ввели число: ", e)

# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input("Введите количество секунд "))

time_hours = user_time // 3600
time_minutes = (user_time - time_hours * 3600) // 60
time_seconds = user_time - time_hours * 3600 - time_minutes * 60

print("часов:", time_hours, "; минут:", time_minutes, "; секунд:", time_seconds)

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = input("Введите целое положительное число ")
number_nn = number_n + number_n
number_nnn = number_n + number_nn
number_n = int(number_n)
number_nn = int(number_nn)
number_nnn = int(number_nnn)
number_summ = number_n + number_nn + number_nnn

print("Cумма чисел n + nn + nnn =", number_summ)

# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = int(input("Введите целое положительное число: "))
max_number = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
print("Максимальная цифра во введенным вами числе равна", max_number)

# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма прибыль выручка больше издержек, или убыток издержки больше выручки. Выведите соответствующее сообщение.

revenue = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))
fin_resault = revenue - cost

if fin_resault < 0:
    print("Получен отрицательный фин результат (Убыток): ", fin_resault)
else:
    print("Получен положительный фин результат: ", fin_resault)

if fin_resault > 0:
    profit_margin = (fin_resault / revenue) * 100
print("Рентабельность продаж = ", profit_margin, "%")

if fin_resault > 0:
    emp_count = int(input("Введите число сотрудников фирмы: "))
profit_per_emp = fin_resault / emp_count
print("Прибыль фирмы в расчете на одного сотрудника = ", profit_per_emp)

# 6) Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.

resault_first_day = int(input("Введите свой результат за первый день пробежки (количество километров): "))
goal_result = int(input("Введите желаемый результат (количество километров): "))
day = 0

while resault_first_day <= goal_result:
    day += 1
    resault_first_day = resault_first_day + resault_first_day * 0.1
    print(day, "-й день:", resault_first_day)