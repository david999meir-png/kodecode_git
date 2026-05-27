from shape import Shape


class Square(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side
    
    @property
    def get_area(self):
        return self.side ** 2
    
    @property
    def get_perimeter(self):
        return self.side * 4
    
    def to_dict(self):
        object_dict = {
                        "id": self.id,
                       "type": self.shape_type,
                       "side": self.side
                        }  
        return object_dict 
    