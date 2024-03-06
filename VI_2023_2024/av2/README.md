﻿# Аудиториска вежба 2 - Вовед во Python

## Задача 1 - Swap на елементи во листа од торки

Да се напише функција која за дадена листа од торки во облик [('a', 1), ('b', 2), ('c', 3)] ќе направи swap на елементите во торките така што елементот на позиција 0 ќе биде елемент на позиција 1 и обратно. Да се користи list comprehension.
Пример влез:
[('a', 1), ('b', 2), ('c', 3)]

Пример излез:
[(1, 'a'), (2, 'b'), (3, 'c')]


## Задача 2 - Движење на агенти

Да се дефинира класа за Агент кој ја чува својата позиција (координати x и y) во некој простор. Да се дефинира метод кој го означува движењето на агентот во просторот. Потоа да се дефинираат агенти кои имплементираат специфично движење (лево, десно, горе, долу). Извршете 5 движења за секој од агентите и испечатете ја позицијата на агентот во секој чекор.

## Задача 3 - Вгнездени list comprehension
Користејќи list comprehension дадена матрица составена од броеви да се промени секој елемент така што ќе се помножи со 2. Секој елемент на матрицата се чита од тастатура така што прво се читаат N и M (број на редици и колони) а потоа во секој ред се читаат елементите одделени со празно место

Пример влез:
4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Излез:
[[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]


## Задача 4 - Вгнездени list comprehension со проверки
Користејќи list comprehension дадена матрица составена од броеви да се промени секој елемент така што ако припаѓа во горната половина(индексот на редицата е помеѓу 0 и n/2) треба да се помножи со 2 а ако припаѓа на долната половина треба да се помножи со 3. Секој елемент на матрицата се чита од тастатура така што прво се читаат N и M (број на редици и колони) а потоа во секој ред се читаат елементите одделени со празно место.

Пример влез:
4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Излез:
[[2, 4, 6, 8], [2, 4, 6, 8], [3, 6, 9, 12], [3, 6, 9, 12]]



## Дополнителни ресурси:
https://www.datacamp.com/community/tutorials/python-list-comprehension
https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/