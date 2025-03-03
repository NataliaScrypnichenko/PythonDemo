# методи стрінги
# довжина st len()-ф-я показує скільки символів є (7)
st=' 21111234 !'
print(len(st))
# методи пишуться через крапку .index()--повертає нам номер першого елемента, який ми шукаємо 2=(під індексом 5),
# коли є багато 2 то буде видавати перший індекс першoї 2, а інші ні, щоб знайти інд.останьої .rindex('2').
# Якщо ми пишемо не присутню цифру чи символ, то видає помилку,
print(st.index('2'))
print(st.rindex('2'))

#а якщо щоб програма працювала далі, то використовую .find = то дає-1 показує що не існує.rfind('2')=дає останю
print(st.find('9'))
print(st.find('2'))
print(st.rfind('2'))

 # str.lower()
# Перетворює всі літери рядка в нижній регістр.
text = "Hello World"
print(text.lower())  # "hello world"

# .islower()
# Метод str.islower() перевіряє, чи всі літери в рядку є малими.
# Якщо рядок містить хоча б одну велику літеру – повертає False.
print("hello".islower())    # True (всі літери малі)
print("Hello".islower())    # False (є велика літера "H")
print("123".islower())      # False (немає літер)
print("hello!".islower())   # True (літери малі, цифри/символи ігноруються)
print("python 3".islower()) # True (цифри та пробіли не впливають)
print("".islower())         # False (порожній рядок)
# 🔹 Важливі деталі:
# Метод ігнорує цифри та символи, перевіряє лише літери.
# Якщо в рядку немає літер взагалі (лише цифри, пробіли, символи) – повертає False.
# Порожній рядок також дає False.
# ✅ Використання:
# Перевірка, чи користувач написав текст маленькими літерами
text = input("Введіть текст: ")
if text.islower():
    print("Текст повністю у нижньому регістрі!")
else:
    print("Є великі літери або текст не містить літер.")
# Переведення тексту в нижній регістр перед перевіркою:
word = " Hello ".strip().lower()
print(word.islower())  # True (прибираємо пробіли, переводимо у нижній регістр)
# Аналіз тексту в чат-ботах:
message = "hello"
if message.islower():
    print("Користувач пише спокійно 😊")
# Метод islower() зручний для перевірки стилю написання тексту, обробки введених даних та аналізу повідомлень. 🚀

# str.upper()-
# перетворює всі літери рядка у великі.
print("hello".upper())      # "HELLO"
print("Hello World".upper())# "HELLO WORLD"
print("python3".upper())    # "PYTHON3" (цифри не змінюються)
print("123abc".upper())     # "123ABC"
print("Привіт!".upper())    # "ПРИВІТ!"
print(text.upper())  # "HELLO WORLD"
# 🔹 Важливі деталі:
# Тільки літери змінюють регістр, цифри та символи залишаються незмінними.
# Не змінює вихідний рядок, а повертає новий.
# ✅ Використання:
# Переведення тексту у верхній регістр (заголовки, оголошення):
title = "breaking news: python 3.12 released!"
print(title.upper())  # "BREAKING NEWS: PYTHON 3.12 RELEASED!"
# Перевірка введених даних (наприклад, кодів):
code = input("Введіть промокод: ").upper()
if code == "DISCOUNT2025":
    print("Код активовано!")
# Переведення користувацького тексту у ВЕЛИКІ ЛІТЕРИ:
user_input = input("Напишіть коментар: ")
print(user_input.upper())  # Виведе у верхньому регістрі


# .isupper()
# Метод str.isupper() перевіряє, чи всі літери в рядку є великими.
# Якщо рядок містить хоча б одну маленьку літеру – повертає False.
print("HELLO".isupper())    # True (всі літери великі)
print("Hello".isupper())    # False (є маленька літера "e")
print("123".isupper())      # False (немає літер)
print("HELLO!".isupper())   # True (літери великі, а цифри/символи ігноруються)
print("PYTHON 3".isupper()) # True (цифри та пробіли не впливають)
print("".isupper())         # False (порожній рядок)
#  Важливі деталі:
# Метод ігнорує цифри та символи, перевіряє лише літери.
# Якщо в рядку немає букв взагалі (наприклад, лише цифри або пробіли) – повертає False.
# Порожній рядок також дає False.
# ✅ Використання:
# Перевірка, чи користувач написав текст ВЕЛИКИМИ ЛІТЕРАМИ:
text = input("Введіть текст: ")
if text.isupper():
    print("Текст повністю у верхньому регістрі!")
