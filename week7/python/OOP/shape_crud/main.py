from shape_manager import ShapeManager
from routing import Menu
from logging_setup import set_logger

shape_managet_muster = ShapeManager()
menu_manager = Menu(shape_managet_muster)

def main():
    set_logger()
    
    while True:
        result = menu_manager.flow_menu()
        if result == "break":
            break


if __name__ == "__main__":
    main()