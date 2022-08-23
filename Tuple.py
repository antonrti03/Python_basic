# Ve co ban giong het list
# tiet kiem bo nho hon list
# chay nhanh hon list
# Hash Object: khong the thay doi noi dung
tub = (1, 2, 3, 4, 5, 2)
print(tub)

tub = (1)
print(tub)

#khac list
tub = (i for i in range(10))
print(tub)

#structor tuble
tub = (i for i in range(10) if i % 2 == 0)
a = tuple(tub)
print(a)

#Toan tu +
tub = (1, 5, 9)
a = tub + (2, 4 ,6)
print(a)

#Matrix
tub = ((1, 2, 3), (4, 5 ,6), (7, 8 ,9))
print(tub)

#Indexing
tub = (1, 5, 9)
a = tub[0]
print(a)

#len
tub = (1, 5, 9)
a = len(tub)
print(a)

#count
tub = (1, 1, 2, 3)
a = tub.count(1)
print(a)

#Tim idex
tub = (1, 1, 2, 3)
a = tub.index(3)
print(a)