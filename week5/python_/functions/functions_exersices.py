# exersice 1
def is_even(n: int) -> bool:
    """return a boolian value, True if it even and false otherwise"""

    if n % 2 == 0:
        return True
    return False

print(is_even(5))
print(is_even(5))


# exersic 2
def factorial(n) -> int:
    """return factorial of n"""

    factorial_sum = 1
    for i in range(n):
        factorial_sum *= (i + 1)
    return factorial_sum

print(factorial(5))
print(factorial(0))


# exersic 3
def count_vowels(s: str) -> int:
    """return how many vowels in the txt"""

    vowels_list = ["a", "e", "i", "O", "u"]
    sum_vowels = 0 
    for letter in s:
        if letter.lower() in vowels_list:
            sum_vowels += 1
    return sum_vowels

print(count_vowels("david meir"))


# exersice 4
def reverse_string(s) -> str:
    """return a new str reversed"""

    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s) - 1 - i]
    return new_str

print(reverse_string("david"))


# exersice 5
def find_max(l: list) -> int:
    """return the max value in the list without using max function"""

    max_value = -2 ** 200
    print(max_value)
    for num in l:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([1, 5, 80, 84848]))


# exercise 6
def celsius_to_fahrenheit(c:float) -> float:
   return 9 / 5 * c + 32

print(celsius_to_fahrenheit(25))


# exercise 7
def  is_palindrome(s:str) -> bool: #asdsa
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -1 -i]:
            return False
    return True

print(is_palindrome("ילד כותב בתוכ דלי"))


# exercise 8
def only_even_nums(l: list) -> list:
    return [n for n in l if n % 2 == 0]

print(only_even_nums([x for x in range (10)]))


# exercise 9
def anagrams_str(s1:str, s2:str) -> bool:
    return sorted(s1) == sorted(s2)

print(anagrams_str("adzs", "asdz"))
print(anagrams_str("adsk", "asdz"))


# exercise 10
def count_words(s:str) -> dict:
    count_dict = {}
    count_list = s.split()
    for i in count_list:
        if i not in count_dict.keys():
            count_dict[i] = count_list.count(i)
    return count_dict

print(count_words("this this this will be will amazing"))

# exercise 11
def calculate_resource_drain(cost:int, waste_factor:float) -> float:
    return cost * (waste_factor / 100)

def get_net_resources(cost:int, waste_factor:float) -> float:
    west_ = calculate_resource_drain(cost, waste_factor)
    return cost - west_

print(get_net_resources(100, 10))


# exercise 12
def intercept_length(packet:str) -> int:
    return len(packet)

def verify_transmission(packet:str) -> str:
    lengh_ = intercept_length(packet)
    return f"Intercepted packet contains {lengh_} bytes of data"

print(verify_transmission("01100110101010111111111110010110"))


# exercise 13
def convert_to_decibels(signal_strength) -> float:
    import math

    return 20 * math.log10(signal_strength / 1)

def is_threat_detected(signal_strength) -> bool:
    corrent = convert_to_decibels(signal_strength)
    return corrent > 90

print(is_threat_detected(41000))
print(is_threat_detected(800))


# exercise 14
def get_fuel_surcharge(distance:float) -> float:
    amount_of_liters = distance / 10
    fuel_cost = 8 * amount_of_liters
    return fuel_cost * 0.17

def get_hazard_pay(distance:float) -> float:
    amount_of_liters = distance / 10
    fuel_cost = 8 * amount_of_liters
    return fuel_cost * 0.05

def calculate_mission_cost(distance:float) -> float:
    fuel_surcharge = get_fuel_surcharge(distance)
    hazard_pay = get_hazard_pay(distance)
    fuel_cost = distance / 10 * 8
    return fuel_surcharge + hazard_pay + fuel_cost

print(calculate_mission_cost(100))

    



