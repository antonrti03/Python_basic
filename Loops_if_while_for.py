# IF - ELIF - ELSE
a = 0
b = 3
if a-1 < 0:
	print('a nho hon 1');
elif a-1 > 3:
	print('OK');
# if - else
if b-1 < 0:
	print('b nho hon 1');
else:
	print('Yes')


# while, break-continue, while-else
k = 5
while k > 0:
	print('k = ', k)
	k -= 1

# Xu ly string, list, tuple

s = 'How Kteam'
idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
length = len(s) # lấy độ dài chuỗi làm mốc kết thúc
while idx < length:
	print(idx, 'stands for', s[idx])
	idx += 1 # di chuyển index tới vị trí tiếp theo


# Break
#Trong trường hợp vòng lặp a chứa vòng lặp b. Trong vòng lặp b chạy câu
#lệnh break thì chỉ vòng lặp b kết thúc, còn vòng lặp a thì không.

five_even_numbers = []
k_number = 1
while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
    five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
        if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
            break # thì kết thúc vòng lặp
    k_number += 1

print(five_even_numbers)
print(k_number)

# Continue
k_number = 1
while k_number < 10:
	if k_number % 2 == 0: # nếu k_number là số chẵn
		k_number += 1 # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
		continue
	print(k_number, 'is odd number')
	k_number += 1


# while - else
# khi vòng vòng lặp while kết thúc thì khối 
# lệnh else-block sẽ được thực hiện.
k = 0
while k < 3:
	print('value of k is', k)
	k += 1
else:
	print('k is not less than 3 anymore')

# For
# Dung while de duyet list, string or tuple
length = 3
iter_ = (x for x in range(length)) #iterator = danh sach
c = 0
while c < length:
	print(next(iter_))
	c += 1

# Neu ko biet len() dung try-block
iter_ = (x for x in range(3)) # giả sử ta không biết có 3 phần tử
while 1: # 1 là một expression True
	try:
		print(next(iter_))
	except StopIteration:
		break

# For
# for variable_1, variable_2, .. variable_n in sequence:
iter_ = (x for x in range(3))
for value in iter_:
	print('->', value)

# for cho Dict
howkteam = {'name': 'Kteam', 'kter': 69}
print( howkteam.items())
list_values = list(howkteam.items())
print(list_values)
print(list_values[0])
print(list_values[1])
# dung cho Dict using For
for key, value in howkteam.items():
	print(key, '=>', value)

# Break in For
s = 'How Kteam'
for ch in s:
	if ch == ' ':
		break
	else:
		print(ch)

# for-else
for k in (1, 2, 3):
	print(k)
else:
	print('Done!')

# range: day so
k = range(3)
print(k[0])

print(list(range(9, 2, -1)))

#Range là một lớp được thiết kế riêng để lưu giữ những dãy số. Vậy nên nó đã
#được những kĩ sư Python sử dụng các thuật toán để có thể có được sự linh
#hoạt này.

lst = [5, (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(lst)):
	print(lst[i])


# sequence scan - indexing scan

# sequence scan
lst = [1, 2, 3]
for value in lst:
	value += 1
	print(value)
print(lst)

# indexing scan
lst = [1, 2, 3]
for i in range(len(lst)): #tao ra 1 day so tu len()
	lst[i] += 1
print(lst)

# comprehension
lst = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam',
'EDUCATION'), ('chia', 'se', 'FREE')]]
print(lst)

# ko dung comprehension

lst = []
for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'se', 'FREE')]:
	a = a.capitalize()
	b = b.upper()
	c = c.lower()
	lst.append('--'.join((a, b + c)))
print(lst)


#
dic = {key:value + 1 for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)) if value % 2 != 0}
print(dic)

dic = {}
for key, value in (('Kteam', 69), ('Too', 50), ('Tun', 14), ('Free Education', 93)):
	if value % 2 != 0:
		dic[key] = value + 1

print(dic)


# enumerate: enumerate(iterable[, start])
student_list = ['Long', 'Trung', 'Giau', 'Thanh']
for student in student_list:
	print(student)

gen = enumerate(student_list)
print(gen)

en = list(gen)
print(en)

for idx, student in enumerate(student_list, 1):
	print(idx, '=>', student)
