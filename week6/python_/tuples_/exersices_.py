# exersice 1

def sum_tuple(t: tuple) -> int:
    sum_ = 0
    for n in t:
        sum_ += n
    
    return sum_

assert (sum_tuple((1, 2, 10))) == 13



# exersice 2

def max_tuple(t: tuple) -> int:
    max_value = -2**80

    for i in t:
        if i > max_value:
            max_value = i
    return max_value

assert (max_tuple((1, 2, 10))) == 10


# exercise 3

def count_tuple(t: tuple, v) -> int:
    counter_ = 0
    for i in t:
        if i == v:
            counter_ += 1
    return counter_

assert (count_tuple((1, 2, 1, 1, ), 1)) == 3



# exersice 4

def reversed_tuple(t: tuple) -> tuple:
    return tuple(sorted(t, reverse=True))

assert (reversed_tuple((1,2,3,4))) == (4, 3, 2, 1 )



# exersice 5

def swip_pairs(t: tuple) -> tuple:
    new_list = []
    for i in range(len(t) - 1):
        if i % 2 != 0:
            continue
        a, b = t[i+1], t[i]
        new_list.append(a)
        new_list.append(b)


    return tuple(new_list)

assert (swip_pairs((1, 2, 3, 4, 5, 6))) == (2, 1, 4, 3, 6, 5)



# exersice 6

def min_max(t: tuple) -> tuple:
    t = sorted(t)
    min_, *_, max_ = t
    return min_, max_

assert (min_max((9, 52, 1, 5, 54, 2))) == (1, 54)



# exersice 7

def distance_t(a: tuple, b: tuple) -> int:
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]

    return (delta_x ** 2 + delta_y ** 2) ** 0.5


assert (distance_t((0, 0), (3, 4))) == 5.0



# exersice 8

def marge_and_sort(t1: tuple, t2: tuple) -> tuple:
    return tuple(sorted(t1 + t2))

assert (marge_and_sort((3, 1, 4), (1, 5, 9))) == (1, 1, 3, 4, 5, 9)



# exersice 9


def count_items(items: tuple) -> tuple:
     temp_ = [(x, items.count(x)) for x in sorted(set(items), key=lambda x: items.index(x))]

     return tuple(temp_)

assert (count_items(("a", "b", "a", "c", "b", "a"))) == (("a", 3), ("b", 2), ("c", 1))



# exersice 10

def rutine_t(t: tuple, k: int) -> tuple:
    list_t = list(t)
    for _ in range(k):
        list_t.insert(0, list_t.pop())

    return tuple(list_t)
    
assert (rutine_t( (1, 2, 3, 4, 5), k = 2)) == (4, 5, 1, 2, 3)
