# Set la 1 container
set_1 = {69, 96}
print(set_1)
print(type(set_1))

set_2 = {'How Kteam'}
print(set_2)

set_3 = {(69, 'Free Education'), (1, 2, 3)}
print(set_3)

set_4 = {(69, 'Free Education'), (1, 2, 3), [1, 2]}
print(set_4)

# khong chua phan tu trung lap
set_1 = {69, 69, 96}
print(set_1)

# Set comprehension
set_1 = {i for i in range(5)}
print(set_1)

# Set constructor
set_1 = set('How Kteam')
print(set_1)
# khong quan tam den vi tri phan tu

# Toan tu: in
set_1 = {1, 2, 3}
a = 1 in set_1
print(a)

set_1 = {(1, 2), 3}
a = (1, 2) in set_1
print(a)

# Toan tu: -
set_1 = {(1, 2), 3}
set_2 = {3}
a = set_1 - set_2
print(a)

# Toan tu: &
set_1 = {(1, 2), 3}
set_2 = {3}
a = set_1 & set_2
print(a)

# Toan tu: |
set_1 = {(1, 2), 3}
set_2 = {4}
a = set_1 | set_2
print(a)

# Toan tu: ^
set_1 = {(1, 2), 3}
set_2 = {4}
a = set_1 ^ set_2
print(a)

#Indexing and Cut are not supported

# Phuong thuc: clear
set_1 = {(1, 2), 3}
set_1.clear()
print(set_1)

# Phuong thuc: discard
set_1 = {(1, 2), 3}
set_1.discard(3)
print(set_1)

# Phuong thuc: copy
set_1 = {(1, 2), 3}
a = set_1.copy()
print(a)