else:
    print("Є маленькі літери або текст не містить літер.")
# Форматування тексту перед перевіркою:
word = " hello ".strip().upper()
print(word.isupper())  # True (спочатку прибираємо пробіли, потім переводимо у верхній регістр)
# Перевірка тексту в чат-ботах:
message = "STOP!"
if message.isupper():
    print("Користувач кричить 😡")
# Метод isupper() часто використовується для перевірки тексту на "крикливість", перевірки формату введених даних або при обробці текстів. 🚀

# str.capitalize()
# Робить першу літеру великою, а решту – малими.Не змінює сам рядок, а повертає новий із зміненим регістром.
# Метод capitalize() корисний для форматування текстів, назв та повідомлень. 🚀
text = "hello world"
print(text.capitalize())  # "Hello world"
print("hello world".capitalize())  # "Hello world"
print("PYTHON".capitalize())       # "Python" (перша велика, інші малі)
print("123abc".capitalize())       # "123abc" (цифри не змінюються)
print("hELLO wORLD".capitalize())  # "Hello world"
print(" привет мир ".capitalize()) # " привет мир " (пробіли залишаються)
# 🔹 Важливі деталі:
# Змінює тільки перший символ, а інші переводить у нижній регістр.
# Цифри та символи на початку не змінюються, якщо немає літер.
# Не змінює вихідний рядок, а повертає новий.
# ✅ Використання:
# Форматування імен:
name = "john doe"
formatted_name = name.capitalize()
print(formatted_name)  # "John doe"
# Форматування заголовків повідомлень:
message = "wELCOME TO PYTHON!"
print(message.capitalize())  # "Welcome to python!"
# Очищення тексту перед виводом:
text = input("Введіть текст: ").strip().capitalize()
print(text)

#str.title()
# Робить першу літеру кожного слова великою.
print("hello world".title())  # "Hello World"

# str.strip()
# Видаляє пробіли (та інші непотрібні символи) з початку та кінця рядка
text = "   hello world   "
print(text.strip())  # "hello world"

# str.lstrip()
# lstrip() – прибирає пробіли зліва
print(text.lstrip())  # "hello world   "

# str.rstrip()
# rstrip() – прибирає пробіли справа.
print(text.rstrip())  # "   hello world"

# str.replace(old, new, count)
# Замінює всі входження підрядка old на new.використовується для заміни підрядка у рядку на інший.
# old – підрядок, який потрібно замінити.
# new – підрядок, на який буде здійснена заміна.
# count (необов’язковий) – скільки разів замінити (None або не вказаний – замінює всі).
# 1. Заміна всіх входжень
st = "banana banana banana"
new_st = st.replace("banana", "apple")
print(new_st)  # "apple apple apple"
print("hello world".replace("world", "Python"))  # "hello Python"
#  Заміна тільки перших N входжень (count)
st = "banana banana banana"
new_st = st.replace("banana", "apple", 2)  # Замінити тільки перші 2 рази
print(new_st)  # "apple apple banana"
#  Заміна тільки перших N входжень (count)
st = "banana banana banana"
new_st = st.replace("banana", "apple", 2)  # Замінити тільки перші 2 рази
print(new_st)  # "apple apple banana"
# Видалення символів (заміна на "")
st = "Hello, world!"
new_st = st.replace(",", "").replace("!", "")
print(new_st)  # "Hello world"
#  Заміна пробілів на -
st = "hello world how are you"
new_st = st.replace(" ", "-")
print(new_st)  # "hello-world-how-are-you"
# 🔹 Важливі деталі:
# Не змінює вихідний рядок, а повертає новий.
# Чутливий до регістру:
print("Hello".replace("h", "X"))  # "Hello" (немає "h" з малої літери)
# Працює швидше, ніж re.sub(), якщо потрібно замінити простий рядок.
# Якщо рядок не містить old, метод повертає той самий рядок без змін.
# ✅ Використання:
# 🔹 Очищення тексту від небажаних символів:
st = "Hello! How's it going?"
st = st.replace("!", "").replace("?", "").replace("'", "")
print(st)  # "Hello Hows it going"
# Форматування чисел:
number = "1,234,567"
clean_number = number.replace(",", "")
print(int(clean_number))  # 1234567
# Метод replace() – простий і зручний спосіб заміни тексту у Python! 🚀


