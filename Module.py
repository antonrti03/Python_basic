# main.py

import a

a.say("How are you")
a.say("I'm Ok")
print(type(a))


#
# main.py
import a1

print(type(a1))

print(a1.var_module_a)
a1.func_module_a()
print(a1.local_var)


# main.py
# lay ra su dung 1 function tu Module
from a1 import func_module_a

func_module_a() # không cần phải sử dụng module object

# main.py
# Lay ra 2 functions in module
from a1 import var_module_a, func_module_a

print(var_module_a)
func_module_a()

# main.py
# Lay ra all functions in module a1

from a1 import *

print(var_module_a)

func_module_a()


# Import một module nhiều lần
# main.py

import a3

print(a3.var_module_a)

a3.var_module_a = 100

import a3

print(a3.var_module_a) #lay gia tri 100, ko quan tam den import lan 2 nua


# Import một module nhiều lần
# main.py

from a3 import var_module_a #chi la copy lay gia tri, ko thay doi gtri trong module a3

var_module_a = 100

import a3  #reset lai Module a3

print(a3.var_module_a) #tra gia tri nam trong module, ko quan tam 100


# Lưu ý về list object khi import
# main.py
from a4 import num, lst

num = 200
lst[0] = 100

import a4 #reset lai module a4

print(a4.num)
print(a4.lst) #co gia tri khac do gan gia tri cho list la gan dia chi


#reload
# main.py

import a5

a5.var = 20
print(a.var)

import a5
print(a5.var)

from importlib import reload

reload(a5)
print(a5.var)


# Đổi tên module, attribute khi import

# main.py

import a_long_name_for_a_module as mdule
from a_long_name_for_a_module import a_long_name_for_a_variable as longvar,\
                a_long_name_for_a_function as longfunc

print(mdule.short_name)
print(longvar)
longfunc()