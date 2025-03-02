# continue = є допоміжними операторами в роботі з циклами
# цикл for записує i цифру в діапазоні 500,якщо і==5 вона повина виконати break,
# якщо цього(if i==5:break) не буде то в кінці буде значення в кінці цього циклу вивидеться 'the end',
# у нас виходить (0,1,2,3,4)= це означає що в даному випадку (і)відпрацювало і break мене викинуло взагалі(він викидує
# і не дає далі працювати)тобто після break воно не працює нічого(break-він зупиняє і повністю виходить із циклу)
for i in range(500):
    if i==5:
        break
    print(i)
else:
    print('the end')
print('some')
# continue- не дає можливості закінчити цикл до кінця
for i in range(10):
    if i==5:
        continue
    print(i)
else:
    print('the end')
print('some')
# не виводить 5,3,7
for i in range(10):
    if i==5 or i==3 or i==7:
        continue
    print(i)
else:
    print('the end')
print('some')
# continue,break працює в циклі while, але потрібно пере писати під while