# str.find(sub)
# Повертає індекс першого входження sub. Якщо не знайдено – -1.
print("hello world".find("world"))  # 6
print("hello world".find("Python"))  # -1

# str.count(sub)
# Підраховує кількість входжень підрядка sub.
print("hello hello world".count("hello"))  # 2

# str.startswith(prefix), str.endswith(suffix)
# Перевіряє, чи починається (startswith) або закінчується (endswith) рядок заданим підрядком.
words = ["hello", "world"]
print(" ".join(words))  # "hello world"
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

# str.isdigit()
# isdigit() – чи складається рядок лише з цифр.Якщо рядок містить хоча б один нецифровий символ – повертає False.
print("123".isdigit())  # True
print("12345".isdigit())   # True (лише цифри)
print("3.14".isdigit())    # False (є крапка)
print("²³".isdigit())      # True (верхній індекс – теж цифри)
print("10 000".isdigit())  # False (є пробіл)
print("abc123".isdigit())  # False (є букви)
print("١٢٣".isdigit())     # True (арабські цифри)
print("".isdigit())        # False (порожній рядок)
# 🔹 Важливі деталі:
# Перевіряє, чи всі символи – цифри (0-9).
# Не допускає знаки "+" та "-", десяткову крапку, пробіли.
# Підтримує цифрові символи Unicode, наприклад, верхні/нижні індекси та арабські цифри.
# ✅ Використання:
# Перевірка введених даних:
user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це число!")
else:
    print("Це не число!")
# Фільтрація цифр у тексті:
text = "Телефон: 098-765-4321"
digits = "".join(char for char in text if char.isdigit())
print(digits)  # "0987654321"
# Метод isdigit() корисний для перевірки, чи рядок містить лише цифри перед конвертацією в int. 🚀

# str.isalpha()
# isalpha() – чи складається лише з букв.
print("hello".isalpha())  # True

# str.isalnum()
# isalnum() – чи містить тільки букви та/або цифри.
print("hello123".isalnum())  # True
print("hello 123".isalnum())  # False (бо є пробіл)

# str.zfill(width)
# Доповнює рядок нулями зліва до заданої довжини width.
print("42".zfill(5))  # "00042"

# str.center(width, fillchar)
# Вирівнює рядок по центру, заповнюючи пробілами або символом fillchar.
print("hello".center(10, "-"))  # "--hello---"

# .isspace()
# Метод str.isspace() перевіряє, чи містить рядок тільки пробіли,
# табуляції (\t), переведення рядка (\n)
# або інші пробільні символи. Якщо так – повертає True, інакше False.Метод корисний,
# коли потрібно перевірити, чи складається рядок лише з пробільних символів, наприклад, перед обробкою введених користувачем даних.
print("   ".isspace())   # True (тільки пробіли)
print("\t\n".isspace())  # True (табуляція + новий рядок)
print("hello".isspace()) # False (є символи)
print(" hello ".isspace()) # False (є пробіли, але також є букви)
print("".isspace())  # False (порожній рядок)

