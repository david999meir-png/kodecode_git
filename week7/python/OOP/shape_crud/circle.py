from shape import Shape


class Circle(Shape):
    pay = 3.14159
    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius
    
    @property
    def get_area(self):
        return self.radius ** 2 * Circle.pay
    
    @property
    def get_perimeter(self):
        return 2 * Circle.pay * self.radius
    
    def to_dict(self):
        object_dict = {
                        "id": self.id,
                       "type": self.shape_type,
                       "radius": self.radius
                        }  
        return object_dict 
    
    @classmethod
    def from_str(cls, txt):
        shape_id, shape_type, radius = txt.split()
        return cls(shape_id, shape_type, radius)
    
    def __str__(self):
        return f'shape id: {self.id} shape type: {self.shape_type} radius: {self.radius}'