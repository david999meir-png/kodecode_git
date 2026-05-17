list_1 = [x for x in range(6)]

# exersice 1

def sum_lst(list_: list) -> int:
    sum_lst = 0

    for i in list_1:
        sum_lst += i

    return sum_lst

assert (sum_lst(list_1)) == 15

# exersice 2

def high_value(list_: list) -> int:
    high_num = 0
    for n in list_:
        if n > high_num:
            high_num = n
    
    return high_num

assert (high_value(list_1)) == 5



# exersice 3
def count_value(list_, value: str) -> int:
    sum_value = 0
    for i in list_:
        if i == value:
            sum_value += 1

    return sum_value


assert (count_value(["ba", "na", "na"], "ba")) == 1
assert (count_value(["ba", "na", "na"], "na")) == 2



# exersice 4

def reverse_list(list_: list) -> list:
    new_list = []
    for i in range(len(list_)):
        current_index = len(list_) -1 -i
        new_list.append(list_[current_index])
    return new_list

assert (reverse_list([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]



# exersice 5

def remove_doplicates(list_: list) -> list:
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


assert (remove_doplicates([9, 8, 9, 7, 5, 6, 9, 8, 6])) == [9, 8, 7, 5, 6]



# exersice 6

def second_largest(list_: list) -> int:
    max_n = high_value(list_)
    second_num = 0

    for i in list_:
        if i > second_num and i < max_n:
            second_num = i

    return second_num if second_num else None


assert (second_largest([10, 10, 10])) == None
assert (second_largest([10, 9, 8])) == 9



# exersice 7

def marge_sorted_lists(list_1: list, list_2: list) -> list:
    new_sorted_list = []
    new_sorted_list.extend(list_1)
    new_sorted_list.extend(list_2)
    new_sorted_list.sort()

    return new_sorted_list


assert (marge_sorted_lists([1, 3, 5], [2, 4, 6])) == [1, 2, 3, 4, 5, 6]



# exersice 8

def rutine_list(list_: list, k: int) -> list:
    for _ in range(k+1):
        list_.append(list_.pop(0))

    return list_

assert (rutine_list([1, 2, 3, 4, 5], k = 2))  == [4, 5, 1, 2, 3]


