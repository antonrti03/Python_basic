#----------28----------------------------
# Khai bao ham
# def <function_name>(parameter_1, parameter_2, .., parameter_n):
def kteam():
	pass # giu cho khi chua biet viet gi
print(kteam())
print(kteam)

# Goi ham <function>()
def kteam():
	print('Hello kteam')

kteam()
kteam()
kteam()


# Parameter và Argument
def kteam(text): # Param = text
	print(text)

kteam('Hello Kteam') # Arguments = 'Hello Kteam'
kteam(100)


# Parameter và Argument
def kteam(text, age): # Param = text
	print(text)
	print(age)

kteam('Hello Kteam', 69) 

# Parameter và Argument
def kteam(greating, name):
	print(greating, name + '!')

kteam('Hello', 'SpaceX') 

# Parameter và Argument default
def kteam(name, greating='Hi'):
	print(greating, name + '!')

kteam('Kteam')

#-----29-------------------------------------
#POSITIONAL VÀ KEYWORD ARGUMENT

def kteam(a, b):
	pass #lenh giu cho

kteam(3, 'Kteam')
# 3, 'Kteam': positional argument -> gan lan luot
kteam(b=3, a='Free Education') #gan ko can lan luot
# 3, 'Free Education': keyword argument

def kteam(a, b):
	print('a', a)
	print ('b', b)

kteam(a=3, b=4)
kteam(b=3, a=4)

# Dung Keyword argument khi co nhieu default argument value.
def Teo(a, b=2, c=3, d=4):
	f = (a + d) * (b + c)
	print(f)

Teo(2)
#Muon truyen lai value cho param nao do:
Teo(2, d=5)

#Python cho phép chúng ta tạo ra các parameter chỉ nhận giá trị bằng việc
#pass argument theo kiểu keyword argument.
# def function (*, key_arg1, key_arg2):
def kteam(pos_or_key_arg, *, key_arg1, key_arg2):
	print(pos_or_key_arg)
	print(key_arg1)
	print(key_arg2)
# Sau * chi la Keyword arguments
kteam(1, key_arg1=2, key_arg2='Kteam')

#----------30----------------------------
#Packing và unpacking arguments
#Unpacking
def kteam(k, t, e, r):
	print(k)
	print(t, e)
	print('end', r)
lst = ['123', 'Kteam', 69.96, 'Henry']
kteam(*lst) #unpack cac phan tu
#chi dung duoi dang Positional arguments

#Packing
# Goi tat ca cac value truyen vao = positional
# argument thanh 1 Tuple
def kteam(*args): #args - packing param
	print(args)
	print(type(args))
kteam('Kteam', 69.96, 'Henry')
kteam(*(x for x in range(7))) #unpack sau đó là pack
'''
Nếu sau một packing parameter còn có những parameter khác, khi gọi hàm
muốn truyền giá trị vào cho các parameter sau packing parameter bạn cần
phải sử dụng keyword argument.
'''
def f(*args, kter):
	print(kter)
f('1', '2', kter='3')
f('1', '2')

# Unpacking arguments với **
dic = {'name': 'Kteam', 'member': 69}
def kteam(a, b):
	print(a)
	print(b)
kteam(*dic)  # chi ra Keys
# Muon lay value phai thay ten bien = key + **
def kteam(name, member):
	print('name: ',name)
	print('member: ', member)
kteam(**dic)

# Packing arguments với **
def kteam(**kwargs):
	print(kwargs)
	print(type(kwargs))
kteam(name='Kteam', member=69)

#--------31------------------------------
#Biến locals và globals

#Khai báo biến ở trong hàm: local variable
#Khai bao bien ngoai ham, sd trong Function
kteam = 'How Kteam'
def say_slogan():
	print("We are", kteam)
say_slogan()

#Khai bao bien in Function, sd trong Function
# chi sd trong 1 function do
def say_slogan():
	kteam = 'How Kteam'
	print("We are", kteam)
say_slogan()
print(kteam)

#Global variable
def make_slogan():
# khởi tạo với global không có giá trị nhé
	global kteam
# sau khi khởi tạo xong, ta mới gán giá trị
	kteam = 'How Kteam'
make_slogan() #phai chay truoc
print(kteam)

#trường hợp là tên biến local trùng với tên
biến global
def make_global():
	global x
	x = 1
def local():
	x = 5
	print('x in local', x)
make_global()
print(x)
local()
print(x)

#pass by reference: tham chieu = dua ban goc
#pass by value: tham tri = dua ban sao

#pass by value
num = 69
st = 'How Kteam'
lst = [1, 2, 3]
tup = tuple('Education')
def change(parameter):
	parameter = 'New value'
	print('Changed successfully!')
change(num)
change(st)
change(lst)
change(tup)
print('*' * 10)
#--------------
print('{}\n{}\n{}\n{}\n'.format(num, st, lst, tup))
#Khong co gtri nao thay doi trong cac bien

