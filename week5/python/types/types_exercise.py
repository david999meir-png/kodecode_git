# exersice 1
my_num = int(input("enter number"))

print(my_num % 2 == 0)

# exersice 2

x = 5
y = 10

x += y
y = x - y
x = x - y

print (f"x = {x}")
print(f"y = {y}")

# exersice 3
print("exersice 3")
my_number = 456
print(my_number // 100 + my_number % 100 // 10 + my_number % 10)

print("exersice 4")
weight = int(input("enter weight:"))
height = float(input("enter height:"))
print(round(weight / (height**2), 2))

print("exersice 5")
decimal_num = input("enter deciamal number:") #47.54
print(int(float(decimal_num)))
print(round(float(decimal_num) - int(float(decimal_num)), 2))
