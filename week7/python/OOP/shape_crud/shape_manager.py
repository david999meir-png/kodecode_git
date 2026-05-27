import json
from shape import Shape


class ShapeManager:

    def __init__(self):
        counter_id = 0
        self.shapes = [Shape]
        self.load_from_json()

    def create_shape(self, shape: tuple): 
        shape_id = self.counter_id   
        self.counter_id += 1

        type_class = shape[0]
        txt = shape_id + shape[1]

        new_object = type_class.from_str(txt, shape_id)
        self.shapes.append(new_object)

        return new_object

    def get_all_shapes(self):
        for s in self.shapes:
            print(s)
    
    def update_shape(self, shape_id, new_data):
        pass
    
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
        pass
