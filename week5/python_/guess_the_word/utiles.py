import random


words = [
    "apple", "banana", "orange", "grape", "melon", "peach", "pear", "plum",
    "cherry", "mango", "lemon", "lime", "kiwi", "carrot", "potato", "tomato",
    "onion", "garlic", "pepper", "cucumber", "school", "teacher", "student",
    "pencil", "notebook", "eraser", "marker", "window", "door", "table",
    "chair", "computer", "keyboard", "screen", "mouse", "phone", "camera",
    "garden", "flower", "tree", "river", "ocean", "mountain", "forest",
    "desert", "island", "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "donkey", "panda", "guitar", "piano", "drums",
    "violin", "music", "movie", "actor", "family", "mother", "father",
    "brother", "sister", "uncle", "aunt", "cousin", "friend", "travel",
    "airport", "ticket", "hotel", "beach", "winter", "summer", "spring",
    "autumn", "coffee", "tea", "water", "juice", "bread", "butter",
    "cheese", "pizza", "burger", "pasta", "soccer", "tennis", "basketball",
    "running", "swimming", "coding", "python", "robot", "planet", "rocket",
    "castle", "treasure", "dragon", "pirate"
]

def choose_random_word(word_list) -> str:
    random_i = random.randint(1, len(word_list)-1)
    return word_list[random_i]
    

def get_tags_list(word) -> list:
    return ["_" for i in range(len(word))]


def is_win(secret_word: str, tags_list: list[str]) -> bool:
    word_for_check = ""
    for letter in tags_list:
        word_for_check += letter

    if word_for_check.lower() == secret_word.lower():
        return True
    return False


def chack_input_guess(letter) -> bool:
    return letter.isalpha() and letter.isascii() and len(letter) == 1


def get_guess() -> str:
    while True:
        user_guess = input("enrer guess:\n")
        if chack_input_guess(user_guess):
            return user_guess.lower()
        
        print("illigal format. try again in english\n")


def check_guess_in_word(guess, word) -> bool:
    return guess.lower() in word


def get_correct_guess_index(guess, word) -> list:
    index_list = []
    for i, letter in enumerate(word):
        if letter.lower() == guess.lower():
            index_list.append(i)
    return index_list


def update_tags_list(index_list:list, tags_list: list, guess:str) -> list:
    for i in index_list:
        tags_list[i] = guess
    return tags_list


def drawing_lines(tries_left: int) -> str:
    stages = [
            """
    +---+
    |   |
    O   |
    /|\\  |
    / \\  |
        |
    ========
    """,
            """
    +---+
    |   |
    O   |
    /|\\  |
    /    |
        |
    ========
    """,
            """
    +---+
    |   |
    O   |
    /|\\  |
        |
        |
    ========
    """,
            """
    +---+
    |   |
    O   |
    /|   |
        |
        |
    ========
    """,
            """
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========
    """,
            """
    +---+
    |   |
    O   |
        |
        |
        |
    ========
    """,
            """
    +---+
    |   |
        |
        |
        |
        |
    ========
    """
        ]
    print(stages[tries_left])


def main():
    tries_count = 6
    secret_word = choose_random_word(words)
    tag_for_user = get_tags_list(secret_word)
    wrong_guesses_set = set()
    win_ = False

    while tries_count:
        print(tag_for_user)
        print(f"tries: {tries_count}")
        print(f"letter that you guesed: {wrong_guesses_set if wrong_guesses_set else 0}")
        guess = get_guess()
        correct_guess = check_guess_in_word(guess, secret_word)

        
        if not correct_guess:
            tries_count -= 1
            drawing_lines(tries_count)
            wrong_guesses_set.add(guess)
            continue

        index_list = get_correct_guess_index(guess, secret_word)
        tag_for_user = update_tags_list(index_list, tag_for_user, guess)

        if is_win(secret_word, tag_for_user):
            win_ =True
            print("Y O U   W I N   T H E   G A M E ! !")
            break

    if not win_:
        print("G A M E   O V E R ! !")
        print(f"the secret word was {secret_word}")
        print("G O O D   B Y . . .")
