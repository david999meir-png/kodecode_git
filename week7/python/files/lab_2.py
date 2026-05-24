def create_grades_file(filename):
    students = [
    ("Dan", [85, 90, 78]),
    ("MOMO", [92, 88, 95]),
    ("Yoni", [70, 65, 80]),
    ("Avi", [100, 95, 98]),
    ("Sara", [60, 72, 68]),
    ]
    with open("grades.txt", "w", encoding="utf-8") as file:
        for name in students:
            grades = ",".join([str(grade) for grade in name[1]])
            write_line = f'{name[0]}, {grades}\n'
            file.write(write_line)


def calculate_averages(filename):
    average = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data = line.split(",")
            name, *grades = tuple(data)
            grades = [int(grade) for grade in grades]

            if not grades:
                average[name] = 0
                continue

            for g in grades:
                if not g.strip():
                    print(f'grade missing at {name}')

            final_average = round(sum(grades) / len(grades), 1)
            average[name] = final_average

        return average

            
def save_results(averages, output_filename):
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write("=== Student Results ===\n")
        list_w = [f'{k}: {float(v)}\n' for k,v in averages.items()]
        sort_list = sorted(list_w, key=lambda x: float(x.split()[1]), reverse=True)

        for i, _ in enumerate(sort_list):
            sort_list[i] = str(i+1) + ". " + sort_list[i]
            
        file.writelines(sort_list)


def add_statistics_to_file(dict_grades: dict, file_name: str):
    with open(file_name, "a", encoding="utf-8") as file:
        lines_for_write = ["=== Statistics ===\n"]
        class_average = 0
        highest = 0
        highest_name = None
        lowest = 100
        lowest_name = None
        passing = 0

        for name, grade in dict_grades.items():
            class_average += grade

            if grade > highest: 
                highest = grade
                highest_name = name
            
            if grade < lowest:
                lowest = grade
                lowest_name = name

            if grade >= 60:
                passing += 1

        lines_for_write.append(f'Class average: {round(class_average / len(dict_grades), 1)}\n')
        lines_for_write.append(f'Highest: {highest_name} ({highest})\n')
        lines_for_write.append(f'Lowest: {lowest_name} ({lowest})\n')
        lines_for_write.append(f'Passing (>=60): {passing}/{len(dict_grades)}')
        file.writelines(lines_for_write)


create_grades_file("grades.txt")
result_1 = calculate_averages("grades.txt")
save_results(result_1, "result.txt")
add_statistics_to_file(result_1 ,"result.txt")
