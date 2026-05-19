print("exersice 1")

couneter = 0

def bump() -> None:
    global couneter
    couneter += 1


def value() -> None:
    global couneter
    print(couneter)

bump()
bump()
bump()

value()



print("exersice 2")

def make_counter():
    couneter_2 = 0
    
    def return_counter():
        nonlocal couneter_2
        couneter_2 += 1
        print(couneter_2)
    
    return return_counter

c = make_counter()
a = make_counter()
c()
c()
c()
a()



print("exersice 3")

x = "global"
def outer():
    x = "enclosin"   # local x
    def inner():
        x = "local"  # local x
        print(x)  
    inner() # = local
    print(x) # = enclosin
outer()
print(x) # global



print("exersice 4")

# דרסנו משתנה build של פייתון ועכשיו המתודות הרגילות של list נעלמו
# list = [1, 2, 3] 
# print(list(range(5)))

list_1 = [1, 2, 3]
print(list(range(5)))


print("exersice 5")
import main



print("exersice 6")
import tools



print("exersice 7")

import datetime as ti
print(ti.datetime.now())



print("exersice 8")

def public_names(library) -> list:
    return sorted([k for k, v in library.__dict__.items() if not k.startswith("_")])

import math
print(public_names(math))



print("exersice 9")

def add_item(item, bag=[]):
    bag.append(item)
    return bag

def fix_add_item(item, list_):
    list_.append(item)

# when you create a list in difaolt, the func returns the same list
# all the time, for fixing the problem, we need use our list 



print("exersice 10")
from geometry import circle, rectangle


print(circle.area(5))
print(rectangle.area(4, 6))