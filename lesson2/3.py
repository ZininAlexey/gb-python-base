# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    month = input("Введите номер месяца в виде целого числа от 1 до 12: ")
    if not month.isnumeric():
        print("Вы ввели не число или не целое число. Попробуйте снова: ")
    elif not 1 <= int(month) <= 12:
        print("Ваше число не диапазоне от 1 до 12. Попробуйте снова")
    else:
        print("Вы ввели число в правильном диапазоне.")
        break

lst = ["зима", "весна", "лето", "осень"]

month = int(month)
if 1 <= month <= 2 or month == 12:
    print(f'Введеный вами номер месяца года относится ко времени года : {lst[0]}')
elif 3 <= month <= 5:
    print(f"Введеный вами номер месяца года относится ко времени года : {lst[1]}")
elif 6 <= month <= 8:
    print(f"Введеный вами номер месяца года относится ко времени года : {lst[2]}")
elif 9 <= month <= 11:
    print(f"Введеный вами номер месяца года относится ко времени года : {lst[3]}")

new_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

winter = new_dict.get("зима")
sprint = new_dict.get("весна")
summer = new_dict.get("лето")
autumn = new_dict.get("осень")
for i in winter:
    if i == month:
        print(f"Введеный вами номер месяца года относится ко времени года : {list(new_dict.keys())[0]}")
    else:
        break
for i in sprint:
    if i == month:
        print(f"Введеный вами номер месяца года относится ко времени года : {list(new_dict.keys())[1]}")
    else:
        break
for i in summer:
    if i == month:
        print(f"Введеный вами номер месяца года относится ко времени года : {list(new_dict.keys())[2]}")
    else:
        break
for i in autumn:
    if i == month:
        print(f"Введеный вами номер месяца года относится ко времени года : {list(new_dict.keys())[3]}")
    else:
        break
