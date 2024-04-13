# '''
# Уровень 1.1 задачника Python
# '''
#
# '''
# №1
# Дано число. Проверьте, отрицательное оно или нет. Выведите об этом информацию в консоль.
# '''
# # x = int(input('Enter your number here >>'))
# # if x < 0:
# #     print('This number is negative')
# # else:
# #     print('This number is positive')
#
# '''№2
# Дана строка. Выведите в консоль длину этой строки.
# '''
# # x = input('Enter your string here >>')
# # print(len(str(x)))
# #
# '''
# №3
# Дана строка. Выведите в консоль последний символ строки.
# '''
# x = input('Enter your string here >>')
# x =str(x)
# print(str(x[len(x)-1]))
#
# '''№4
# Дано число. Проверьте, четное оно или нет.
# '''
# # x = int(input('Enter your string here >>'))
# # if x % 2 == 0:
# #     print('The number is pair')
# # else:
# #     print('The number is impair')
#
# '''№5
# Даны два слова. Проверьте, что первые буквы этих слов совпадают.
# '''
# # a, b = map(str, input('Enter 2 strings here >>').split('-'))
# # print(a[:2])
# # print(b[:2])
# # if a[:2] == b[:2] :
# #     print( True)
# # else:
# #     print(False)
# '''
# №6
# Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.
# '''
# # x = input('Enter your string here >>')
# # x = str(x)
# # if x[len(x)-1] == 'ь':
# #     print(x[len(x)-2])
# # else:
# #     print(x[len(x) - 1])
#
# '''
# Уровень 1.2 задачника Python
# '''
# '''№1
# Дано число. Выведите в консоль первую цифру этого числа.
# '''
# # x = int(input('Enter your number here >>'))
# # list1 = []
# # for el in str(x) :
# #     list1.append(el)
# # print('The first character is', a', list1[0])
#
# #x = int(input('Enter your string here >>'))
# # c = len(str(x))
# # list1 = []
# # print(c)
# # while c > 0 :
# #     a = x % 10
# #     x //= 10
# #     list1.append(a)
# #     c -= 1
# # print(list1)
# # print(list1[len(str(x))])
# # print(list1[len(str(x))-2])
#
# '''№2
# Дано число. Выведите в консоль последнюю цифру этого числа.
# '''
#
# # x = int(input('Enter your number here >>'))
# # a = x % 10
# # print('The last character is', a)
#
# '''№3
# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
# '''
# # x = int(input('Enter your number here >>'))
# # list1 = []
# # for el in str(x) :
# #     list1.append(el)
# # print('The sum of the first and last number is', int(list1[0])+int(list1[len(str(x))-1]))
#
# '''№4
# Дано число. Выведите количество цифр в этом числе.
# '''
# # x = int(input('Enter your number here >>'))
# # c = len(str(x))
# # print('The number of character is :', c)
#
# '''№5
# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
# '''
# # a, b = map(int, input('Enter 2 numbers here separeted with "-">>').split('-'))
# # a = str(a)
# # b = str(b)
# # #print((a[0]))
# # #print((b[0]))
# # if (a[0]) == (b[0]) :
# #     print(True)
# # else:
# #     print(False)
#
# '''
# №6
# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него следующий срез:
# [1, 2, 3]
# '''
# # list_1 = [1, 2, 3, 4, 5, 6]
# # print(list_1[:3])
#
# '''
# Уровень 1.3 задачника Python
# '''
# ''' №1 Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.
# '''
# # x = input('Enter your string here >>')
# # c = len(str(x))
# # if c == 0 or c ==1 :
# #     while c ==1:
# #         print('Enter an other string')
# #         c  +=1
# # else:
# #     print(x[len(x)-2])
#
# '''№2
# Даны два целых числа. Проверьте, что первое число без остатка делится на второе
# '''
# # a, b = map(int, input('Enter 2 numbers here separeted with "-">>').split('-'))
# # c = False
# # if a % b == 0:
# #     c = True
# # if c == True:
# #     print('The second number divide the fisrt number')
# # else:
# #     print('The second number do not divide the fisrt number')
#
# '''№3
# Дана некоторая строка:
# 'abcde'
# Получите список ее символов:
# ['a', 'b', 'c', 'd', 'e']
# '''
# # str_1 = 'abcde'
# # list_1 = []
# # for el in str_1:
# #     list_1.append(el)
# # print(list_1)
#
# '''№4
#
# Дан список:
#
# [1, 2, 3, 4, 5, 6]
# Получите из него следующий срез:
#
# [3, 4, 5]
# '''
# # list_1 = [1, 2, 3, 4, 5, 6]
# # print(list_1[2:5])
#
# '''№5
# Дан словарь с датой:
# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# }
# Из элементов этого словаря соберите дату в следующем формате:
# '2025-12-31'
# '''
# # dict_1 = {
# # 	'year' : '2025',
# # 	'month': '12',
# # 	'day'  : '31',
# # }
# # print(dict_1['year'],'-', dict_1['month'],'-', dict_1['day'])
#
# '''Уровень 1.4 задачника Python
# №1
# Выведите в консоль все целые числа от 1 до 100.
# '''
# # for i in range(101):
# #     print(i, end='-')
#
# '''№2
# Выведите в консоль все целые числа от -100 до 0.
# '''
# # x = -100
# # while x <=0 :
# #      print(x, end='/')
# #      x+=1
#
#
# '''№3
# Выведите в консоль все целые числа от 100 до 1.
# '''
# # x = 100
# # while x >=0 :
# #      print(x, end='-')
# #      x-=1
#
# # for i in range(100:-1):
# #      print(i, end='-')
#
# '''№4
# Выведите в консоль все четные числа из промежутка от 1 до 100.
# '''
# # x = 0
# # while x <=100 :
# #      print(x, end='/')
# #      x+=2
#
# '''№5
# Выведите в консоль все числа кратные трем в промежутке от 1 до 100
# '''
# # for i in range(1,101):
# #      if i % 3 == 0:
# #           print(i, end='/')
# #
#
# # x = 0
# # while x < 100:
# #      if x % 3 == 0 :
# #           print(x)
# #      x += 1
#
# '''№6
# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него два последних элемента:
# [5, 6]
# '''
# # list_1 = [1, 2, 3, 4, 5, 6]
# # print(list_1[4:6])
#
# '''№7
# Дана некоторая строка:
# 'abcdeabc'
# Получите сет ее символов:
#
# {'a', 'b', 'c', 'd', 'e'}
# '''
#
# # string_1 = 'abcdeabc'
# # list_1 = list(string_1)
# # print(list_1)
# # set_1 = set(list_1)
# # print(set_1)
#
# '''Уровень 1.5 задачника Python
# №1
# Найдите сумму всех целых чисел от 1 до 100.
# '''
# # a = 0
# # summa = 0
# # while a <= 100:
# #     summa +=a
# #     a+1
# #     print(summa)
#
#
# # summa = 0
# # for i in range (1,100):
# #     summa+=i
# # print(summa)
#
# '''№2
# Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
# '''
# # summa = 0
# # for i in range (1,100):
# #     if i % 2 == 0:
# #         summa += i
# # print(summa)
#
# '''№3
# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.'''
#
# # summa = 0
# # for i in range (1,100):
# #     if i % 2 != 0:
# #         summa += i
# # print(summa)
#
# '''№4
# Даны два целых числа. Найдите остаток от деления первого числа на второе.'''
#
# # x, y = map(int, input('Enter 2 numbers >>').split('/'))
# # print('Rest of division 1st number to 2nd is', x/y)
#
# '''№5
# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него каждый второй элемент:
# [1, 3, 5]'''
#
# # list_1 = [1, 2, 3, 4, 5, 6]
# # print(list_1[:5:2])
# # print([i for i in list_1 if i % 2 != 0])
#
#
# # res = map(lambda x: x % 2 ==0, list_1)
# # res_1 = filter(lambda x: x % 2 ==0, list_1)
# # print(list(res))
# # print(list(res_1))
#
# '''Уровень 1.6 задачника Python
#
# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму элементов этого списка.
# '''
# # summa = 0
# # for el in [1, 2, 3, 4, 5] :
# #     summa += el
# # print(summa)
#
# '''№2
# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратов элементов этого списка.
# # '''
# # summa = 0
# # for el in [1, 2, 3, 4, 5] :
# #     summa += el**2
# # print(summa)
#
# '''№3
# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратных корней элементов этого списка.
# '''
# # summa = 0
# # for el in [1, 2, 3, 4, 5] :
# #     summa += (el)**0.5
# # print(summa)
#
# '''№4
# Дан список с числами:
# [1, 2, -3, 4, -5]
# Найдите сумму положительных элементов этого списка.'''
#
# # summa = 0
# # for el in [1, 2, -3, 4, -5]:
# #     if el >=0:
# #         summa += el
# # print(summa)
#
# '''№5
# Дан список с числами:
# [-1, 2, -3, 4, 5, 11]
# Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.
# '''
# # summa = 0
# # for el in [-1, 2, -3, 4, 5, 11]:
# #     if el >=0 and el < 10:
# #         summa += el
# # print(summa)
#
# '''№6
# Дана некоторая строка:
# 'abcde'
# Переберите и выведите в консоль по очереди все символы с конца строки.'''
#
# # string = 'abcde'
# # c = len(str(string))
# # for i in (string,-1):
# #     print(i)
#
# # string = 'abcde'
# # list_1 = list(string)
# # list_1.reverse()
# # print(list_1)
# # for i in  list_1:
# #     print(i)
#
# '''Уровень 1.7 задачника Python
# №1
# Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Найдите сумму элементов этого словаря.'''
#
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
# #
# # print(dict_1)
# # print(dict_1.items(), sep='/')
# # print(dict_1.keys())
# # print(dict_1.values())
# # print(dict_1.get('b'))
# # summa = 0
# # for el in dict_1.values() :
# #     summa +=el
# # print(summa)
#
# '''№2
# Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Найдите сумму квадратов элементов этого словаря.'''
#
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
# # summa = 0
# # for el in dict_1.values() :
# #     summa +=el**2
# # print(summa)
#
# '''№3
# Дана строка:
# 'abcde'
# Получите список букв этой строки.
# '''
# # strings = 'abcde'
# # print(list(strings))
# # print(strings.split(','))
# '''№4
# Дано некоторое число:
# 12345
# Получите список цифр этого числа.
#
# №5
# Дано некоторое число:
# 12345
# Переверните его:
# '''
# #
# # def number(x):
# #     list_1 = []
# #     for i in str(x):
# #         list_1.append(i)
# #     print(list_1)
# #     list_1.reverse()
# #     #print(list_1)
# #     a = ''.join(list_1)
# #     return 'Перевернуто число',x, '>>', a
# #
# # x = int(input('Введите число >>'))
# # print(number(x))
#
# # A = '12345'
# # print(A[::-1])
#
#
# '''№6
# Дано некоторое число:
# 12345
# Найдите сумму цифр этого числа.
# '''
# # x = 12345
# # summa = 0
#
#
# # for el in str(x):
# #     summa +=int(el)
# # print(summa)
#
# # while x > 0:
# #     a = x % 10
# #     summa += a
# #     x //= 10
# # print(summa)
#
#
# '''Уровень 1.8 задачника Python
# №1
# Дан кортеж с числами:
# (1, 2, 3, 4, 5)
# Найдите сумму элементов этого кортежа.
# '''
# # tuple_1 = (1, 2, 3, 4, 5)
# # print(tuple_1[0])
# # summa = 0
# # for el in (1, 2, 3, 4, 5) :
# #     summa += el
# # print(summa)
#
# '''№2
# Дан список с числами:
# [1, 2, 3, 4, 5, 6]
# Увеличьте каждое число из списка на 10 процентов.
# '''
# # list_1 = [1, 2, 3, 4, 5, 6]
# # res = map(lambda x: x+(x/10),list_1)
# # print(list(res))
#
# '''№3
# Дана строка:
# 'abcdef'
# Получите первых три символа этой строки:
# 'abc'
# '''
# # string_1 = 'abcdef'
# # print(string_1[:3])
#
#
# '''Уровень 1.9 задачника Python
# №1
# Дана строка:
# 'abcdef'
# Получите три последних символа этой строки:
# 'def'
# '''
# # string_1 = 'abcdef'
# # print(string_1[3:7])
#
# '''№2
#
# Дан словарь с числами:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Увеличьте каждое число из словаря в 2 раза:
# {
# 	'a': 2,
# 	'b': 3,
# 	'c': 6,
# 	'd': 8,
# }
# '''
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
#
# # d = dict_1.values()
# # print(d)
# #
# # res = map(lambda x: x*2, dict_1.values())
# # d = list(res)
# # e = d.copy()
# # print(e)
# # print(dict_1)
#
#
#
# # for x, y in dict_1.items():
# # 	dict_1.update({x:y*2})
# # print(dict_1)
#
# '''Уровень 1.10 задачника Python
# №1
# Дана строка:
# 'abcdef'
# Получите каждый второй символ этой строки:
#
# 'acf'
# '''
# # string_1 = 'abcdef'
# # print(string_1[0:6:2])
#
# ''' Уровень 2.1 задачника Python
# №1
# Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.'''
#
# # strings = ('dffvs','http://hvgfjka', 'ddkjh' , 'http://jhgfd')
# # for st in strings :
# # 	if st[:4] == 'http':
# # 		print(st)
# #
# '''№2
# Дана некоторая строка. Найдите позицию первого нуля в строке.'''
#
# # strings = 'ajhgknfo0'
# # n = strings.find('0')
# # print(n)
#
# '''№3
# Дан список. Удалите из него элементы с заданным значением.'''
#
# # list_1 = [1, 2, 3, 4, 5, 6]
# # list_1.remove(3)
# # print(list_1)
#
# '''№4
# Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.'''
#
# # for el in range(10,1000):
# # 	if el < 100 :
# # 		a = el % 10
# # 		b = (el // 10)
# # 		c = a + b
# # 		if c == 5:
# # 			print(el)
# # 	elif 100 <el >1000 :
# # 		a = el % 10
# # 		b = (el // 10)%10
# # 		c = el // 100
# # 		d = c + b
# # 		if d == 5:
# # 			print(el)
#
# # good one
# # count = 0
# # for el in range(10,1000):
# # 		a = el % 10
# # 		b = (el // 10)%10
# # 		c = el // 100
# # 		if c == 0:
# # 			if a + b == 5:
# # 				print(el)
# # 				count += 1
# # 		elif c != 0:
# # 			if c + b == 5:
# # 				print(el)
# # 				count +=1
# # print(count)
#
# '''№5
# Дана некоторая строка:
# 'abcdeabc'
# Очистите ее от дублей символов:
# 'abcde'
# '''
# # strings = 'abcdeabc'
# # tuple_1 = tuple(strings)
# # print(tuple_1)
# # for el in tuple_1 :
# #     if tuple_1.count(el) > 1:
# #         list_1 = list(tuple_1)
# # print(list(tuple_1))
# # for el1 in list_1 :
# #     if list_1.count(el1) > 1:
# #         list_1.remove(el1)
# # print(list_1)
#
#
# # goog one
#
# # list_1=[]
# # for i in strings :
# #     list_1.append(i)
# #     if list_1.count(i) > 1:
# #         list_1.remove(i)
# # print(list_1)
#
# '''
# Уровень 2.2 задачника Python
# №1
# Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
# '''
#
# # (a, b, c, d, e, f) = map (int, input('enter numbers of list_1 > ').split(' '))
# # list_1 = []
# # count = 0
# # for i in (a, b, c, d, e, f):
# #     list_1.append(i)
# #     if i < 0:
# #         count += 1
# # print(list_1)
# # print(count)
#
#
# '''№2
# Дан список с числами. Оставьте в нем только положительные числа.
# '''
# # (a, b, c, d, e, f) = map (int, input('enter numbers of list_1 > ').split(' '))
# # list_1 = []
# # for i in (a, b, c, d, e, f):
# #     list_1.append(i)
# #     if i < 0:
# #         list_1.remove(i)
# # print(list_1)
#
#
# ''' res = map(lambda x: x % 2 ==0, list_1)
#  res_1 = filter(lambda x: x % 2 ==0, list_1)
#  '''
# # Good one
#
# # res = filter((lambda x: x > 0), list_1)
# # print(res)
# # print(type(res))
# # print(list(res))
#
# '''№3
# Дана строка. Удалите предпоследний символ из этой строки.
# '''
# # strings = 'abcdeabc'
# # print(strings[:len(strings)-1])
#
# '''№5
#
# Дан список с дробями:
#
# [1.456, 2.125, 3.32, 4.1, 5.34]
# Округлите эти дроби до одного знака в дробной части.
# '''
# # list_1 = [1.456, 2.125, 3.32, 4.1, 5.34]
#
#
# # res = filter(lambda x:round(x, 1), list_1)
# # print(list(res))
#
# # Good one
# # New_list = [round(x, 1) for x in list_1]
# # print(New_list)
#
# # Good one
#
# # list_2 = []
# # for el in list_1:
# #     i = round(el, 1)
# #     #print(i)
# #     list_2.append(i)
# # print(list_2)
#
# ''' №6 Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Получите список его значений:
# [1, 2, 3, 4]
# '''
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
# #
# # print(list(dict_1.values()))
#
# '''Уровень 2.3 задачника Python
# №1
# Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.'''
#
# # string_1 = 'abcd'
# # string_2 = 'defgab'
# #
# # print( string_1[len(string_1)-1] == string_2[0])
#
# '''№2
# Дана некоторая строка. Найдите позицию третьего нуля в строке.
# '''
# # string_1 = input('Введите строку>>')
# # for el in string_1:
# #     if el == "0":
# #         print(string_1.find(el,5, len(string_1)))
# #
#
# ''' №3 Даны числа, разделенные запятыми:
#
# '12,34,56'
# Найдите сумму этих чисел.
# '''
#
# # str_1 = '12,34,56'
# # no one print(str_1.split(','), type(str_1))
# # A = str_1[:2]
# # B = str_1[3:5]
# # C = str_1[6:8]
# # list_1 = [A, B, C]
# # print(list_1)
# # summa = 0
# # for el in list_1 :
# #     summa +=int(el)
# #
# # print(summa)
#
# '''№4
# Дана дата в следующем формате:
#
# '2025-12-31'
# Преобразуйте эту дату в следующий словарь:
#
# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# '''
# # str_1 = '2025-12-31'
# # A = str_1[:4]
# # B = str_1[5:7]
# # C = str_1[8:10]
# # list_1 = [A, B, C]
# # list_2 = ['year', 'month', 'day']
# # dict_1 ={list_2[0]:A, list_2[1]:B, list_2[2]:C}
# #
# #
# # print(dict_1, type(dict_1))
#
# '''№5
#
# Дан словарь:
#
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Получите сет его значений:
#
# {1, 2, 3, 4}
# '''
#
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
# # print(set(dict_1.values()))
#
# '''Уровень 2.4 задачника Python
# №1
# Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.'''
#
# # string_1 = input('Введите строку>>')
# # list_1 = []
# # for el in string_1 :
# #     if 57 > ord(el) >47 :
# #         list_1.append(el)
# # print(string_1.find(list_1[0]))
#
# '''№2
#
# Дано число. Выведите в консоль количество четных цифр в этом числе.'''
#
# # Num_1 = input('Введите число >>')
# # res = filter(lambda x: int(x) % 2 ==0, Num_1)
# # print(list(res))
#
#
# ''''№3
# Дан словарь:
#
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Получите список его ключей:
#
# ['a', 'b', 'c', 'd']'''
#
# # dict_1 = {
# # 	'a': 1,
# # 	'b': 2,
# # 	'c': 3,
# # 	'd': 4,
# # }
# # print(list(dict_1.keys()))
#
#
# '''№4
# Дана некоторая строка:
#
# 'abcde'
# Переведите в верхний регистр все нечетные буквы этой строки. В нашем случае должно получится следующее:
#
# 'AbCdE' '''
# # str_1 = 'abcde'
# # for el in str_1 :
# #     if str_1.find(el) % 2 == 0:
# #         print(str_1.replace(el, el.upper()))
# #
# # # good one
# # print(str_1[0].upper()+str_1[1]+str_1[2].upper()+str_1[3]+str_1[4].upper())
# #
# #
# # res = filter (lambda x : str_1.find(x) % 2 == 0, str_1)
# # print(list(res))
#
#
#
# '''№5
# Дана некоторая строка со словами:
#
# 'aaa bbb ccc'
# Сделайте заглавным первый символ каждого слова в этой строке. В нашем случае должно получится следующее:
#
# 'Aaa Bbb Ccc'
# '''
#
# '''№6
# Дана дата в следующем формате:
#
# '2025-12-31'
# Преобразуйте эту дату в следующий кортеж:
#
# ('31', '12', '2025')'''
# # str_1 = '2025-12-31'
# # A = str_1.split('-')
# # print(A, type(A))
# # A.reverse()
# # print(tuple(A))
#
# '''Уровень 2.5 задачника Python
# №1
# Дана некоторая строка, например, вот такая:
#
# '023m0df0dfg0'
# Получите сет позиций всех нулей в этой в строке.'''
#
# #good one
#
# # str_1 = '023m0df0dfg0'
# # list_1 = [str_1.find('0',0,4), str_1.find('0',4,7),str_1.find('0',7,10) ,str_1.find('0',8,12)]
# # print(list_1)
#
# # no good one
# # A = list(str_1)
# # # print(str_1.find('0'))
# # # for el in str_1:
# # #     if el in str_1:
# # #         print(str_1.find(el,0,len(str_1)-1))
# # c = 0
# # print(len(A))
# # while c <= len(A):
# #     print(A.index('0'))
# #     A.remove(A[0])
# #     print(A)
# #     c +=1
# #     print(c)
# #good one
# # a = '023m0df0dfg0'
# # for el in a:
# #   if el == '0':
# #     print(a.index(el))
# #     a = a.replace('0', 'w', 1)
# #
# # A = []
# # for i in range(len(a)):
# #   if a[i] == '0':
# #     A.append(i)
# # print(A)
#
#
# '''№2
#
# Дана некоторая строка:
#
# 'abcdefg'
# Удалите из этой строки каждый третий символ. В нашем случае должно получится следующее:
#
# 'abdeg'
# '''
# # str_1 ='abcdefg'
# # str_2=''
# # for i in range(len(str_1)):
# #     if i != 2 and i != 5 :
# #         str_2 += str_1[i]
# #         #print(str_1[i])
# # print(str_2)
# #
# # print(str_1.replace(str_1[2],''))
# #good one
# # print(str_1[0:2]+str_1[3:5]+str_1[6])
#
# '''№3
#
# Дан некоторый список, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# Поделите сумму элементов, стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях.'''
#
# # list_1 = [1, 2, 3, 4, 5, 6]
# # list_2 = []
# # list_3 = []
# # print(len((list_1)))
# #
# # for i in range(len(list_1)):
# #     if i % 2 == 0:
# #         list_2.append(list_1[i])
# #         # list_1.pop(list_1[i])
# #     if i % 2 != 0:
# #         list_3.append(list_1[i])
# # print(sum(list_3)/sum(list_2))
# # print(list_2, list_3)
#
#
# #  good one
# #
# # x = list_1[1] + list_1[3] + list_1[5]
# # y = list_1[0] + list_1[2] + list_1[4]
# #
# # print(x/y)
#
# '''№4
# Дана дата в следующем формате:
#
# ['2025', '12', '31']
# Преобразуйте эту дату в следующий кортеж:
#
# ('31', '12', '2025')'''
# #
# # list_1 = ['2025', '12', '31']
# # a = list_1[::-1]
# # print(tuple(a))
# #
#
# '''Уровень 2.6 задачника Python
# №1
#
# Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.'''
# # string_1 = '2f7g60'
# # pos = []
# # print(len(string_1))
# # for i in string_1:
# #     if 57 > ord(i) >47:
# #         pos.append( string_1.index(i))
# #     else:
# #         print('нет цифр')
# # print(pos)
# #
#
#
# '''№2
#
# Дана некоторая строка:
#
# 'AbCdE'
# Смените регистр букв этой строки на противоположный. В нашем случае должно получится следующее:
#
# 'aBcDe'
# '''
# # str_1 = 'AbCdE'
# # str_2 = ''
# # for el in str_1 :
# #     if el == el.upper():
# #         str_2 += el.lower()
# #     if el == el.lower():
# #         str_2 += el.upper()
# # print(str_2)
#
# '''№3
#
# Дан некоторый список с числами, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# Слейте пары элементов вместе:
#
# [12, 34, 56] '''
#
# # list_1 = [1, 2, 3, 4, 5, 6]
# # list_2 = [str(list_1[0])+ str(list_1[1]), str(list_1[2])+ str(list_1[3]), str(list_1[4])+ str(list_1[5]) ]
# # print(list_2)
#
# '''
# №4
#
# Дана некоторая строка со словами:
#
# 'aaa bbb ccc eee fff'
# Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее:
#
# 'aaa Bbb ccc Eee fff'''
#
# # str_1 = 'aaa bbb ccc eee fff'
# # list_1 = str_1.split(' ')
# # list_2 = []
# # print(list_1)
# # # good one
# # for i in range(len(list_1)-1):
# #     if i % 2 != 0:
# #         list_1[i] = list_1[i].capitalize()
# #print(list_1)
# #print(' '.join(list_1))
#
#
# # for el in list_1:
# #     list_2.append(el.capitalize())
# # print(list_2)
# # print(' '.join(list_2))
#
#
# '''Уровень 2.7 задачника Python
# №1
#
# Дан символ. Узнайте, в каком регистре этот символ - в верхнем или нижнем.'''
#
# # c = False
# # while c == False:
# #     sign = input('Введите символ >>')
# #     if 57 < ord(sign) < 48:
# #         if sign == sign.upper():
# #             print('Символ в верхнем регистре')
# #             break
# #
# #         else:
# #             print('Символ в нижнем регистре')
# #             break
# #
# #     elif 57 > ord(sign) > 47:
# #         print('Введите буквы')
# #
# #     else:
# #         print('Введите буквы')
#
#
#
# '''№2
#
# Дано некоторое число, например, такое:
#
# 123789
# Удалите из этого числа все нечетные цифры. В нашем случае получится такой результат:
#
# 28'''
#
# # number_1 = 123789
# # number_2 = ''
# # number_1 = str(number_1)
# # for el in number_1:
# #     if int(el) % 2 != 0:
# #         number_2 += el
# #         print(el, type(el))
# # print(int(number_2))
#
#
# '''№3
#
# Дан кортеж с датой:
#
# ('2025', '12', '31')
# Преобразуйте эту дату в следующий словарь:
#
# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# }
# '''
# # tuple_1 = ('2025', '12', '31')
# #
# # dict_1 = {'year': tuple_1[0], 'month': tuple_1[1], 'day': tuple_1[2]}
# # print(dict_1)
#
#
# '''Уровень 2.8 задачника Python
# №1
#
# С помощью цикла заполните список целыми числами от 1 до 10.
#
# '''
# # c = 1
# # list_1 = []
# # while c <= 10 :
# #     list_1.append(c)
# #     c += 1
# # print(list_1)
#
#
# '''№2
#
# Дана строка с буквами. Проверьте, что в этой строке не более двух заглавных букв.
#
# '''
#
#
# # str_1 = 'GFDKdgJHY'
# # count = len(str_1)
# # while count < len(str_1):
# #     for i in range(len(str_1)-1):
# #         if str_1[i] == str_1.upper():
# #             count += 1
# #         if count == 2:
# #             print(True)
# #             break
# #
#
#
#
#
# # str_1 = 'GGFDKdgJHY'
# # for el in str_1:
# #     if el.upper() :
# #         if el.count(el) > 2:
# #             print(True)
# #         else:
# #             print(False)
#
#
# '''№3
#
# Дан список со строками, содержащими целые числа:
#
# ['1', '2', '3', '4', '5']
# Преобразуйте элементы этого списка в числа:
#
# [1, 2, 3, 4, 5]
# '''
# # list_1 = ['1', '2', '3', '4', '5']
# # res = filter(lambda x: int(x)*3, list_1)
# # res_1 = map(lambda x: int(x), list_1)
# # print(list(res))
# # print(list(res_1))
# #
# # # good one
# # print([int(x) for x in list_1])
#
# '''Уровень 2.9 задачника Python
# №1
#
# С помощью цикла заполните список четными числами из промежутка от 1 до 100.
#
# '''
#
# # c = 1
# # list_1 = []
# # while c < 101:
# #     c += 1
# #     if c % 2 ==0:
# #         list_1.append(c)
# # print(list_1)
#
#
# # print([x for x in range(1,101) if x % 2 != 0])
#
# '''№2
#
# Дан список с числами:
#
# [1, 2, 3, 4, 5]
# Выведите в консоль элементы этого списка в обратном порядке.'''
#
# # print([1, 2, 3, 4, 5][::-1])
#
# '''№3
#
# Даны две строки:
#
# txt1 = 'abcde'
# txt2 = '12345'
# Сделайте из этих строк словарь так, чтобы символы первой строки стали ключами, а символы второй строки - значениями:
#
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# 	'e': 5,
# }
# '''
# # txt1 = 'abcde'
# #
# # txt2 = '12345'
# # dict_1 = {
# #     txt1[0]:txt2[0],
# #     txt1[1]:txt2[1],
# #     txt1[2]:txt2[2],
# #     txt1[3]:txt2[3],
# #     txt1[4]:txt2[4]
# #
# # }
# #
# # print(dict_1)
#
#
# '''Уровень 2.10 задачника Python
# №1
#
# Дана строка с буквами и цифрами. Проверьте, что в этой строке не более трех букв.'''
#
# # str_1 = input('Введите строку >>')
# # c = 0
# # list_1 =[]
# # for el in str_1:
# #     if 123 > ord(el) > 96:
# #         list_1.append(el)
# # print(list_1)
# # if len(list_1) <= 3:
# #     c = 1
# # if c == 1:
# #     print(True)
# # else:
# #     print(False)
#
#
#
# '''№2
#
# Дано число. Получите первую четную цифру с конца этого числа.'''
#
# # num_1 = int(input('Введите число >>'))
# # str_1 = ''
# # for el in str(num_1):
# #     if int(el) % 2 == 0:
# #         str_1 += el
# # print(str_1[0])
#
#
#
# '''№3
#
# Дана некоторая строка:
#
# 'abcde abcde abcde'
# Замените в ней первый символ каждого слова на '!':
#
# '!bcde !bcde !bcde'''
# #
# # string_1 = 'abcde abcde abcde'
# # string_1 = string_1.split()
# # print(string_1)
# # list_1 = []
# # string_2 = ''
#
# # for i in range(len(string_1)):
# #     list_1.append(string_1[i].replace(string_1[i][0],'!'))
# #
# # print(str(list_1))
#
# # # #
# # for i in range(len(string_1)):
# #     string_2 +=' ' + string_1[i].replace(string_1[i][0],'!')
# #
# # print(string_2.strip())
#
#
# # for el in string_1:
# #     string_2 += ' '+ el.replace(el[0],'!')
# #     print(el.replace(el[0],'!'))
# #
# # print(string_2.strip())
#
#
# '''№4
#
# Дан список со строками, содержащими целые числа:
#
# ['1', '2', '3', '4', '5']
# Найдите сумму элементов этого списка.'''
#
# # list_1 = ['1', '2', '3', '4', '5']
# # list_2 = []
# # for el in list_1:
# #     x = int(el)
# #     list_2 .append(x)
# # print(sum(list_2))
#
# #
# # list_1 = ['1', '2', '3', '4', '5']
# # list_2= []
# # for el in list_1:
# #      list_2 .append(int(el))
# # print(sum(list_2))
#
# '''Уровень 3.1 задачника Python
# №1
#
# С помощью включения создайте следующий список:
#
# [1, 2, 3, 4, 5, 6] '''
#
#
#
# '''№2
#
# Даны два списка:
#
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# Объедините эти списки в один:
#
# [1, 2, 3, 4, 5, 6]'''
#
# # lst1 = [1, 2, 3]
# # lst2 = [4, 5, 6]
#
# # print(lst1 + lst2)
# #
# # for el in lst2:
# #     lst1.append(el)
# # print(lst1)
#
# ''''№3
#
# Дан некоторый список, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# Найдите сумму первой половины элементов этого списка.'''
#
# # lst1 = [1, 2, 3, 4, 5, 6]
# # lst2 = lst1[:3]
# # print(sum(lst2))
#
#
# '''Уровень 3.2 задачника Python
# №1
#
# С помощью включения создайте следующий список:
#
# [1, 3, 5, 7, 9]'''
#
# ''''№2
#
# Даны два кортежа:
#
# tpl1 = (1, 2, 3)
# tpl2 = (4, 5, 6)
# Объедините эти кортежи в один:
#
# (1, 2, 3, 4, 5, 6) '''
#
# # tpl1 = (1, 2, 3)
# # tpl2 = (4, 5, 6)
# # list_1 = list(tpl1)
# #
# # print(tpl1 + tpl2)
# #
# # for el in tpl2:
# #     list_1.append(el)
# # print(tuple(list_1))
#
#
#
# '''№3
#
# Даны два словаря:
#
# dct1 = {
# 	'a': 1,
# 	'b': 2,
# }
# dct2 = {
# 	'c': 3,
# 	'd': 4,
# }
# Объедините эти словари в один:
#
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# } '''
# #
# # dct1 = {
# # 	'a': 1,
# # 	'b': 2,
# # }
# # dct2 = {
# # 	'c': 3,
# # 	'd': 4,
# # }
# # #
# # # for x, y in dct2.items():
# # #     dct1[x] = y
# # # print(dct1)
# #
# # dct1.update(dct2)
# # print(dct1)
#
#
# '''№4
#
# Дан некоторый список, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# Поделите сумму первой половины элементов этого списка на сумму второй половины элементов.'''
#
# # list_1 = [1, 2, 3, 4, 5, 6]
# # print(sum(list_1[:3])/ sum(list_1[3:]))
#
#
#
# '''Уровень 3.3 задачника Python
# №1
#
# Дано некоторое число:
#
# 1357
# Проверьте, что все цифры этого числа являются нечетными.'''
#
# # good one
#
# # num_1 = 1657
# # num_1 = str(num_1)
# # num_2 = ''
# #
# # for el in num_1:
# #     if el % 2 != 0:
# #         num_2 += el
# #
# # if len(str(num_1)) == len(num_2):
# #     print('Все цифры являются нечетными')
# # else:
# #     print('Не все цифры являются нечетными')
#
#
# # c = 0
# # while c <= len(str(num_1))-1:
# #     x = num_1 % 10
# #     num_1 // 10
# #     c +=1
# #     if x % 2 != 0:
# #         print(True)
# #     else:
# #         print(False)
#
#
# '''№2
#
# Дано некоторое слово:
#
# 'abcba'
# Проверьте, что это слово читается одинаково с любой стороны.'''
#
# # str_1 = 'level'
# # if str_1 == str_1[::-1]:
# #     print(True)
# # else:
# #     print(False)
#
#
#
# '''№3
#
# Даны два сета:
#
# st1 = {1, 2, 3}
# st2 = {4, 5, 6}
# Объедините эти сеты в один:
#
# {1, 2, 3, 4, 5, 6}'''
# #
# # st1 = {1, 2, 3}
# # st2 = {4, 5, 6}
# # list_1 = list(st1)
# #
# # st1.update(st2)
# # print(st1)
# #
# # for el in st2:
# #     list_1.append(el)
# # print(set(list_1))
#
#
#
# ''' Уровень 3.4 задачника Python
# №1
#
# Дана строка. Удалите из нее все гласные буквы.'''
#
# # str_1 = input('Введите строку >>')
# # # list_1 = ['a', 'e', 'i', 'o', 'u', 'y']
# # list_2 = list(str_1)
# # print(list_2)
# # for el in list_2:
# #     #if el in list_1:
# #     if el =='a' or el == 'e' or el == 'i' or el == 'i' or el == 'o' or el == ' u' or el =='y':
# #         print(el)
# #         list_2.remove(el)
# #
# # print(''.join(list_2))
#
#
# # for el in str_1:
# #     if el in list_1:
# #         str_2 = str_1.replace(el, '')
# #         print(str_2)
#
#
# '''№2
#
# Даны два сета:
#
# st1 = {1, 2, 3, 4, 5}
# st2 = {4, 5, 6, 7, 8}
# Получите сет их общих элементов:
#
# {4, 5}'''
#
# # st1 = {1, 2, 3, 4, 5}
# # st2 = {4, 5, 6, 7, 8}
# # A = set([x for x in st1 if x in st2])
# # print(A)
#
# '''№3
#
# Даны два сета:
#
# st1 = {1, 2, 3, 4, 5}
# st2 = {4, 5, 6, 7, 8}
# Получите сет элементов, входящих только в один из сетов:
#
# {1, 2, 3, 6, 7, 8}'''
#
#
#
#
#
# '''
#
# Уровень 3.5 задачника Python
# №1
#
# Дан текст со словами. Запишите в список все слова, начинающиеся на букву 'a'.'''
#
# # string_1 = 'африка америка европа азия сибирь асумани'
# # string_1 = string_1.split()
#
# # list_1 = []
# # for el in string_1:
# #     if el[0] == 'а' :
# #         list_1.append(el)
# # print(list_1)
#
#
# # #good one
#
# # res = filter(lambda x: x[0] == 'а', string_1)
# # print(list(res))
#
#
# '''№2
#
# Дан список со числами. Проверьте, что все элементы этого списка являются положительными числами.'''
#
# # list_1 = [1, 0, 5, 7, 9]
# # c = 0
# # for i in range(len(list_1)):
# #     if list_1[i] < 0:
# #         c = 1
# # if c == 1:
# #     print('Все элементы списка не положительные')
# # else:
# #     print('Все элементы списка  положительные')
#
#
# '''№3
#
# Даны два списка:
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [4, 5, 6, 7, 8]
# Получите список их общих элементов:
#
# [4, 5]'''
#
# #good one
#
# # list_1 = [1, 2, 3, 4, 5]
# # list_2 = [4, 5, 6, 7, 8]
# # print([x for x in list_1 if x in list_2])
#
#
#
# # list_3 = list_1 + list_2
# # list_4 = []
# # for el in list_3:
# #     if el in list_1 and el in list_2:
# #         list_4.append(el)
# # print(list(set(list_4)))
#
#
# '''№4
#
# Дана некоторая переменная с числом:
#
# num = 5;
# Сделайте строку, содержащую столько нулей, сколько указано в переменной. В нашем случае получится такая строка:
#
# '00000'
# '''
# # num = 5
# #
# # print('0'*num)
#
#
# '''
# Уровень 3.6 задачника Python
# №1
#
# Дан список со числами. Удалите из него числа, состоящие более чем из трех цифр.'''
#
# # list_1 = [23, 5456, 9, 557, 9075, 54]
# # res = filter(lambda x: len(str(x)) <= 3, list_1)
# # print(list(res))
#
#
# '''№2
#
# Дана строка. Проверьте, что эта строка состоит только из цифр.'''
#
# # string_1 = '75476392'
#
# # list_1 = []
# # for el in string_1:
# #     if 58 > ord(el) > 47:
# #         list_1.append(el)
# # if len(list_1) == len(string_1):
# #     print(True)
# # else:
# #     print(False)
#
# #good one
#
# # res = filter(lambda x: 58 > ord(x) > 47, list(string_1))
# # A = list(res)
# # print(len(string_1) == len(A))
#
#
# '''№3
#
# Дано число, например, вот такое:
#
# num = 12345;
# Проверьте, что все цифры этого числа больше нуля.'''
#
# # num = 12345
# # str_1, c, y = (str(num), 0, 0)
# # while c <= len(str_1)-1:
# #     x = num % 10
# #     num //= 10
# #     c += 1
# #     if x == 0:
# #         y = 1
# #
# # if y == 1:
# #     print('В числе есть цифра 0')
# # else:
# #     print('Все цифры этого числа больше нуля')
#
#
# '''№4
#
# Даны два списка:
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [1, 2, 3]
# Проверьте, что все элементы первого списка есть во втором'''
#
# # lst1 = [1, 2, 3]
# # lst2 = [1, 2, 3]
#
# # lst3 = []
# # q = 0
# # for el in lst1:
# #     if el in lst2:
# #         q = 0
# #     else:
# #         lst3.append(el)
# #         q = 1
# # if q == 1:
# #     print(lst3, 'not in lst2')
# # else:
# #     print('все элементы первого списка есть во втором')
#
# # good one
#
# # A = [x for x in lst1 if x in lst2]
# # print(A == lst1)
#
# '''Уровень 3.7 задачника Python
# №1
#
# Дана строка. Сделайте заглавной последнюю букву каждого слова в этой строке.'''
#
# # string_1 = 'Как ваши дела, мадемуазель пимбо'
# # string_1 = string_1.split()
# # list_1 = []
# # for el in string_1:
# #     x = el[:len(el) - 1] + el[len(el) - 1].capitalize()
# #     if el[len(el) - 1] == ',' or el[len(el) - 1] == '.' or el[len(el) - 1] == '-':
# #         x = el[:len(el) - 2] + el[len(el) - 2].capitalize()
# #     list_1.append(x)
# #
# # print(' '.join(list_1))
#
#
# '''№2
#
# Дана строка. Проверьте, что эта строка состоит только из четных цифр.'''
#
# # str_1 = '1294678'
# # res = filter(lambda x: int(x) % 2 == 0, str_1)
# # A = (''.join(list(res)))
# # print(len(A) == len(str_1))
# # print(A, type(A), len(A), len(str_1))
#
# #good one
#
# # str_1 = '2468'
# # y = [x for x in str_1 if int(x) % 2 == 0]
# # print(''.join(y) == str_1)
#
#
# '''№3
#
# Даны две строки:
#
# txt1 = '12345'
# txt2 = '45678'
# Получите символы, которые есть и в одной, и в другой строке:
#
# '45' '''
# # txt1 = '12345'
# # txt2 = '45678'
# # print(','.join([x for x in txt1 if x in txt2]))
#
#
#
# '''№4
#
# Дана некоторая строка:
#
# 'a bc def ghij'
# Переведите в верхний регистр все подстроки, в которых количество букв меньше или равно трем. В нашем случае должно получится следующее:
#
# 'A BC DEF ghij'
# '''
# # str_1 = 'a bc def ghij hj jhgytr h'
# # str_1 = str_1.split()
# # str_2 =''
# #
# # for el in str_1:
# #     if len(el) <= 3:
# #         el = el.upper()
# #         str_2 += ' ' + el
# #     if len(el) > 3:
# #         str_2 += ' '+ el
# # print(str_2)
#
#
# '''Уровень 3.8 задачника Python
# №1
#
# Дан список со числами. Проверьте, что все числа из этого списка содержат в себе цифру 3.'''
#
# # list_1 = [132, 436, 637, 352, 366]
# #
# # res = filter(lambda x: '3' in str(x), list_1)
# # print(len(list(res)) == len(list_1))
# #
# # # good one
# #
# # Y = [x for x in list_1 if '3' in str(x)]
# # print(len(Y) == len(list_1))
#
#
# '''№2
#
# Через запятую написаны числа. Получите максимальное из этих чисел.'''
#
# # num_1 = input('Введите число через запятую >>')
# # num_1 = num_1.split(',')
# # A = [int(x) for x in num_1]
# # print(max(A))
#
#
# '''№3
#
# Дана строка в формате:
#
# 'kebab-case'
# Преобразуйте ее в формат:
#
# 'snake_case'''
#
# # str_1 = 'mother-fucker'
# # str_1 = str_1.split('-')
# # str_2 = str_1[0].lower() + '_' + str_1[1].lower()
# # str_3 = str_1[0].lower() + str_1[1].capitalize()
# # print('-'.join(str_1))
# # print(str_2)
# # print(str_3)
# #
#
#
# '''№4
#
# Дана строка в формате:
#
# 'snake_case'
# Преобразуйте ее в формат:
#
# 'camelCase'''
#
#
#
#
# '''№5
#
# Дана строка в формате:
#
# 'camelCase'
# Преобразуйте ее в формат:
#
# 'snake_case' '''
# # str_1 = 'motherFucker'
# # for el in str_1:
# #     if el == el.capitalize():
# #         print(el)
# #         str_1 = str_1.replace(el, '_'+el.lower())
# # print(str_1)
#
#
#
# '''Уровень 3.9 задачника Python
# №1
#
# Дан список с числами. Удалите из него числа, имеющие два и более нуля.'''
#
# # list_1 = [1010, 30, 340540, 48, 765, 700]
# # for el in list_1:
# #     if str(el).count('0') >= 2:
# #         print(el)
# #         list_1.remove(el)
# # print(list_1)
#
#
# '''№2
#
# Найдите все числа от 1 до 1000, сумма цифр которых равна 13. Результат запишите в сет.'''
#
# '''№3
#
# Дан список:
#
# [1, 2, 3]
# Сделайте так, чтобы в нем каждый элемент повторился два раза:
#
# [1, 1, 2, 2, 3, 3] '''
#
# '''№4
#
# Даны два списка:
#
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# Переберите эти списки одним циклом и в каждой итерации выводите их элементы следующим образом:
#
# '1,4'
# '2,5'
# '3,6'
#  '''
#
#
#
#
#
#
# '''Уровень 3.10 задачника Python
# №1
#
# Дан список и число. Оставьте в списке только те числа, которые являются делителями заданного числа.'''
#
# # list_1 = [3, 6, 7, 9, 10, 34, 6, 57]
# # num = 36
# # res = filter(lambda x: num % x == 0, list_1)
# # print(set(res))
#
#
#
# '''№2
#
# Дан список с числами. После каждого однозначного числа вставьте еще такое же.'''
#
# # list_1 = [3, 69, 7, 87, 10, 34, 65, 57]
# #
# # for i in range(len(list_1)-1):
# #     if list_1[i] < 10:
# #         list_1[i] += list_1[i]*10
# #
# # print(list_1, type(list_1))
#
#
# '''№3
#
# Даны два числа. Получите список цифр, которые есть и в одном, и во втором числе.'''
#
# # num_1 = 5678
# # num_2 = 895
# #
# # str_1 = str(num_1)
# # str_2 = str(num_2)
# # list_1 = [x for x in str_1 if x not in str_2]
# # print(list_1)
#
# '''№4
#
# Дано число. Получите список позицией всех цифр 3 в этом числе, за исключением первой и последней.'''
#
# '''№5
#
# Дан список со числами. Оставьте в нем числа, состоящие из разных цифр, а остальные удалите.'''
#
# # list_1 = [34, 77, 98, 43, 11, 45, 54, 111, 555]
# # list_2 = []
# # print(list_2)
#
#
# '''№6
#
# Даны два списка:
#
# lst1 = [1, 2, 3];
# lst2 = [1, 2, 3, 4, 5];
# Удалите из большего списка лишние элементы с конца так, чтобы длины списков стали одинаковыми.'''
#
# # lst1 = [1, 2, 8, 6, 3]
# # lst2 = [1, 6, 89, 90]
# # if len(lst1) < len(lst2):
# #     lst3 = lst2[:len(lst1)]
# # else:
# #     lst3 = lst1[:len(lst2)]
# #
# # print(lst3)
#
#
# '''№7
#
# Дан список с некоторыми числами, например, вот такой:
#
# [123, 456, 789]
# Напишите код, который перевернет числа в этом списке по следующему принципу:
#
# [321, 654, 987]'''
#
# # list1 = [123, 456, 789, 123, 678]
# # list2 = [str(x)[::-1] for x in list1]
# # print(list2)
#
#
# '''Уровень 4.1 задачника Python
# №1
#
# Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию.'''
#
#
#
#
# '''№2
#
# Дан список:
#
# [1, '', 2, 3, '', 5]
# Удалите из списка все пустые строки.'''
#
# # list_1 = [1, '', 2, 3, '', 5]
# # list_2 = [x for x in list_1 if x != '']
# # print(list_2)
#
# # print(list(x for x in list_1 if x != ''))
#
# '''№3
#
# Дан список:
#
# [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9],
# ]
# Выведите в консоль все элементы этого списка.'''
#
# # list_1 = [
# # 	[1, 2, 3],
# # 	[4, 5, 6],
# # 	[7, 8, 9],
# # ]
# # for el in list_1:
# #     print(el)
#
#
# '''Уровень 4.2 задачника Python
# №1
#
# Дано число. Получите список делителей этого числа.'''
# # num = 15
# # for i in range(1, num+1):
# #     if num % i == 0:
# #         print( i)
#
#
#
# '''№2
#
# Выведите в консоль все числа в промежутке от 10 до 1000, у которых первая цифра четная.'''
#
# # A = [str(x) for x in range(10, 1001)]
# # for el in A:
# #     if int(el[0]) % 2 == 0:
# #         print(el)
#
#
# '''№3
#
# Дан список:
#
# [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9],
# ]
#
# Найдите сумму элементов этого списка.'''
#
# # list_1 = [
# # 	[1, 2, 3],
# # 	[4, 5, 6],
# # 	[7, 8, 9],
# # ]
#
# # list_2 = []
# # for el in list_1:
# #     a = sum(el)
# #     list_2.append(a)
# #
# # print(sum(list_2))
#
# # res = [sum(x) for x in list_1]
# # print(sum(res))
#
# '''№4
#
# Дан следующий словарь:
#
# dct = {
# 	1: {
# 		1: 11,
# 		2: 12,
# 		3: 13,
# 	},
# 	2: {
# 		1: 21,
# 		2: 22,
# 		3: 23,
# 	},
# 	3: {
# 		1: 24,
# 		2: 25,
# 		3: 26,
# 	},
# }
# Найдите сумму элементов этого словаря.'''
#
# # dct = {
# # 	1: {
# # 		1: 11,
# # 		2: 12,
# # 		3: 13,
# # 	},
# # 	2: {
# # 		1: 21,
# # 		2: 22,
# # 		3: 23,
# # 	},
# # 	3: {
# # 		1: 24,
# # 		2: 25,
# # 		3: 26,
# # 	},
# # }
# # print(sum(dct.keys()))
# # A = dct.values()
# # A = list(A)
# #
# # print(A, type(A))
# # print(sum(A[0].keys()))
# # print(sum(A[0].values()))
# # print(sum(A[1].keys()))
# # print(sum(A[1].values()))
# # print(sum(A[2].keys()))
# # print(sum(A[2].values()))
# # Y = [(sum(dct.keys()), sum(A[0].keys()), sum(A[0].values()), sum(A[1].keys()), sum(A[1].values()), sum(A[2].keys()), sum(A[2].values()))]
# # print(Y)
#
#
# '''Уровень 4.3 задачника Python
# №1
#
# Дан список. Удалите из него каждый пятый элемент.'''
#
# # list_1 = [2, 4, 6, 7, 0, 5]
# #
# # if len(list_1) < 4:
# #     print('Out of range')
# # else:
# #     list_1.remove(list_1[4])
# #     print(list_1)
#
#
#
#
# '''№2
#
# Даны два числа. Получите список общих делителей этих чисел.'''
#
# # num_1 = 96
# # num_2 = 72
# # max_1 = num_1
# # if num_2 > max_1:
# #     num_2 = max_1
# #
# # a = [x for x in range(1, max_1+1) if num_1 % x == 0 and num_2 % x == 0]
# # print(a)
#
#
# '''№3
#
# Даны два числа:
#
# txt1 = 12345
# txt2 = 45678
# Получите кортеж цифр, которые есть и в одном, и в другом числе:
#
# (4, 5) '''
#
# # txt1 = 12345
# # txt2 = 45678
# #
# # A = [int(x) for x in str(txt1) if x in str(txt2)]
# # print(tuple(A))
#
# '''№4
#
# Дан список:
#
# [
# 	[
# 		[11, 12, 13],
# 		[14, 15, 16],
# 		[17, 17, 19],
# 	],
# 	[
# 		[21, 22, 23],
# 		[24, 25, 26],
# 		[27, 27, 29],
# 	],
# 	[
# 		[31, 32, 33],
# 		[34, 35, 36],
# 		[37, 37, 39],
# 	],
# ]
# Найдите сумму элементов этого списка.'''
#
#
#
# '''Уровень 4.4 задачника Python
# №1
#
# Дан список с числами. Оставьте в нем только те числа, которые делятся на 5.'''
#
# # list_1 = [12, 55, 65, 23, 98, 45]
# # print([x for x in list_1 if x % 5 == 0])
#
#
#
# '''№2
#
# Дано число. Проверьте, что у этого числа есть только один делитель, кроме него самого и единицы.'''
#
# # num_1 = 41
# # list1 = []
# # for i in range(2, num_1):
# #     if num_1 % i == 0 or num_1 % i == num_1:
# #         list1.append(i)
# # if len(list1) == 1:
# #     print('У числа есть только один делитель, кроме него самого и единицы.')
# # elif len(list1) == 0:
# #     print('У числа есть только 2 делители, самого себя и единицы.')
# # else:
# #     print('У числа есть много делителей')
#
#
# '''№3
#
# Дан следующий словарь:
#
# dct = {
# 	1: {
# 		1: 11,
# 		2: 12,
# 		3: 13,
# 	},
# 	2: {
# 		1: 21,
# 		2: 22,
# 		3: 23,
# 	},
# 	3: {
# 		1: 24,
# 		2: 25,
# 		3: 26,
# 	},
# }
# Найдите сумму элементов этого словаря.'''
#
#
#
# '''Уровень 4.5 задачника Python
# №1
#
# Выведите в консоль все числа в промежутке от 10 до 1000, у которых предпоследняя цифра четная.'''
#
# # print([x for x in range(10, 1000) if str(x)[-2] in ['0', '2', '4', '6', '8']])
#
#
#
# '''№2
#
# Дана строка:
#
#
# 	text1
# 	text2
# 	text3
# 	text4
# 	text5
#
# Разбейте эту строку в список так, чтобы каждая непустая линия текста стала отдельным элементом списка:
#
# [
# 	'text1',
# 	'text2',
# 	'text3',
# 	'text4',
# 	'text5',
# ]'''
#
#
#
#
#
# '''№3
#
# Дан следующий словарь:
#
# dct = {
# 	1: {
# 		1: {
# 			1: 111,
# 			2: 112,
# 			3: 113,
# 		},
# 		2: {
# 			1: 121,
# 			2: 122,
# 			3: 123,
# 		},
# 	},
# 	2: {
# 		1: {
# 			1: 211,
# 			2: 212,
# 			3: 213,
# 		},
# 		2: {
# 			1: 221,
# 			2: 222,
# 			3: 223,
# 		},
# 	},
# 	3: {
# 		1: {
# 			1: 311,
# 			2: 312,
# 			3: 313,
# 		},
# 		2: {
# 			1: 321,
# 			2: 322,
# 			3: 323,
# 		},
# 	},
# }
# Найдите сумму элементов этого словаря.
# '''
#
# '''Уровень 5.3 задачника Python
# №1
#
# Попросите пользователя ввести два числа целых числа через консоль. Заполните список целыми числами от минимального введенного числа до максимального.'''
#
# # x, y = map(int, input('Введите через пробель 2 числа >>').split())
# # # print([x for x in range(x, y+1)])
# # if x < y:
# #     print([x for x in range(x, y + 1)])
# # if x > y:
# #     print([x for x in range(x, y - 1, -1)])
#
#
#
# '''№2
#
# Попросите пользователя ввести дату в формате год-месяц-день. Определите день недели, соответствующий этой дате.
#
# №3
#
# Попросите пользователя ввести год. Определите, високосный этот год или нет.
#
# №4
#
# Напишите программу, которая сформирует следующую строку:
#
# '54321'
# №5
#
# Дан некоторый список, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# Поменяйте местами пары элементов этого списка:
#
# [2, 1, 4, 3, 6, 5]
# '''
#
#
# '''№1 Патрик
# Дан список:
# [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9],
# ]
# Слейте элементы этого списка в один одномерный список:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]'''
#
# # L = [
# #      [1, 2, 3],
# #      [4, 5, 6],
# #      [7, 8, 9],
# # ]
# # L_1 = []
# # for i in range (len(L)):
# #   for j in range(len(L[i])):
# #     L_1.append(L[i][j])
# # print(L_1)
#
# #good one too
#
# # L = [
# #      [1, 2, 3],
# #      [4, 5, 6],
# #      [7, 8, 9],
# # ]
# # L_1 = []
# # for i in range (len(L)):
# #   L_1 += L[i]
# # print(L_1)
#
# #code mu
# #5.6 №3
# '''Дан
# некоторый
# список, например, вот
# такой:
#
# [123, 456, 789]
# Слейте
# все
# элементы
# этого
# списка
# в
# один
# список, разбив
# их
# посимвольно:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# '''
#
# # A = [123, 456, 78789]
# # A_1 = []
# # for i in range(len(A)):
# #   for j in range(len(str(A[i]))):
# #     A_1.append(str(A[i])[j])
# #
# # print(A_1)
#
# #5.2
#
# ''' Патрик 5.2
# Дан некоторый список, например, вот такой:
#
# [1, 2, 3, 4, 5, 6]
# По очереди выведите в консоль подсписки из двух элементов нашего списка:
#
# [1, 2]
# [3, 4]
# [5, 6]'''
#
# # M = [1, 2, 3, 4, 5, 6]
# #
# # for i in range(0, len(M)-1, 2):
# #   print(M[i] , M[i+1])
#

