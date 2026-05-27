from shape_manager import ShapeManager


class Menu:
    def __init__(self, manager):
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
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "circle",
                        "radius": radius
                          }
            
        elif choice == "2":
            side = input("enter side:\n")
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "hexagon",
                        "side": side
                          }
            
        elif choice == "3":
            width = input("enter width:\n")
            height = input("enter haight:\n")
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "rectangle",
                        "width": width,
                        "height": height
                          }

        elif choice == "4":
            side = input("enter side:\n")
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "square",
                        "side": side
                          }
            
        elif choice == "5":
            side = input("enter side:\n")
            shape_dict = {
                        "shape_id": None,
                        "shape_type": "triangle",
                        "side": side
                          }
        
        else:
            raise ValueError("wrong choice, please folow the menu.")
        return shape_dict

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
        
        elif choice == "4":
            shape_id = input("enter shape id:\n")
            self.manager.delete_shape(shape_id)
        
        elif choice == "5":
            return "break"
        
        else:
            raise ValueError("wrong choice, please folow the menu.")
            
