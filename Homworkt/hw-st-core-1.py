# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st ='as 23 fdfdg544'
# Створюємо порожній рядок result, куди будемо додавати цифри
result = ""
# Перебираємо кожен символ рядка.
for i in st:
    # Перевіряємо, чи це цифра
    if i.isdigit():
        # Додаємо її до result разом із комою.
        result += i + ","
# Видаляємо зайву кому в кінці
print(result.rstrip(","))
