# SHIFT + Rigth Mouse
# D:\Python_OpenCV\Python_basic>Number.py
# Built = Subline: Ctrl + B
# Python supports kieu phan so, so phuc (ngon ngu khac ko ho tro)

#gan so nguyen cho a (interger), python ko gioi han so luong so
a = 4 
print(a)
print(type(a))

# So thuc: co 15 so nam sau so thap phan
b = 1.96425767698943643463463636878678 
print(b)
print(type(b))
#-------------------------------------------------------------------
#De tinh chinh xac cho so thuc sau dau thap phan
# Su dung toan bo noi dung cua thu vien decimal
from decimal import*
#lay toi da 30 chu so phan nguyen va thap phan
getcontext().prec=30
f = 10/3
print(f)
print(type(f))
d = Decimal(10)/Decimal(3)
print(d)
print(type(d))
#-----------------------------------------------------------
#Tao phan so trong Python
from fractions import*
g1 = Fraction(10,3)
print(g1)
print(type(g1))
g2 = Fraction(1,3)
g3 = g1 + g2
print(g3)
#----------------------------------------------------------
# So Phuc: complex numbet = <phan thuc>+<phan ao>j
c1 = complex(2,5)
print(c1)
print(c1.real)
print(c1.imag)

#----------------------------------------------------------
# Toan tu co ban trong Python
# X+Y; X-Y; X*Y; X/Y; X//Y: thuong nguyen; X%Y: phan du; 
# X**Y: luy thua

#----------------------------------------------------------
# Thu vien Math trong Python
# import <ten thu vien>
# <ten thu vien>.<ten ham> : 
# .trunc(x); .floor(x); .ceil(x); .fabs(x); .sqrt(x); .gcd(x,y)
import math
math.sqrt(9)