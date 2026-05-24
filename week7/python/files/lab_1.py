import os


def add_entry(file_name, date, content) -> None:
    if safe_read_diary(file_name):
        print(f"{file_name} doesn't found.")
        return
    
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f'{date}: {content}\n')


def search_diary(filename, keyword) -> list:
    if safe_read_diary(filename):
        print(f"{filename} doesn't found.")
        return
    
    with open(filename, "r", encoding="utf-8") as file:
        return [line for line in file if keyword in line]


def safe_read_diary(filename):
    if os.path.exists(filename):
        return True
    return False
        



with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("24-04-2026: it was a perfect day\n")
    file.write("24-05-2026: it was a long lesson\n")
    file.write("24-05-2026: it was a nice practice\n")
print("the diayr created!")

add_entry("diary.txt", "24-05-2026", "too mach information...")

if safe_read_diary("diary.txt"):
    print(f"diary.txt doesn't found.")
else:
    with open("diary.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)

print(search_diary("diary.txt", "04"))