#Luy y khi su dung List cos dung Indexing
lst = ['How Kteam', 1, 2]
def change(parameter):
	parameter[1] = 'New value'
	print('Changed successfully!')
print(lst)
change(lst)
print(lst) #bi thay doi do tro Indexing

#Giới thiệu hàm locals và globals
print(locals())

#------32-----------------------------------
#Return

#return [object]
def cal_rec_per(width, height):
	per = (width + height) * 2
	return per
# Gan vaue cho 2 bien
rec_1_width = 5
rec_1_height = 3
# khởi tạo một biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)

#khong chay sau khi co return
def _return_ter_func():
	print('chúng ta sử dụng return để ngắt hàm')
	# dòng dưới đây tương tự như bạn viết return None
	return
	print('Hàm print này dĩ nhiên không được gọi')
none = _return_ter_func()
print(type(none))

#return nhiều giá trị cùng một lúc
def cal_rec_area_per(width, height):
	perimeter = (width + height) * 2
	area = width * height
	return perimeter, area
rec_width = 3
rec_height = 9
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)
print(rec_per, rec_area)

#-----33--------------Yield--------------

#Generator: la 1 iterator
kteam_gen = (value for value in range(3))
for value in kteam_gen:
	print(value)
#Tai su dung lai khong duoc
for value in kteam_gen:
	print(value)

# Yield: giong return (tra ve oject) nhung tra ve
# 1 generator
def square(lst):
	sq_lst = []
	for num in lst:
		sq_lst.append(num**2)
	return sq_lst
kteam_ret = square([1, 2, 3])
for value in kteam_ret:
	print(value)
#Yield
def square(lst):
	for num in lst:
		yield num**2
kteam_gen = square([1, 2, 3])
for value in kteam_gen:
	print(value)

#test
def gen():
	for value in range(3):
		print('yield', value + 1, 'times')
		yield value
for value in gen():
	print(value)

#Phương thức send
#generator.send(value)
def gen():
	for i in range(4):
		x = yield i
		print('value sent from you', x)
g = gen() # gán generator này cho biến g
print(next(g)) # gọi hàm next để chạy lệnh yield "x = yield i"
g.send('Kteam')
print(next(g))

#test
def gen():
	while True:
		x = yield
		yield x**2
g = gen()
print(next(g))
print(g.send(2))
print(next(g))
print(g.send(10))

#----34----------lambda------------------
#lambda argument_1, argument_2, …, argument_n : expression

def ave(a, b, c):
	return (a + b + c)/3
print(ave(1, 3, 2))
#lambda
ave = lambda a, b, c: (a + b+ c)/3
print(ave(1, 3, 2))

x_power_a = lambda x, a=2: x ** a
print(x_power_a(2))
print(x_power_a(2,3))
print(type(x_power_a))
#lambda cũng phân biệt global và local

#dung thay def
kteam_lst = [lambda x: x**2, lambda x: x**3, lambda x: x**4] 
print(kteam_lst[0])
print(kteam_lst[0](2)) #2^2
print(kteam_lst[-1](2)) #2^4
for func in kteam_lst:
	print(func(3)) # 3**2, 3**3, 3**4

#Câu điều kiện cho lambda
#b if a else c
find_greater = lambda x, y: x if x > y else y
print(find_greater(1, 3))
print(find_greater(6, 2))

#test
cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print(cd_of_2_3(6))
print(cd_of_2_3(8))

#----34-----Functional tools----------------
# map(func, iterable)
kteam = [1, 2, 3, 4]
kteam_updated = []
for value in kteam:
	kteam_updated.append(value + 1)
print(kteam_updated)
#map ruong duong
def inc(x): return x + 1
kteam = [1, 2, 3, 4]
print(list(map(inc, kteam)))
#map + lambda
kteam = [1, 2, 3, 4]
print(list(map(lambda x: x + 1, kteam)))

#map(func, *iterable)
func = lambda x, y: x + y
kteam_1 = [1, 2, 3, 4]
kteam_2 = [5, 6, 7, 8]
kteam = map(func, kteam_1, kteam_2)
print(list(kteam))

#filter(function or None, iterable)
func = lambda x: x > 0
kteam = [1, -3, 5, 0, 2, 6, -4, -9]
print(list(filter(func, kteam)))
#tuong tu
kteam = [1, -3, 5, 0, 2, 6, -4, -9]
print([x for x in kteam if x > 0])

#Hàm reduce: reduce(function, sequence[, initial])
from functools import reduce
kteam_add = lambda x, y: x + y
kteam = [1, 2, 3, 4, 5]
print(reduce(kteam_add, kteam)) # ((((1+2)+3)+4)+5)

#-----35----De quy----(recursion)-----------
def cal_sum(lst):
	if not lst: # tương đương if len(lst) == 0:
		return 0
	else:
		return lst[0] + cal_sum(lst[1:])
print(cal_sum([1, 2, 3, 4]))
