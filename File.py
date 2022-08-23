#open(file, mode='r', buffering=-1, encoding=None, errors=None,
#newline=None, closefd=True, opener=None)
file_object = open('kteam.txt', 'a+')
print(file_object)

# Phuong thuc: read
file_object = open('kteam.txt')
data = file_object.read(6)
file_object.close() #dua con tro ve dau hang
print(file_object)
print(data)

# Phuong thuc: readline - doc 1 dong
file_object = open('kteam.txt')
data = file_object.readline()
data1 = file_object.readline()
file_object.close() #dua con tro ve dau hang
print(data)
print(data1)

# Doc phai = iterable
file_object = open('kteam.txt')
data = list(file_object)
file_object.close() #dua con tro ve dau hang
print(data)

# Ghi file: <File>.write(text)
file_object = open('kteam.txt', 'a+')
data = file_object.write('\nKteam')
file_object.close() #dua con tro ve dau hang
print(data)

# Kiem soat con tro file
file_object = open('kteam.txt', 'r')
data = file_object.read() #Dua tro ve cuoi file
file_object.seek(0) #Dua tro ve 0
data2 = file_object.read() 
file_object.close() #dua con tro ve dau hang
print(data)
print(data2)