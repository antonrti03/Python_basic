# main.py
# Tu package lay ra modules: Và đây cũng là cách mà mọi người thường làm và bạn cũng nên theo.
from kteam_package import module_a as mod_a, module_b as mod_b

mod_a.func()
print(mod_a.a_var)

mod_b.func()
print(mod_b.b_var)
