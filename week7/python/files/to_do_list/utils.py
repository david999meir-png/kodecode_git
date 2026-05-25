import os


def get_tasks_as_a_list(filename: str) -> list:
    """enter a filename and get a list with all the lines"""

    with open(filename, "r", encoding='utf-8') as f:
        tasks_list = f.readlines()
        return tasks_list


def save_backup(filename: str) -> None:
    """enter a filename and create a new file as a backup"""
    
    all_line = get_tasks_as_a_list(filename)

    with open("backup_task.txt", "w", encoding='utf-8') as backup_file:
        backup_file.writelines(all_line)

def print_list(l: list) -> None:
    for i in l:
        print(i)

        
def write_to_file(filename: str, lines: list) -> bool:
    """the func gets a list of lines and write them into the file
    if the file doesn't exist return false"""

    if not os.path.exists(filename):
        return False
    
    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(lines)
        return True


def load_tasks(filename: str) -> list:
    """take a txt file and return a list with tasks as a dictionaries"""
    
    tasks = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            id, status, desc = tuple(line.split("|"))
            tasks.append({"id": id,
                          "status": status,
                          "desc": desc
                          })
        return tasks


def save_tasks(filename: str, tasks: list) -> None:
    """the func gett a list with dictionaries, and save the tasks on the file"""
    
    with open(filename, "w", encoding='utf-8') as file:
        lines_for_write = []
        for task in tasks:
            lines_for_write.append(f'{task["id"]} | {task["status"]} | {task["desc"]}\n')
        
        file.writelines(lines_for_write)
        save_backup(filename)


def find_line_by_id(filename: str, task_id: str) -> int | None:
    """looking up for task index"""

    all_line = get_tasks_as_a_list(filename)
    for i, line in enumerate(all_line):
        if line.strip().startswith(task_id):
            return i
    