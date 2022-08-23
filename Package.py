# Run with folder: kteam_package
# Lay ra package: package.sub_package.module.
import kteam_package.module_a, kteam_package.module_b as mod_b #rut gon kteam_package.module_b

kteam_package.module_a.func()

print(kteam_package.module_a.a_var)

mod_b.func()

print(mod_b.b_var)

# main.py
# Tu package lay ra modules: Và đây cũng là cách mà mọi người thường làm và bạn cũng nên theo.
from kteam_package import module_a as mod_a, module_b as mod_b

mod_a.func()
print(mod_a.a_var)

mod_b.func()
print(mod_b.b_var)


# main.py
# imports tat ca modules = sd     __all_      trong      __init__.py
from kteam_package import *

module_a.func()
print(module_a.a_var)

module_b.func()
print(module_b.b_var)