# SHIFT + Rigth Mouse
# D:\Python_OpenCV\Python_basic>String.py
# Built = Subline: Ctrl + B
# Python supports kieu phan so, so phuc (ngon ngu khac ko ho tro)
#----------------------------------------------------------
# Nhay don
''
# Nhay kep
""
# Nhay khac: chuoi nhieu dong
''''''
""""""
#
strH = 'How kteam'
print(strH)
print(type(strH))

strH1 = "I'm a beginner"
print(strH1)
print(type(strH1))

# Chuoi nhieu dong
strH2 = '''
HowKteam.com
Free education
Share tobe better
'''
print(strH2)

strH3 = """
HowKteam.com
Free education
Share tobe better
"""
print(strH3)

strH4 = """HowKteam.com\nFree education\nShare tobe better"""
print(strH4)

#
print('\a') #beep
#------------------------------------
# Chuoi tran:
print(r'Haizz, \neu mot ngay nao do')

#---Toan tu +------
strA = "HowKteam.com"
strB = "Free edu"
strC = strA + "\n" + strB
print(strC)

#---Toan tu x------
strA = "HowKteam.com"
strC = strA*5
print(strC)

# Tim xem B co ton tai trong A khong?
strA = "HowKteam.com"
strB = "k"
strC = strB in strA
print(strC)

#Indexing trong string: [0]->[n-1]
strA = "abc xyz"
strB = strA[1]
strC = strA[-1]
strD = strA[len(strA)-1]
print(strB)

#Cut string: left to rigth
strA = "abc xyz"
strB = strA[1:5]
strC = strA[None:None]
strD = strA[:]
strC = strA[None:5:1] # step =1
strC = strA[None:5:-1] # step =1, cut nguoc lai
print(strB)


# Convert string to number
strA = "69"
strB = int(strA)+5 # float(strA)
print(strB)

# Covert number to string
strA = 69
strB = str(strA) + "5"
print(strB)

# Replace char in string:
strA = "abc xyz"
strA = strA[None:1] + "0" + strA[2:None]
print(strA)
print(hash(strA))

#=================================================
#https://www.howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-chuoi-trong-python--phan-3-1545
# Dinh dang chuoi trong Python
# 1. Dinh dang chuoi bang %s, %r, %d, %.2f
a = 'My name is %s' %('Kteame')
print(a) #My name is Kteame

a = 'My name is %s %s' %('Kteame','1')
print(a)

s = '%s %s'
re = s %('1', '2')
print(re)

#f = '%.2f' %(3.4999)
#print(f)
#
k = 'Ab'
re = f'{{k}}'
print(re) # not run

# 2.Dinh dang bang phuong thuc Format
'a: {}, b: {}, c: {}'.format(1,2,3) # truyen vao theo thu tu
# truyen vao theo Index
'a: {1}, b: {2}, c: {0}'.format('one','two', 'three')
#truyen bien vao string
'1: {one}, 2: {two}'.format(one=10, two=20) 
# Can le cua phuong thuc format
# {:(c)<n}: can le trai
# {:(c)>n}: can le phai
# {:(c)^n}: can le giua
r = '{:^10}'.format('abc')
print(r)

r = '{:*^10}'.format('abc')
print(r)

r = 'How {:*^10} - Free education'.format('Kteam')
print(r)
#
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)


# Bai 10: string continue
a = 'how kteam - free'
b = a.capitalize() #viet hoa dau string
print(b)

a = 'how kteam - free'
b = a.upper() #viet hoa all
print(b)

a = 'how kteam - Free'
b = a.lower()
print(b)

a = 'how kteam - Free'
b = a.swapcase()
print(b)

a = 'how kteam - Free'
b = a.title() #Viet hoa chu cai dau cua tu
print(b)

a = 'Kteam'
b = a.center(30, '*') #dua string vao giua don vi can
print(a)
print(b)

a = 'Kteam'
b = a.rjust(30, '*') #can phai
print(a)
print(b)

a = 'Kteam'
b = a.ljust(30, '*') #can trai
print(a)
print(b)

a = 'Kteam'
b = a.encode() #chuyen ma hoa theo chuan
print(a)
print(b)

a = 'Kteam'
b = a.join(['1', '2', '3']) #add them de keo dai string
print(a)
print(b)

a = 'Kteam tree'
b = a.replace('t', 'F', 2) #thay the, bao lan
print(a)
print(b)

a = '  Kteam tree   '
b = a.strip() #xoa 2 khoang dau, cuoi = 'char'
print(a)
print(b)

a = '  Kteam tree   '
b = a.lstrip() #xoa khoang cuoi = 'char'
print(a)
print(b)

# Bai 11: string
a = 'how kteam free'
b = a.split(' ') #chia cac phan tu thanh char list: cat khoang trang or char
print(a)
print(b)

a = 'how kteam free'
b = a.split(' ', 1) #cat 1 lan
print(b)

a = 'how kteam free'
b = a.rsplit(' ', 1) #cat 1 lan tu phai
print(b)

a = 'how kteam free'
b = a.partition('k') #tim den 'k' roi cat string truoc va sau 'k'
print(b)

a = 'how kteam free'
b = a.count('k') #dem so luong 'k' trong string
print(b)

a = 'how kteam free'
b = a.count('k',0,3) #dem so luong 'k' trong string tu 0 den 3
print(b)

a = 'how kteam free'
b = a.startswith('h') #co bat dau bang 'h' ko?
print(b)

a = 'how kteam free'
b = a.startswith('k',0,5) #co bat dau bang 'h' ko?
print(b)

a = 'how kteam free'
b = a.endswith('e') #co bat dau bang 'h' ko?
print(b)

a = 'how kteam free'
b = a.find('t') #return a index
print(b)

a = 'how kteam free'
b = a.islower() #viet thuong ko?
print(b)

a = 'how kteam free'
b = a.isupper() #viet thuong ko?
print(b)

a = '5'
b = a.isdigit() #kiem tra so
print(b)

a = '   '
b = a.isspace() #kiem khoang trang?
print(b)