# exersice 1

for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i == 7:
        break
    print(i)

# exersice 2
password = "1234"

while True:
    uder_try = input("enter password:\n")
    if uder_try == password:
        print("welcome!")
        break
    print("try again")
# when you don't know how many times it will take untiil the user will enter a correct password tou must use while loop.

# exersice 3
all_names = []

while True:
    name_ = input("enter name:\n")
    if name_.lower() == "done":
        break
    all_names.append(name_)
    
[print(name) for name in all_names]

# exersice without number..
for row in range(1, 4):
    for column in range(1, 4):
        if row == column:
            break
        print(row, column)

# exersice 4
the_str = input("enter some text, it'll count all the voewles.\n")
voweles_ = ["a", "i", "u", "o", "e"]
sum_voweles = 0
for letter in the_str:
    if letter.lower() in voweles_:
        sum_voweles += 1

print(f"sum of voweles: {sum_voweles}")

# exersice 5

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

# exersice 6
user_str = input("enter some text:\n")

for i in range(len(user_str)):
    print(f"{user_str[len(user_str)-1 -i]}", end="")

# exersice 7
user_num = int(input("enter number:\n"))
sun_evens = 0

while user_num > 0: # 8547
    if(user_num) % 10 % 2 == 0:
        sun_evens += 1
    user_num = user_num // 10

print(f"some all evens: {sun_evens}")

# exersice 8
txt_8 = "Apple"
new_txt = ""

for letter in txt_8:
    new_txt += letter*2

print(new_txt)

# exersice 9
highest = -2 ** 200

while True:
    user_num = int(input("enter number:\n"))

    if user_num > highest:
        highest = user_num

    if user_num == 0:
        break
print(f"the highest number is: {highest}")

# exersice 10

str_for_check = input("enter some str for check:\n")
good_str = True

for letter in str_for_check:
    letter:str

    if not letter.isdigit():
        if not letter.isalpha() or not letter.isascii():
            good_str = False
            break

print (good_str)

# exersice 11
user_num = int(input("enter number:\n")) # 2834
new_number = 0

while user_num:
    copy_for_len = user_num // 10
    multy_ = 1

    while copy_for_len:
        multy_ = multy_ * 10
        copy_for_len = copy_for_len // 10

    sum_for_raise = (user_num % 10) * multy_
    new_number += sum_for_raise
    user_num = user_num // 10

print(new_number)

# exersice 11 with a little halp...

user_num = int(input("enter num:\n")) 
revers_num = 0
while user_num:
    last_n = user_num % 10
    revers_num = (revers_num * 10) + last_n
    user_num //= 10
print(revers_num)