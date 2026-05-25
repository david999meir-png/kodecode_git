import os
from tasks_manegment import add_task, list_tasks,\
      complete_task, remove_task, filter_by_status, search_task, satistic
from utils import save_tasks, print_list


def show_menu() -> None:
    print('\n=== To-Do List Manager ===')
    print('1. show all tasks')
    print('2. add task')
    print('3. remove task')
    print('4. mark as completed')
    print('5. filter by status')
    print('6. free search')
    print('7. show satistics')
    print('8. EXIT')


def user_flow_manegment(filename, choice) -> None:
    """menage the user choice and the flow"""

    if choice == "1":
        list_tasks(filename)
        
    elif choice == "2":
        desc = input("add task's description:\n")
        add_task(filename, desc)

    elif choice == "3":
        task_id = input("enter task id:\n")
        remove_task(filename, task_id)
    
    elif choice == "4":
        task_id = input("enter task id:\n")
        complete_task(filename, task_id)

    elif choice == "5":
        status = input("enter status for filtering:\n")
        filtred = filter_by_status(filename, status)
        print_list(filtred)
    
    elif choice == "6":
        txt_for_search = input("enter text for searching:\n")
        searched = search_task(filename, txt_for_search)
        print_list(searched)
    
    elif choice == "7":
        print(satistic(filename))
    
    if choice == "8":
        print('see you...')
        return "break"


def main() -> None:
    FILENAME = "tasks.txt"

    if not os.path.exists(FILENAME):
        raise FileNotFoundError(f"{FILENAME} wasn't found")
    try:
        while True:
            show_menu()
            choice = input("enter your choice:\n")
            result = user_flow_manegment(FILENAME, choice)

            if result == "break":
                break

    except (FileExistsError, FileNotFoundError) as e:
        print(e)
    
    except(ValueError, TypeError, IndexError) as e:
        print(e)


tasks = [
    {"id": 1, "status": "pending", "desc": "Buy groceries"},
    {"id": 2, "status": "DONE", "desc": "Clean the kitchen"},
    {"id": 3, "status": "pending", "desc": "Finish Python homework"},
    {"id": 4, "status": "DONE", "desc": "Call the dentist"},
    {"id": 5, "status": "pending", "desc": "Pay electricity bill"},
    {"id": 6, "status": "pending", "desc": "Read 20 pages of a book"},
    {"id": 7, "status": "DONE", "desc": "Workout for 30 minutes"},
    {"id": 8, "status": "pending", "desc": "Wash the car"},
    {"id": 9, "status": "DONE", "desc": "Backup computer files"},
    {"id": 10, "status": "pending", "desc": "Prepare dinner"}
]

save_tasks("tasks.txt", tasks)

if __name__ == "__main__":
    main()