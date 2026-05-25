from utils import get_tasks_as_a_list, save_backup, find_line_by_id, write_to_file


def add_task(filename:str , description: str) -> None:
    """add new tasks to the file from a dictionary"""
    
    with open(filename, "a", encoding='utf-8') as file:
        data = get_tasks_as_a_list(filename)
        id, *_ = tuple(data[-1].split("|"))
        
        file.write(f'{int(id) + 1} | pending | {description}')
        save_backup(filename)
        print(f'task {description} added.')


def complete_task(filename: str, task_id: str) -> None:
    """arg: filename - txt file. task_id - int or str.
      the func changes the status of the task id"""
    
    all_line = get_tasks_as_a_list(filename)
    task_line = find_line_by_id(filename, task_id)

    all_line[task_line] = all_line[task_line].replace("pending", "DONE")

    write_to_file(filename ,all_line)
    save_backup(filename)
    print(f'task {task_id} updated.')


def list_tasks(filename: str) -> None:
    """print in a good view all the tasks"""

    with open(filename, "r", encoding='utf-8') as f:
        for task in f:
            task_id, status, desc = tuple(task.split("|"))
            status = [] if status.strip() == "pending" else ["✓"]
            print(f'{task_id.strip()} | {desc.strip()} | {status}')


def remove_task(filename: str, task_id) -> None:
    """remove the task from the file by id"""

    line_for_remove = find_line_by_id(filename, task_id)
    all_lines = get_tasks_as_a_list(filename)

    del all_lines[line_for_remove]

    write_to_file(filename ,all_lines)
    save_backup(filename)


def filter_by_status(filename: str, status: str) -> list:
    """filter the all tasks with the desired status"""

    all_line = get_tasks_as_a_list(filename)
    return [task for task in all_line if status in task]


def search_task(filename: str, txt: str) -> list:
    """this is a free search in the tasks"""

    all_line = get_tasks_as_a_list(filename)
    return [task for task in all_line if txt in task]


def satistic(filename: str) -> str:
    """return all the DONE func"""
    
    all_line = get_tasks_as_a_list(filename)
    done_tasks = 0

    for task in all_line:
        if "DONE" in task:
            done_tasks += 1
    return f'tasks completed: ({done_tasks}/{len(all_line)})'