'''Уровень 6.1 задачника Python
№1

Сделайте функцию, которая вернет текущий день недели словом.

№2

Сделайте функцию, которая параметром будет получать дату, а возвращать день недели словом, соответствующий этой дате.'''
import math
# from datetime import datetime
# def Data_fc(y):
#     y = datetime(int(y[0]), int(y[1]), int(y[2]))
#     print(y)
#     return y.strftime('%A')
#
# data_1 = input().split(',')
# print(Data_fc(data_1))

'''№3

Сделайте функцию, которая параметром будет принимать секунды, а возвращать количество суток, соответствующих этим секундам.'''

# import math
# def Count_day(s):
#     x = (s/3600)/24
#     return math.floor(x)
#
# s = int(input('Введите кол-во секундов >>'))
# print('Количество суток = ', Count_day(s))


'''№4

Сделайте функцию, которая параметром будет принимать число и строку и обрезать эту строку до длины, заданной первым параметром.'''

# def cut_string(str_2):
#     str_2 = str_2
#     x = int(input('Введите длину для отрезки >>'))
#     if len(str_2) < x:
#         print('операция не выполняется')
#     else:
#         str_1 = str_2[:x]
#         return str_1
#
# str_2 = input('Введите строку тут >> ')
# print(cut_string(str_2))



