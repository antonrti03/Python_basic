# tra ve dia chi cua gia tri trong bo nho
a = id(67) 
print(a)

id      variable
0x88898|Kteam
....|....
....|....
....|....

# tra ve dia chi cua gia tri trong bo nho
b = 'Kteam'
a = id(b)
c = id('Kteam')
print(c)

# toan tu
n = 69
print(n)
print(n+1)
print(n.__add__(1)) # tuong tu + 1
print(n.__sub__(1)) # -1
print(n.__neg__())


# Hash object
s_1 = 'how'
s_2 = 'python'

s_1 = s_1 + 'hello'
s_2+= 'hello'
print(id(s_1))
print(id(s_2))

# unHash object
s_1 = [1, 2]
print(id(s_1))
s_1+= [3, 4]
print(id(s_1))

# Gan tuong duong giua hash - unHash object
s_1 = [1, 2]
s_1.append(3)
print(s_1)
s_2 = [1, 2]
s_2+=(3,)
print(s_2)