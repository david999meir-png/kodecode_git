import json
from shape import Shape
from Hexagon import Hexagon
from circle import Circle
from rectangle import Rectangle
from square import Square
from Triangle import Tringle



class ShapeManager:

    def __init__(self):
        self.counter_id = 0
        self.shapes = [Shape]
        self.load_from_json()

    def create_shape(self, data: dict): 
        type_shape = ShapeManager.get_class_type(data)

        if data["shape_id"] == None:
            data["shape_id"] = self.counter_id   
            self.counter_id += 1

        new_object = type_shape.from_dict(data)
        self.shapes.append(new_object)

        return new_object

    def get_all_shapes(self):
        for s in self.shapes:
            print(s)
    
    def update_shape(self, shape_id: int, dic: dict):
        for s in self.shapes:
            if shape_id != s.id:
                continue
            shape_class = type(s)
            data = s.to_dict()
            data.update(dic)

            self.create_shape(data)
            self.shapes.remove(s)
        
        else:
            raise ValueError(f"{shape_id} wasn't found")

            

    
    def delete_shape(self, shape_id):
        for s in self.shapes:
            if not s.id == shape_id:
                continue
            self.shapes.remove(s)
        
        else:
            raise ValueError(f"{shape_id} wasn't found.")
    
    def save_to_json(self):
        all_shapes_dict = []
        for shape in self.shapes:
            get_dict = shape.to_dict()
            all_shapes_dict.append(get_dict)

        with open("shapes.json", "w", encoding="utf-8") as f:
            json.dump(all_shapes_dict, f)        


    def load_from_json(self):

        with open("shapes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for shape in data:
                type_class = ShapeManager.get_class_type(shape)

                new_object = type_class.from_dict(shape)
                self.shapes.append(new_object)

    @staticmethod
    def get_class_type(dic: dict):
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