'''№5

Сделайте функцию, которая параметром будет получать дату, а возвращать знак зодиака, соответствующий этой дате.'''




'''№6

Сделайте функцию, которая параметром будет принимать число, а возвращать сумму его делителей.'''

# num = int(input('Введите число >> '))
# summa = 0
# res = [x for x in range(1,num+1) if num % x == 0]
# print(res)
# for el in res:
#     summa += el
# print(summa)
# print(sum(res))


'''Уровень 6.2 задачника Python
№1

Сделайте функцию, которая параметром будет принимать число и удалять из него нули.'''

# num = 124
# num = str(num)
# print(num, type(num))
# print(num.split(','), type(num))
# print(list(num))

#
# def udalit_o(num):
#     num = list(num)
#     for el in num:
#         if el == '0':
#             num.remove(el)
#     return ''.join(num)
# num =input('Введите число >> ')
# print(udalit_o(num))


# def udalit_o(num):
#     res = [el for el in num if el != '0']
#     return int(''.join(res))
#
# num = input('Введите число >> ')
# print(udalit_o(num), type(udalit_o(num)))


'''№2

Сделайте функцию, которая будет возвращать сколько дней прошло или осталось до заданной даты в году, в зависимости
 от того, была уже эта дата или нет.'''

# from datetime import datetime
#
# def how_much_d(date):
#     x = datetime(int(date[0]), int(date[1]), int(date[2]))
#     return (f'Прошло {x.strftime('%j')} дней (дня) в {x.strftime('%Y')} году')
#
# date_1 = input('Введите дату через запятую >>').split(',')
# print(how_much_d(date_1))




