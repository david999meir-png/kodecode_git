# exercise 1

def remove_daplicates(l: list) -> list:
    return list(set(l))

assert (remove_daplicates([1, 2, 2, 3, 1, 4, 3])) == [1, 2, 3, 4]
 


# exercise 2

def len_set(l: list) -> int:
    new_list = []
    for i in l:
        if i in new_list:
            new_list.append(i)

    return len((new_list))



# exercise 3

def daplicates(l1: list, l2: list) -> list:
    return list(set(set(l1) & set(l2)))

assert (daplicates([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4]



# exercise 4

def elements_in_only_on(l1: list, l2: list) -> list:
    return list(set(set(l1) ^ set(l2)))

assert (elements_in_only_on([1, 2, 3, 4], [3, 4, 5, 6])) == [1, 2, 5, 6]



# exercise 5

def is_subset(l1: list, l2: list) -> bool:
    remaind = set(l1) - set(l2)
    return not bool(remaind)

assert (is_subset([1, 2, 3], [1, 2, 3, 4, 5])) == True
assert (is_subset([1, 2, 6], [1, 2, 3, 4, 5])) == False



# exercise 6

def sort_characters(txt: str) -> bool:
    return list(txt) == sorted(list((txt)))

assert (sort_characters(("abcdefg"))) == True
assert (sort_characters(("abcdefdzg"))) == False



# exercise 7

def first_double(l: list) -> int | None:
    if len(l) == len(set(l)):
        return
    num_seem = set()
    for x in l:
        if x in num_seem:
            return x
        num_seem.add(x)
   
assert (first_double([1, 2, 3, 2, 4, 1])) == 2
assert (first_double([1, 2, 3, 4])) == None



# exersice 8

def diff_words(txt: str) -> int:
    return len(set(x.lower() for x in txt.split()))

assert (diff_words("The cat and the dog and the bird")) == 5



# exersice 9

def sum_pairs(l: list, target: int) -> bool:
    set_pairs = set()
    for n in l:
        search_num = target - n
        if search_num in set_pairs:
            return True
        set_pairs.add(n)
    return False

assert (sum_pairs([3, 1, 4, 7, 2], 6)) == True
assert (sum_pairs([3, 1, 4, 7, 2], 100)) == False



# exersice 10

def xor_lists(l1: list, l2: list) -> list:
    one_set = set(sorted(l1 + l2))
    xor_list = []
    for i in one_set:
        if i not in l1:
            xor_list.append(i)
        elif i not in l2:
            xor_list.append(i)

    return xor_list

assert (xor_lists([1, 2, 3, 4], [3, 4, 5, 6])) == [1, 2, 5, 6]
print (xor_lists([1, 2, 3, 4], [3, 4, 5, 6])) 
