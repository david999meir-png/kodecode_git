# exercise 1
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f'{self.name} says woof'

# exercise 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width
        

# exercise 3
class Counter:
    def __init__(self, amount=0):
        self.amount = amount
    
    def increment(self, amount):
        self.amount += amount


# exercise 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'


# exercise 5
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("ther is not enugh maney.")
        self._balance -= amount


# exercise 6
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    

# exercise 7
class Student:
    school = "kodcode"

    def __init__(self, name):
        self.name = name

a = Student('david')
b = Student('Alias')

a.name = "David"

print(a.name)
print(b.name)


# exercise 8
class Player:
    players = 0

    def __init__(self, name):
        self.name - name
        Player.players += 1


# exercise 9
class Money:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def is_more_than(self, other: Money):
        return self.amount > other.amount


# exercise 10
class Playlist:
    def __init__(self):
        self.songs_list = []

    
    def add_song(self, song):
        self.songs_list.append(song)
    
    def remove_song(self, song):
        self.songs_list.remove(song)
    
    def count_songs(self):
        return len(self.songs_list)

    def __str__(self):
        return self.songs_list
