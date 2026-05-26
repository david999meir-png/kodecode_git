# exercise 1
class Student:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    

# exercise 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.width


# exercise 3
class Thermometer:
    def __init__(self, celsius):
        self._celsius = celsius
            
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, cel):
        if cel < -273.15:
            raise ValueError
        self._celsius = cel


# exercise 4
class BankAccount:
    def __init__(self,name, balance):
        self.name = name
        self._balance = balance
    
    @property
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError
        self._balance -= amount
    

# exercise 5
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# exercise 6
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    

# exercise 7
class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def is_even(n):
        return n % 2 == 0


# exercise 8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def from_tuple(cls, t):
        return cls(t[0], t[1])
    

# exercise 9
class User:
    sum_users = 0
    def __init__(self, name):
        self.name = name
        User.sum_users += 1
    
    @classmethod
    def how_maney(cls):
        return User.sum_users


# exercise 10
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('negative price.')
        if not isinstance(new_price, (int, float)):
            raise TypeError('enter number only.')
        self._price = new_price
