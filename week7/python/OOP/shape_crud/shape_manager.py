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
        pass
    
    def update_shape(self, shape_id, new_data):
        pass
    
    def delete_shape(self, shape_id):
        pass
    
    def save_to_json(self):
        pass

    def load_from_json(self):
        pass
