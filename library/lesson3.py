import math

# 1

a, b, c = 10, 5, 2
print(f"Сумма: {a + b + c}")
print(f"Разность: {a - b - c}")
print(f"Произведение: {a * b * c}")
print(f"a - b + c: {a - b + c}")
print(f"(a * b) / c: {(a * b) / c}")
print(f"(a + b) % c: {(a + b) % c}")

cat_a, cat_b = 3, 4

# 2

# Площадь треугольника
area = 0.5 * cat_a * cat_b
print(f"Площадь треугольника: {area}")

# Гипотенуза
hypotenuse = math.sqrt(cat_a**2 + cat_b**2)
print(f"Гипотенуза: {hypotenuse}")

# 3
lst = ['Hello world', 'a b c', 'hi how are you doing?']
for w in lst:
	print('В строке ' + str(len(w.split(' '))) + ' words')

# 4
string = 'hhhabchghhh'
first_h = string.index('h')
last_h = string.rindex('h')
print(string[:first_h+1] + string[first_h+1:last_h].replace('h', 'H') + string[last_h:])


# 5. Дана строка.
# ● Сначала выведите третий символ этой строки.
# ● Во второй строке выведите предпоследний символ строки.
# ● В третьей строке выведите первые пять символов строки.
# ● В четвертой выведите всю до последних двух символов.
# ● В пятой строке выведите все символы с четными индексами
# ● В шестой строке выведите все символы с нечетными
# индексами, то есть начиная со второго символа строки.
# ● В седьмой строке выведите все символы в обратном порядке.
# ● В восьмой строке выведите все символы строки через один в
# обратном порядке, начиная с последнего.
# ● В девятой строке выведите длину данной строки.


string_2 = 'Hello'
print(string_2[2:3])
print(string_2[-2:-1])
print(string_2[:5])
print(string_2[:-2])
print(string_2[::2])
print(string_2[1::2])
print(string_2[::-1])
print(string_2[:1:-1])
print(len(string_2))

# 6
ints = [1, 23, 456]
for i in ints:
	print(int(str(i)[-1]))

# 7
print('Кол-во десятков в трехзначном:')
values = [123, 456, 789]
for i in values:
	print(int(str(i)[1]))
print('---------------------------')

# 8 
print('Сумма цифр:')
digits = [1,23,456,7890]
for i in digits:
	ls = str(i)



