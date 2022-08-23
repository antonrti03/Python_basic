# Bai 12
#  gioi ban = []
# cac phan tu cach nhau boi dau ','
# List co kha nang chua moi gia tri cua doi tuong va chinh no
# 
a = [1, 2, 3, 'Kteama']
b = [[1 , 2 , 3], [1, [1, 2]], [], 'Kteama']
print(a)
print(b)
#convehence list
a = [i for i in range(4)]
b = [[n, n*2, n*3] for n in range(1,4)]
print(a)
print(b)

# iterable
a = list('Kteam')
b = [[n, n*2, n*3] for n in range(1,4)]
print(a)
print(b)

a = [1, 2]
a = a + ['one', 'two']
print(a)

# Toan tu *
a = [1, 2]
a *= 2
print(a)

# Toan tu 'in'
a = [1, 2]
b = 1 in a
print(b)

# Toan tu indexing
a = [1, 2, 'a', 'b', 'Kteam', [3, 4]]
b = a[5][0]
b = a[1:3]
print(b)

# Toan tu gan
a = [1, 2, 'a', 'b', 'Kteam', [3, 4]]
a[1] = 'Ktea'
b = a[1]
print(b)
print(a)

# Matrix = list in list
a = [[1, 2, 3], [4, 5 ,6], [7, 8, 9]]
print(a[0])
print(a[1])
print(a[0])

print(a[0][0])
print(a[1][0])
print(a[2][0])

# Luu y: ko gan list nay sang list khac 
# (2 bien tham chieu dung chung 1 vung nho)-> thay doi vung nho
a = [1, 2, 3]
b = a
print(b)
print(a)

b[0]= 'Kteam'
print(b)
print(a)
# De xu ly dung constructer list: tao ra vung nho khac
a = [1, 2, 3]
b = list(a)
b[0] = 'hello'
print(b)
print(a)

# Bai 13
# Count(a): tra ve so lan xuat hien cua 'a'
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.count(1)
print(c)

# Index: tra ve vi tri cua phan tu
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.index(3)
print(c)

# Copy: tao ra 1 list moi
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.copy()
c[0] = 'Kr'
print(c)
print(a)

# clear: xoa phan tu trong list
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.clear()
print(c)
print(a)

# Cac phuong thuc cap nhat: append
# them phan tu vao cuoi list
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
a.append(10)
a.append([1,2])
a.extend([3,4])
print(a)

# Cac phuong thuc cap nhat: insert
# them phan tu vao cuoi list
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
a.insert(1, 5) # them 5 vao vi tri index 1
print(a)

# Cac phuong thuc cap nhat: pop
# lay ra phan tu trong list, cat ra khoi list ban dau
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.pop(2)
print(a)
print(c)

# Move: loai bo phan tu tai ()
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
c = a.remove(3) #bo di 3
print(a)
print(c)

# Reverse: dao nguoc lai phan tu trong list
a = [1, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
print(a)
a.reverse() # dao nguoc lai
print(a)

# sort: sap xep lai tang dan
a = [11, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
print(a)
a.sort() # dao nguoc lai
print(a)

# sort: sap xep lai tang dan
a = [11, 1, 3, 4, 5 ,6 ,7 ,8 ,9]
print(a)
a.sort(reverse=True)
print(a)