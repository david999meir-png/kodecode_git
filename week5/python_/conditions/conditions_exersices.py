# exersice 1
age = int(input("anter age:"))

if 0 > age or age > 120:
    print("invalid")

elif age <= 12:
    print("caild")

elif age <= 17:
    print("teen")

else:
    print("adult")

# exersice 2
character = input("please enter a character:")
vowel_ = ["a", "e", "i", "o", "u"]

if not character.isalpha() or not character.isascii():
    print("invalid")

elif character.lower() in vowel_:
    print("Vowel")

else:
    print("Consonant")

# exersice 3
age_ = int(input("enter age:"))
VIP_CARD = input("do you have a VIP card? yes / no\n")

if age_< 16:
    print("permission denaid...")

elif (age_>= 18 and VIP_CARD.lower() == "yes") or 21 >= age_>= 19:
    print("welcome...")

# exersice 4
password = "12345678"

user_password = input("enter your password:\n")

if user_password == password:
    print("Access Granted")

elif len(user_password) < 8:
    print("too short...")

else:
    print("wrong password...")

# exersice 5
x = int(input("enter coordinates of X"))
y = int(input("enter coordinates of Y"))

max_range_X = 50
min_range_x = 10
max_range_Y = 80
min_range_Y = 20

if max_range_X > x > min_range_x and max_range_Y > y > min_range_Y:
    print("Inside the rectangle")

elif x == max_range_X or x == min_range_x or y == min_range_Y or y == max_range_Y:
    print("on the edge")

else:
    print("Outside the rectangle")

# exersice 6
user_name = input("enter your name:") or "anonymos"
print(f"hi {user_name} nice to see you!")

# exersice 8*
num1 = int(input("enter first number:\n"))
num2 = int(input("enter second number:\n"))
num3 = int(input("enter third number:\n"))

print(f"som of the positive numbers: {(num1 > 0) + (num2 > 0) + (num3 > 0)}")

# exersice 10*

user_score = int(input("enter your score:\n"))
print("A") if 90 <= user_score <=100 else print("B") if 80 <= user_score < 90 else print("C") if 70 <= user_score < 80 else print("F") if user_score < 70 else print()

