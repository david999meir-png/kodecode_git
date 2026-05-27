import json
from shape import Shape
from hexagon import Hexagon
from circle import Circle
from rectangle import Rectangle
from square import Square
from Triangle import Tringle


class ShapeManager:
    def __init__(self):
        self.counter_id = 0
        self.shapes = []
        self.load_from_json()

    def create_shape(self, data: dict) -> Shape:
        """Creates a new shape object and adds it to the system."""

        type_shape = ShapeManager.get_class_type(data)

        if data["shape_id"] == None:
            data["shape_id"] = self.counter_id   
            self.counter_id += 1

        new_object = type_shape.from_dict(data)
        self.shapes.append(new_object)
        self.save_to_json()

        return new_object

    def get_all_shapes(self) -> None:
        """Prints the details of all currently saved shapes."""

        for s in self.shapes:
            print(s)
    
    def update_shape(self, shape_id: int, dic: dict) -> None:
            """Updates an existing shape with new data based on its ID."""

            shape_for_update = self.search_shape_by_id(shape_id)
            if shape_for_update is None:
                raise ValueError(f"{shape_id} wasn't found")

            self.shapes.remove(shape_for_update)
            self.create_shape(dic)

    def search_shape_by_id(self, shape_id) -> None | Shape:
        """Searches and returns a shape object by its ID, or None if not found."""

        for shape in self.shapes:
            if shape.id != int(shape_id):
                continue
            return shape
        return None
    
    def delete_shape(self, shape_id) -> None:
            """Removes a shape from the system using its ID."""

            shape_for_remove = self.search_shape_by_id(shape_id)

            if shape_for_remove is None:
                raise ValueError(f"{shape_id} wasn't found.")
            
            self.shapes.remove(shape_for_remove)
            self.save_to_json()
            
    def save_to_json(self) -> None:
        """Saves all current shapes from the system into a JSON file."""

        all_shapes_dict = []
        for shape in self.shapes:
            get_dict = shape.to_dict()
            all_shapes_dict.append(get_dict)

        with open("shapes.json", "w", encoding="utf-8") as f:
            json.dump(all_shapes_dict, f)        

    def load_from_json(self) -> None:
        """Loads historical shapes from the JSON file into the system."""

        try:
            with open("shapes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.counter_id = self.get_max_id(data) + 1

            for shape in data:
                type_class = self.get_class_type(shape)

                new_object = type_class.from_dict(shape)
                self.shapes.append(new_object)

        except FileExistsError as e:
            raise

    @staticmethod
    def get_class_type(dic: dict) -> Shape:
        shape_map = {
            "circle": Circle,
            "hexagon": Hexagon, 
            "rectangle": Rectangle, 
            "square": Square,
            "triangle": Tringle
            }
        type_shape = dic["shape_type"]
        type_class = shape_map[type_shape]

        return type_class
    
    def get_max_id(self, json_dict) -> int:
        max_id = 0

        for shape in json_dict:
            if not shape["shape_id"] > max_id:
                continue
            max_id = shape.id
        return max_id
    