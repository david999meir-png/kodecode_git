# exercise 1
class Animel:
    def __init__(self, name):
        self.name = name


    def speak(self):
        return "..."

class Dog(Animel):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "woor"

r = Dog("rex")
print(r.speak())


# exercise 2
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return "a vehicle"

class Car(Vehicle):
    pass

a = Car("ddd")
print(a.describe())


# exercise 3
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    

# exercise 4
class Logger:
    def __init__(self, msg):
        self.msg = msg
    
    def log(self):
        return self.msg


class TimeLogger(Logger):
    def __init__(self, msg, time):
        super().__init__(msg)
        self.time = time
    
    def log(self):
        return f'[{self.time}] {self.msg}'


# exercise 5
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2


class Trianglee:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width
    
shapes = [Circle(4),
          Trianglee(4, 5),
          Square(7, 7)
                        ]
sum_area = 0
for shape in shapes:
    print(shape.area())
    sum_area += shape.area()

print(sum_area)



# exercise 6
class Cat:
    def __init__(self):
        pass

    def speak(self):
        return "miau"


class Duck:
    def __init__(self):
        pass

    def speak(self):
        return "gagaga"


def make_them_speak(animals):
    for i in animals:
        print(i.speak())

make_them_speak([Cat(), Duck()])


# exercise 7
class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name, living_area):
        super().__init__(name)
        self.living_area = living_area


class Dog(Mammal):
    def __init__(self, name, living_area, bite):
        super().__init__(name, living_area)
        self.bite = bite


# exercise 8
def count_dogs(animals):
    counter = 0
    for i in animals:
        if not isinstance(i, Dog):
            continue
        counter += 1
    return counter


# exercise 9
class Shape:

    def __str__(self):
        pass


class Square1(Shape):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'square {self.x}'


class Circle2(Shape):
    def __init__(self, ra):
        self.r = ra
    
    def __str__(self):
        return f'circle r = {self.r}'

shapes = [Square1(5), Circle2(4)]
print(shapes[0])
print(shapes[1])


# exercise 10
from abc import ABC, abstractmethod


class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        return amount
    

class CardPayment(Payment):
    ...

# feild = Payment()
# field_2 = CardPayment()
good = CashPayment()
