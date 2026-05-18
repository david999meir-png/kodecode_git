# exersice 1

def sum_dict(d: dict) -> int:
    sum_d = 0
    for i in d.values():
        sum_d += i
    
    return sum_d

assert (sum_dict({"a": 4, "d": 6})) == 10



# exersice 2

def max_dict_val(d: dict) -> int:
    max_key = None
    max_val = -20**20
    for k, v in d.items(): 
        if v > max_val:
            max_val = v
            max_key = k
    return max_key

assert (max_dict_val({"a": 3, "b": 7, "c": 5})) == "b"



# exersice 3

def Count_characters(word: str) -> dict:
    dict_letters = {}
    for letter in list(word):
        if letter not in dict_letters:
            dict_letters[letter] = list(word).count(letter)

    return dict_letters

assert (Count_characters(("banana"))) == {"b": 1, "a": 3, "n": 2}



# exersice 4

def swip_keys_to_value(d: dict) -> dict:
    return {v: k for k, v in d.items()}

assert (swip_keys_to_value(({"a": 1, "b": 2, "c": 3} ))) == {1: "a", 2: "b", 3: "c"}



# exersice 5

def marge_dicts(d1: dict, d2:dict) -> dict:
    # return {**d1, **d2} 
    d1.update(d2)
    return d1

assert (marge_dicts({"a": 1, "b": 2}, {"b": 20, "c": 30})) == {"a": 1, "b": 20, "c": 30}



# exersice 6

def filter_dict(d: dict, threshold: int) -> dict:
     return {k: v for k, v in d.items() if v > threshold}

assert (filter_dict({"a": 1, "b": 5, "c": 3, "d": 8}, 3)) == {"b": 5, "d": 8}



# exersice 7

def gruop_by_first_letter(words: list) -> dict:
    dict_leeters = {}
    for word in words:
        k = word[0]
        dict_leeters.setdefault(k, []).append(word)

    return dict_leeters

assert (gruop_by_first_letter(["apple", "ant", "banana", "berry", "cherry"])) \
== {"a": ["apple", "ant"], "b": ["banana", "berry"], "c": ["cherry"]}
        


# exercise 8

def count_words(txt: str) -> dict:
    words = txt.split()
    return {w: words.count(w) for w in set(words)}

assert (count_words("the cat sat on the mat")) == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}



# exercise 9

def duble_keys(d1: dict, d2: dict) -> list:
    return [k for k in d1 if k in  d2]

assert (duble_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7})) == ["b", "c"]



# exercise 10

def most_frequent_value(d: dict) -> int:
    value = list(d.values())
    max_v = [0]
    for i in value:
        c = value.count(i)
        if c > max_v[0]:
            max_v[0] = i
        elif c == max_v:
            max_v.append(i)

    
    return tuple(max_v) if len(max_v) > 1 else max_v[0]

assert (most_frequent_value({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1})) == 1
