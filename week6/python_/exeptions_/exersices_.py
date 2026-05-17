# exersice 1

def safe_int(s: str) -> int | None:
    try:
        return int(s)
    
    except ValueError as e:
        print("you must enter str of num")
        print(e)

    except TypeError as e:
        print("please enter a ligle value only int or str.") #  למה לא מדפיס?
        print(e)

    except Exception as e:
        print(e)
    

assert(safe_int("fg")) == None
assert(safe_int("5")) == 5
assert(safe_int(6.5)) == 6
assert(safe_int([8])) == None



# exersice 2

def safe_divide(a: int, b: int) -> float | str:
    try:
        return a / b
    
    except ZeroDivisionError:
        return "undefined"
    
    except Exception as e:
        print(e)
    
    
assert(safe_divide(10, 2)) == 5
assert(safe_divide(10, 0)) == "undefined"



# exersice 3

def read_first_line(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            return first_line
        
    except FileNotFoundError as e:
        print(e)
    
    except Exception as e:
        print(e)


assert(read_first_line("this_is_error")) == None



# exersice 4

def get_value(d, key):
    try: 
        return d[key]
    except KeyError as e:
        print(e)
        return "missing"
    
    except Exception as e:
        print(e)
    

assert (get_value({1: "a"}, 1)) == "a"
assert (get_value({1: "a"}, 8)) == "missing"



# exersice 5

def parse_ints(values: list) -> list:
    ints_list = []
    for n in values:
        try:
            ints_list.append(int(n))

        except ValueError, TypeError:
            print(f"invalid value: {n} skipped.")
        
        except Exception as e:
            print(e)

    return ints_list


assert (parse_ints(["d", "5", "78", True, {"d"}])) == [5, 78, 1]



# exersice 6

def validate_age(age: int) -> int | None:
    try:
        if 0 > age or  age > 150:
            raise ValueError("age out of range!")
        return age
    
    except ValueError as e:
         print(e)

    except Exception as e:
        print(e)


assert (validate_age(50)) == 50
assert (validate_age(500)) == None



# exersice 7

class InsufficientFundsError(Exception):
    pass

def withdraw(balance: float, amount: float) -> float | None:
    try:
        if amount > balance:
            raise InsufficientFundsError
        return balance - amount
    
    except InsufficientFundsError:
        print(f"please choose amount lees than {balance}")
        raise
    
    except Exception as e:
        print(e)
    

assert (withdraw(400, 300)) == 100
assert (withdraw(100, 100)) == 0



# exersice 8

def func():
    import random

    my_lst = [4, 5, 3, 4]
    my_ind = random.randint(0, 5)
    return my_lst[my_ind]



def retry(func, n):
    for i in range(n):
        try:
            current = func()
            return current

        except Exception as e:
            if i == (n-1):
                raise e

print(retry(func, 10))
    


# exersice 9

def count_errors(funcs: list) -> int:
    errors_ = 0
    for f in funcs:
        try:
            f()
        except Exception as e:
            print(e)
            errors_ += 1
    
    return errors_


assert (count_errors([lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2])) == 2



# exersice 10

def load_config(path: str):
    try:

        with open(path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            try:
                return int(first_line)
            
            except Exception as e:
                raise RuntimeError("failed to load config") from e


    except FileNotFoundError as e:
        raise RuntimeError("failed to load config") from e
        


