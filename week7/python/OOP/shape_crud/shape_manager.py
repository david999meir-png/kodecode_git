import json
import logging
from shape import Shape
from hexagon import Hexagon
from circle import Circle
from rectangle import Rectangle
from square import Square
from Triangle import Tringle


logger = logging.getLogger(__name__)

class ShapeManager:
    def __init__(self):
        self.counter_id = 1
        self.shapes = []
        self.load_from_json()

    def create_shape(self, data: dict) -> Shape:
        """Creates a new shape object and adds it to the system."""

        type_shape = ShapeManager.get_class_type(data)

        if data["shape_id"] == None:
            data["shape_id"] = self.counter_id   
            self.counter_id += 1
            logger.info("a new shape %s created ID %s ", type_shape, self.counter_id - 1)


        new_object = type_shape.from_dict(data)
        self.shapes.append(new_object)
        self.save_to_json()

        return new_object

    def get_all_shapes(self) -> None:
        """Prints the details of all currently saved shapes."""

        for s in self.shapes:
            print(s)
        logger.debug("all the shapes showed")
    
    def update_shape(self, shape_id: int, dic: dict) -> None:
            """Updates an existing shape with new data based on its ID."""

            shape_for_update = self.search_shape_by_id(shape_id)
            if shape_for_update is None:
                raise ValueError(f"{shape_id} wasn't found")

            self.shapes.remove(shape_for_update)
            self.create_shape(dic)

            logger.info("shape id %s updated", shape_id)

    def search_shape_by_id(self, shape_id) -> None | Shape:
        """Searches and returns a shape object by its ID, or None if not found."""

        for shape in self.shapes:
            if shape.id != int(shape_id):
                continue
            logger.debug("shape %s found", shape.shape_type)
            return shape
        return None
    
    def delete_shape(self, shape_id) -> None:
            """Removes a shape from the system using its ID."""

            shape_for_remove = self.search_shape_by_id(shape_id)

            if shape_for_remove is None:
                raise ValueError(f"{shape_id} wasn't found.")
            
            self.shapes.remove(shape_for_remove)
            self.save_to_json()

            logger.warning("shape id: %s DELETED !", shape_id)
            
    def save_to_json(self) -> None:
        """Saves all current shapes from the system into a JSON file."""

        all_shapes_dict = []
        for shape in self.shapes:
            get_dict = shape.to_dict()
            all_shapes_dict.append(get_dict)

        with open("shapes.json", "w", encoding="utf-8") as f:
            json.dump(all_shapes_dict, f)  
            logger.info("shapes saved to json file")      

    def load_from_json(self) -> None:
        """Loads historical shapes from the JSON file into the system."""

        try:
            with open("shapes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    self.counter_id = self.get_max_id(data) + 1


                    for shape in data:
                        type_class = self.get_class_type(shape)

                        new_object = type_class.from_dict(shape)
                        self.shapes.append(new_object)
                    logger.info("shapes loaded from json")

        except FileNotFoundError as e:
            logger.warning("srart run with empty dada")
        
        except json.JSONDecodeError:
            logger.error("there is a problem with a json file")

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

        logger.debug("extract class type %s", type_class)
        return type_class
    
    def get_max_id(self, json_dict) -> int:
        max_id = 0

        for shape in json_dict:
            current_id = shape.get("shape_id", 0)
            if current_id > max_id:
                max_id = current_id
        logger.debug("calulate the max id %s", max_id)
        return max_id
    