# .isdecimal()
# Метод str.isdecimal() перевіряє, чи складається рядок тільки з десяткових цифр (0-9).
# Якщо так – повертає True, інакше False.
print("123".isdecimal())   # True (тільки цифри 0-9)
print("٣٤٥".isdecimal())   # True (арабські цифри)
print("12.3".isdecimal())  # False (містить крапку)
print("⅕".isdecimal())     # False (дробові символи)
print("²".isdecimal())     # False (степінь, не стандартна цифра)
print("123abc".isdecimal()) # False (містить літери)
print("".isdecimal())      # False (порожній рядок)
# Важливо:
# isdecimal() перевіряє тільки десяткові цифри.
# Він не працює з дробовими або надрядковими числами (наприклад, ² або ⅕).
# Якщо потрібно перевірити всі види чисел, краще використовувати .isdigit(), яке приймає більше числових символів.
# 🔍 Різниця між .isdecimal(), .isdigit() і .isnumeric():
# Метод	Десяткові цифри (0-9)	Надрядкові (², ³)	Дроби (⅕, ½)	Арабські цифри (٣٤٥)
# isdecimal()	✅ Так	❌ Ні	❌ Ні	✅ Так
# isdigit()	✅ Так	✅ Так	❌ Ні	✅ Так
# isnumeric()	✅ Так	✅ Так	✅ Так	✅ Так
# Якщо потрібно перевірити лише звичайні цифри (0-9) – використовуйте isdecimal().
# Якщо хочете врахувати степені та інші цифрові символи – використовуйте isdigit().
# Якщо потрібно перевірити будь-які числові символи (навіть дроби) – використовуйте isnumeric().

# isdigit()
# Метод str.isdigit() перевіряє, чи складається рядок тільки з цифрових символів.
# Якщо всі символи – цифри, метод повертає True, інакше False.
print("123".isdigit())   # True (звичайні цифри 0-9)
print("٣٤٥".isdigit())   # True (арабські цифри)
print("²³".isdigit())    # True (степені ², ³ вважаються цифрами)
print("12.3".isdigit())  # False (є крапка)
print("⅕".isdigit())     # False (дробовий символ)
print("123abc".isdigit()) # False (літери)
print("".isdigit())      # False (порожній рядок)

# .isalpha()
# Метод str.isalpha() перевіряє, чи складається рядок лише з букв (алфавітних символів).
# Якщо всі символи – літери (без цифр, пробілів або спеціальних символів), метод повертає True, інакше False.
# Метод працює з будь-якими літерами алфавітів (латиниця, кирилиця, грецький алфавіт тощо).
# Якщо у рядку хоч один не-алфавітний символ (цифра, пробіл, пунктуація), isalpha() поверне False.
print("Hello".isalpha())   # True (тільки літери)
print("Привіт".isalpha())  # True (українські літери)
print("Python3".isalpha()) # False (є цифра)
print("Hello!".isalpha())  # False (є спеціальний символ)
print(" ".isalpha())       # False (пробіл)
print("".isalpha())        # False (порожній рядок)
# Використання:
# Перевірка, чи ім'я користувача містить лише букви
name = "Іван"
if name.isalpha():
    print("Ім'я коректне")
else:
    print("Ім'я має містити лише букви")
# Використання разом із .replace() для перевірки складених слів
full_name = "Jean-Luc"
print(full_name.replace("-", "").isalpha())  # True
# Якщо потрібно перевірити слова з пробілами або дефісами, перед перевіркою їх варто очистити (replace, strip).

# .endswith()
# Метод str.endswith(suffix[, start, end]) перевіряє, чи закінчується рядок вказаним суфіксом (suffix).
# Якщо так – повертає True, інакше False.
# string.endswith(suffix, start, end)
# suffix – рядок або кортеж рядків, які потрібно перевірити.
# start (необов'язково) – початковий індекс перевірки.
# end (необов'язково) – кінцевий індекс перевірки.
print("hello.txt".endswith(".txt"))  # True (рядок закінчується на ".txt")
print("document.pdf".endswith(".txt"))  # False (закінчується на ".pdf")
# Перевірка кількох суфіксів
print("report.docx".endswith((".pdf", ".docx")))  # True (є серед варіантів)
# Перевірка з обмеженням області пошуку
print("example.py".endswith(".py", 0, 7))  # False (перевіряємо тільки "example")
# Використання з URL
print("https://example.com".endswith((".com", ".org")))  # True
#  Важливі деталі:
# Параметри start та end дозволяють перевірити тільки певну частину рядка.
# Можна передавати кортеж суфіксів для перевірки декількох варіантів.
# Метод чутливий до регістру ("Hello".endswith("o") → True, "Hello".endswith("O") → False).
# Використання:
# Перевірка розширення файлу:
filename = "data.csv"
if filename.endswith(".csv"):
    print("Це файл CSV")