'''№3

Сделайте функцию, которая вернет список всех високосных годов за предыдущие сто лет.'''
# def four_year(years):
#     res = [x for x in range(int(years[0]), int(years[1])) if x % 4 == 0 or x % 400 == 0]
#     res_1 = []
#     for el in res:
#         res_1.append(el)
#     return res_1
# years = input('Введите интервал времени из ста лет через запятую >>').split(',')
# print(four_year(years))


''' №4 Сделайте функцию, которая параметром будет год и проверять, високосный он или нет.'''

'''№5

Сделайте функцию, которая будет возвращать сколько дней осталось до конца0 текущего месяца.

№6

Сделайте функцию, которая вернет предыдущий, текущий и следующий дни недели словом в виде следующего словаря:

{
	'next': 'пн',
	'curr': 'вс',
	'prev': 'сб',
}'''

# Уровень 7.1 задачника Python



'''№1

Дан текстовый файл. Получите количество символов в нем.'''

# with open('tst_1.txt', 'w') as file:
#     a = file.write('Hello friends \n')

# with open('tst_1.txt', 'r') as file:
#     a = file.read()
#     b = len(a.strip())
#     print(a)
#     print(b)

'''№2

Попросите пользователя ввести текст через консоль. Запишите введенный текст в какой-нибудь файл.'''

