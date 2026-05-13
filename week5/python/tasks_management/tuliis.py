def convert_bool_value(status: bool) -> str:
    if status: return "completed"
    return "not completed"


def show_all_tasks(tasks_list: list[dict]) -> None:
    for task in tasks_list:
        status = convert_bool_value(task["done"])
        print(f"name: {task["mission_name"]} | urgency: {task["urgency"]} | status: {status}")
    return
    

def count_by_criteria(tasks_list: list[dict], urgency=None, done=None) -> int:
    """the default of this function return all the tasks, tou can chose filter it by criteria
    urgency: high / medium / low
    done: True / False
    """

    if urgency is None and done is None:
        return len(tasks_list)
    
    elif urgency:
        return len ([task for task in tasks_list if task["urgency"] == urgency])

    elif done:
        return len([task for task in tasks_list if task["done"]])
    
    elif done is False:
        return len([task for task in tasks_list if not task["done"]])


def show_menu() -> None:
    print("welcome to the best tasks management")
    print("-"*20)
    print("1. show all tasks")
    print("2. show amount urgency tasks")
    print("3. show amount open tasks")
    print("4. show amount completed tasks ")
    print("5. exit")


def get_user_choice(max_menu_range=5) -> str:
    menu_range = [str(n) for n in range(1, max_menu_range+1)]
    while True:
        choice_ = input("enter your choice:\n")
        if choice_ in menu_range: return choice_
        print(f"please enter number lower than {max_menu_range}")


def show_daily_report(tasks_list: list[dict]) -> None:
    show_all_tasks(tasks_list)
    print("-"*20)
    print(f"urgency tasks: {count_by_criteria(tasks_list, urgency="high")}")
    print(f"open tasks: {count_by_criteria(tasks_list, done=False)}")
    print(f"completed tasks: {count_by_criteria(tasks_list, done=True)}")



     
        