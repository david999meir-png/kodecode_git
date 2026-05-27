class Menu:

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