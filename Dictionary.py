# la 1 container dung Key de phan biet
# dung cap Key : Value
# key la hash object
dic = {'name': 'Kteam', 'member': 69}
print(dic)
print(type(dic))

# Dict Comprehension
dic = {key: value for key, value in [('name', 'Kteam'), ('member', 69)]}
print(dic)
print(type(dic))

# Khoi tao Dict tu mapping object


# Khoi tao Dict bang Iterator
iter_ = [('name', 'Kteam'), ('member', 69)]
dic = dict(iter_)
print(dic)
print(type(dic))

# Khoi tao Dict bang keyword arguments
name = 'SpaceX' #day la bien
member = 696969
dic = dict(name='Kteam', member=69) #day la key
print(dic)
print(type(dic))
# Ten bien trung ten Key nhung ko a/h gi

# Khoi tao Dict su dung fromkeys
iter_ = ('name', 'number')
dic_none = dict.fromkeys(iter_)
print(dic_none)
dic = dict.fromkeys(iter_, 'non None value')
print(dic)


# Lay value trong Dict = Key
dic = {'name': 'Kteam', 'member': 69}
print(dic['member'])

# Thay value trong Dict = Key
dic = {'name': 'Kteam', 'member': 69}
dic['member'] = 96
print(dic)
dic['member'] = dic['member'] + 1
dic['name'] = dic['name'] + '- Anton'
dic['add'] = 900
print(dic)

# Cac phuong thuc cua Dict
# COPY
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.copy()
print(dic)
print(d_2)

# CLEAR
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.copy()
d_2 = d_2.clear()
print(dic)
print(d_2)

# GET
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.get('name1', 'Default')
print(dic)
print(d_2

# items()
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.items()
print(dic)
print(d_2)

# keys(): lay ra key
d = {'team': 'Kteam', (1, 2): 69}
keys = d.keys()
print(keys)
print(type(keys))
list_keys = list(keys)
print(list_keys)

# .values(): lay ra value
d = {'team': 'Kteam', (1, 2): 69}
values = d.values()
print(values)
print(type(values))
list_values = list(values)
print(list_values)

# .pop(): bo di phan tuco key trong dict
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.pop('name')
print(dic)
print(d_2)

# .pop(): bo di phan tuco key trong dict
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.pop('name1', 'Khong co')
print(dic)
print(d_2)

# .popitem(): loai bo cap key-value in Dict
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.popitem()
print(dic)
print(d_2)

# .setdefault(key, default): add key-value in Dict
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.setdefault('age')
print(dic)
print(d_2)

# .update(): add key-value in Dict
dic = {'name': 'Kteam', 'member': 69}
d_2 = dic.update(age=25)
print(dic)
print(d_2)