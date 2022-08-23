# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#Truyen vao rat nhieu du lieu bat ki.
print('Kteam', 69, '- Free education')
# use: sep -  them ky tu giua cac phan tu
print('Kteam', 69, '- Free education', sep='\n')

# end-''
print('Kteam', 69, '- Free education', end='||')

from time import sleep
print('line 1\n', 'line2', end='\n')
sleep(3) # dừng chương trình 3 giây
print('end...')

#save as File
with open('kteam.txt', 'w') as f:
	print('printed by print function', file=f)

# flush
from time import sleep # nhập hàm sleep từ thư viện time
print('start...', end='', flush=True)
sleep(3) # dừng chương trình 3 giây
print('end...')

# Print/3.x
from time import sleep
your_name = "Henry"
your_great = "Hello! My name is "
for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()