# Перевірка домену сайту:
url = "https://example.org"
if url.endswith((".com", ".org", ".net")):
    print("Популярний домен")
#Фільтрація файлів у списку:
files = ["report.pdf", "image.jpg", "script.py", "notes.txt"]
pdf_files = [f for f in files if f.endswith(".pdf")]
print(pdf_files)  # ['report.pdf']

# .startswith()
# Метод str.startswith(prefix[, start, end]) перевіряє, чи починається рядок із вказаного префікса (prefix).Метод startswith() корисний для перевірки
# початку рядків, наприклад, у файлах, URL-адресах або текстових документах.
# Якщо так – повертає True, інакше False.
# prefix – рядок або кортеж рядків для перевірки.
# start (необов'язково) – початковий індекс перевірки.
# end (необов'язково) – кінцевий індекс перевірки.
print("hello world".startswith("hello"))  # True (рядок починається з "hello")
print("hello world".startswith("world"))  # False (не на початку)
# Перевірка кількох варіантів
print("data.csv".startswith(("data", "info")))  # True (починається з "data")
# Перевірка з обмеженням області пошуку
print("example.py".startswith("py", 8))  # True (перевіряємо з 8-го символу)
print("example.py".startswith("py", 0, 7))  # False (перевіряємо лише "example")
# Використання з URL
print("https://example.com".startswith("https://"))  # True
print("http://example.com".startswith(("http://", "https://")))  # True
# Важливі деталі:
# Метод чутливий до регістру: "Hello".startswith("H") → True, "Hello".startswith("h") → False.
# start і end дозволяють перевіряти тільки частину рядка.
# Можна передавати кортеж префіксів для перевірки кількох варіантів.
# ✅ Використання:
# Перевірка протоколу URL:
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print("Це веб-адреса")
# Фільтрація файлів за префіксом:
files = ["log_2024.txt", "report.pdf", "log_2023.txt", "data.csv"]
logs = [f for f in files if f.startswith("log_")]
print(logs)  # ['log_2024.txt', 'log_2023.txt']
# Перевірка формату номера телефону:
phone = "+380971234567"
if phone.startswith("+380"):
    print("Український номер")

# .translate()
# Метод str.translate(table) замінює символи в рядку відповідно до таблиці замін.
# Ця таблиця створюється за допомогою str.maketrans()
# string.translate(table)
# table – це словник або об'єкт, створений через str.maketrans(), де вказані заміни.
# 1. Видалення символів
st = "Hello, World!"
table = str.maketrans("", "", ",!")  # Видаляємо "," та "!"
print(st.translate(table))  # "Hello World"
# Заміна символів
st = "hello world"
table = str.maketrans("hw", "HW")  # Замінюємо "h" на "H", "w" на "W"
print(st.translate(table))  # "Hello World"
# Комбінована заміна + видалення
st = "hello, world!"
table = str.maketrans({"h": "H", "w": "W", ",": None, "!": None})  # Видаляємо "," і "!"
print(st.translate(table))  # "Hello World"
# 🔹 Важливі деталі:
# Не змінює вихідний рядок, а повертає новий.
# Працює швидше, ніж replace(), якщо потрібно замінити багато символів одночасно.
# Якщо у maketrans() передати None або порожній рядок як другий аргумент – символи просто видаляються.
# ✅ Використання:
# 🔹 Очищення тексту від непотрібних символів:
st = "Hello! How's it going?"
table = str.maketrans("", "", "!?'")  # Видаляємо знаки пунктуації
print(st.translate(table))  # "Hello Hows it going"
# Швидка заміна кількох символів:
st = "apple orange banana"
table = str.maketrans("ao", "AO")  # "a" → "A", "o" → "O"
print(st.translate(table))  # "Apple OrAnge bAnAnA"
# Метод translate() – потужний інструмент для заміни та видалення символів у рядках! 🚀