str_1 = input('Введите строку >>')
with open('tst_1.txt', 'a') as file:
    a = file.write(str_1 + '\n')



'''№3

Дан текстовый файл со словами. Напишите программу, которая обернет каждое слово в круглые скобки. 
Результат запишите в новый файл.'''




'''№4

Дан текстовый файл со словами и с дробями вида 1/2. Напишите программу, которая обернет каждую дробь в круглые скобки.
 Результат запишите в новый файл.

№5

Напишите программу, которая сформирует следующий список:

[
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
] '''

# '''№1

# Дан текстовый файл. Получите количество символов в нем.
# '''

# f = open('tdt.txt', 'r').readlines()
# summa = 0
# print(f)
# for el in f:
#   summa += len(el)-1

# print(summa+1)

'''
Дан текстовый файл. Получите количество чисел в нем.
'''
# f = open('tdt.txt', 'r')

# L = []
# for i in range(5):
#   L.append(f.readline().split())
# print(L)
# summa = 0
# for el in L:
#   summa += len(el)
# print(summa)

# print(L)

# f = f.read()
# #f = f.replace('\n', '')
# f = f.split('\n')
# print(f, type(f)) #123 2311 2134 1 12\n3214 1332 1\n1234

'''№2
Попросите пользователя ввести текст через консоль. Запишите введенный текст в какой-нибудь файл.
'''

# str_1 = input('Введите строку >>')
# with open('tst_1.txt', 'a') as file:
#     a = file.write(str_1 + '\n')


'''№3
Дан текстовый файл со словами. Напишите программу, которая обернет каждое слово в круглые скобки. Результат запишите в новый файл.
'''

# f = open('tdt.txt', 'r')

# s = f.readline().split()
# L = ['('+x+')' for x in s]
# s = ' '.join(L)
# w = open('xvc.txt', 'w')
# w.write(s + '\n')
# w.close()
# f.close()

'''№4

Дан текстовый файл со словами и с дробями вида 1/2. Напишите программу, которая обернет каждую дробь в круглые скобки. Результат запишите в новый файл.'''

# f = open('tdt.txt', 'r')

# s = f.readline().split()
# L = []
# for el in s:
#   if el[0].isdigit():
#     L.append('('+el+')')
#   else:
#     L.append(el)
# s = ' '.join(L)
# w = open('123.txt', 'w')
# w.write(s + '\n')
# w.close()
# f.close()