from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, width, height):
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

    
    @property
    def get_area(self):
        return self.width * self.height
    
    @property
    def get_perimeter(self):
        return (self.height*2) + (self.width*2)
    
    def to_dict(self):
        object_dict = {
                        "id": self.id,
                       "type": self.shape_type,
                       "width": self.width,
                       "hight": self.height
                        }  
        return object_dict 

    @classmethod
    def from_str(cls, txt):
        shape_id, shape_type, w, h = txt.split()
        return cls(shape_id, shape_type, w, h)
    
    def __str__(self):
        return f'shape id: {self.id} shape type: {self.shape_type} width: {self.width} height: {self.height}'