from shape_manager import ShapeManager


class Menu:
    def __init__(self, manager: ShapeManager):
        self.manager = manager

    @staticmethod
    def show_main_menu() -> None:
        print("===== main menu =====")
        print("Add shape .1")
        print("Show all shapes .2")
        print("Update shape .3")
        print("Delete shape .4")
        print("get shape area .5")
        print("get shape primetter .6")
        print("Exit .0")

    @staticmethod
    def show_shapes_menu() -> None:
        print("Shape Menu")
        print("1. Circle")
        print("2. Hexagon")
        print("3. Rectangle")
        print("4. Square")
        print("5. Triangle")
        print("0. Back / Exit")

    @staticmethod
    def get_user_choice() -> str:
        user_choice = input("enrer your choice:\n")
        return user_choice

    @staticmethod
    def processing_choice(choice: str) -> dict:
        if choice == "1":
            radius = input("enter radius:\n")
            if not Menu.is_valid_num(radius):
                raise ValueError("invalid input, please enter positive numner only.")

            shape_dict = {
                "shape_id": None,
                "shape_type": "circle",
                "radius": float(radius),
            }

        elif choice == "2":
            side = input("enter side:\n")
            if not Menu.is_valid_num(side):
                raise ValueError("invalid input, please enter positive numner only.")

            shape_dict = {
                "shape_id": None,
                "shape_type": "hexagon",
                "side": float(side),
            }

        elif choice == "3":
            width = input("enter width:\n")
            if not Menu.is_valid_num(width):
                raise ValueError("invalid input, please enter positive numner only.")

            height = input("enter haight:\n")
            if not Menu.is_valid_num(height):
                raise ValueError("invalid input, please enter positive numner only.")

            shape_dict = {
                "shape_id": None,
                "shape_type": "rectangle",
                "width": float(width),
                "height": float(height),
            }

        elif choice == "4":
            side = input("enter side:\n")
            if not Menu.is_valid_num(side):
                raise ValueError("invalid input, please enter numnet only.")

            shape_dict = {"shape_id": None, "shape_type": "square", "side": float(side)}

        elif choice == "5":
            side_1 = input("enter side_1:\n")
            if not Menu.is_valid_num(side_1):
                raise ValueError("invalid input, please enter positive numner only.")
            
            side_2 = input("enter side_2:\n")
            if not Menu.is_valid_num(side_2):
                raise ValueError("invalid input, please enter positive numner only.")
            
            side_3 = input("enter side_3:\n")
            if not Menu.is_valid_num(side_3):
                raise ValueError("invalid input, please enter positive numner only.")


            shape_dict = {
                "shape_id": None,
                "shape_type": "triangle",
                "side_1": float(side_1),
                "side_2": float(side_2),
                "side_3": float(side_3),
            }

        else:
            raise ValueError("wrong choice, please folow the menu.")
        return shape_dict

    @staticmethod
    def is_valid_num(n: str) -> bool:
        try:
            n = float(n)
            if n > 0:
                return True
            return False
        except ValueError:
            return False

    def flow_menu(self) -> str | None:
        """Starts the main interactive menu loop for the user."""

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
            shape_for_update["shape_id"] = int(shape_id)
            self.manager.update_shape(shape_id, shape_for_update)

        elif choice == "4":
            shape_id = input("enter shape id:\n")
            self.manager.delete_shape(shape_id)

        elif choice == "5":
            shape_id = input("enter shape id:\n")
            shape = self.manager.search_shape_by_id(shape_id)
            if not shape:
                raise ValueError(f"id {shape_id} wasn't found")
            print(shape.get_area)

        elif choice == "6":
            shape_id = input("enter shape id:\n")
            shape = self.manager.search_shape_by_id(shape_id)
            if not shape:
                raise ValueError(f"id {shape_id} wasn't found")
            print(shape.get_perimeter)

        elif choice == "0":
            print("good by...")
            return "break"

        else:
            raise ValueError("wrong choice, please folow the menu.")
