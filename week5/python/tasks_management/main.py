from tuliis import  show_all_tasks, count_by_criteria, get_user_choice, show_menu,show_daily_report


mission_list = [
    {"mission_name": "go to the bank", "urgency": "high", "done": False},
    {"mission_name": "buy groceries", "urgency": "medium", "done": True},
    {"mission_name": "finish Python homework", "urgency": "high", "done": False},
    {"mission_name": "call mom", "urgency": "low", "done": True},
    {"mission_name": "clean the room", "urgency": "medium", "done": False},
    {"mission_name": "schedule dentist appointment", "urgency": "low", "done": False}
]

if __name__ == "__main__":
    while True:
        show_menu()
        current_choice = get_user_choice()
        if current_choice == "1": show_all_tasks(mission_list)
        elif current_choice == "2": print(count_by_criteria(mission_list, urgency="high"))
        elif current_choice == "3": print(count_by_criteria(mission_list, done=False))
        elif current_choice == "4": print(count_by_criteria(mission_list, done=True))
        elif current_choice == "5": break

    
show_daily_report(mission_list)