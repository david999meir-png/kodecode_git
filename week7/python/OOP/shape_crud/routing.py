from shape_manager import ShapeManager


class Menu:
    def __init__(self, manager: ShapeManager):
        self.manager = manager
        

    @staticmethod
    def show_main_menu():
        print("===== main menu =====")
        print("Add shape .1")
        print("Show all shapes .2")
        print("Update shape .3")
        print("Delete shape .4")
        print("Exit .5")

    @staticmethod
    def show_shapes_menu():
        print("Shape Menu")
        print("1. Circle")
        print("2. Hexagon")
        print("3. Rectangle")
        print("4. Square")
        print("5. Triangle")
        print("0. Back / Exit")

    @staticmethod
    def get_user_choice():
        user_choice = input("enrer your choice:\n")
        return user_choice
    
    @staticmethod
    def processing_choice(choice: str) -> dict:
        if choice == "1":
            radius = input("enter radius:\n")
            if not Menu.is_valid_num(radius):
                raise ValueError("invalid input, please enter numnet only.")
            
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "circle",
                        "radius": radius
                          }
            
        elif choice == "2":
            side = input("enter side:\n")
            if not Menu.is_valid_num(side):
                raise ValueError("invalid input, please enter numnet only.")
            
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "hexagon",
                        "side": side
                          }
            
        elif choice == "3":
            width = input("enter width:\n")
            if not Menu.is_valid_num(width):
                raise ValueError("invalid input, please enter numnet only.")
            
            height = input("enter haight:\n")
            if not Menu.is_valid_num(height):
                raise ValueError("invalid input, please enter numnet only.")
            
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "rectangle",
                        "width": width,
                        "height": height
                          }

        elif choice == "4":
            side = input("enter side:\n")
            if not Menu.is_valid_num(side):
                raise ValueError("invalid input, please enter numnet only.")
            
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "square",
                        "side": side
                          }
            
        elif choice == "5":
            side = input("enter side:\n")
            if not Menu.is_valid_num(side):
                raise ValueError("invalid input, please enter numnet only.")
            
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "triangle",
                        "side": side
                          }
        
        else:
            raise ValueError("wrong choice, please folow the menu.")
        return shape_dict

    @staticmethod
    def is_valid_num(n: str):
        try:
            n = float(n)
            return True
        except ValueError:
            return False

    def flow_menu(self):
        Menu.show_main_menu()
        choice = Menu.get_user_choice()

        if choice == "1":
            Menu.show_shapes_menu()
            inner_choice = Menu.get_user_choice()

            shape = Menu.processing_choice(inner_choice)
            self.manager.create_shape(shape)
        
        elif choice == "2":
            self.manager.get_all_shapes()
        
        elif choice == "3":
            shape_id = input("enter shape id:\n")

            Menu.show_shapes_menu()
            inner_choice = Menu.get_user_choice()
            
            shape_for_update = Menu.processing_choice(inner_choice)
            shape_for_update["shape_id"] = shape_id
            self.manager.update_shape(shape_for_update)
        
        elif choice == "4":
            shape_id = input("enter shape id:\n")
            self.manager.delete_shape(shape_id)
        
        elif choice == "5":
            return "break"
        
        else:
            raise ValueError("wrong choice, please folow the menu.")
            
