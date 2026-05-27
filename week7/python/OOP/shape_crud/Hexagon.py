from shape import Shape


class Hexagon(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side
    
    @property
    def get_area(self):
        return ((3*3**0.5)/2) * (self.side**2)
    
    @property
    def get_perimeter(self):
        return self.side * 6
    
    def to_dict(self):
        object_dict = {
                       "shape_id": self.id,
                       "shape_type": self.shape_type,
                       "side": self.side
                        }  
        return object_dict 
    
    def __str__(self):
        return f'shape id: {self.id} shape type: {self.shape_type} side: {self.side}'
    