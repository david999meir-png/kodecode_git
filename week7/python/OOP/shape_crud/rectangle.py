import logging
from shape import Shape


logger = logging.getLogger(__name__)

class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, width, height):
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

    
    @property
    def get_area(self) -> float:
        return self.width * self.height
    
    @property
    def get_perimeter(self) -> float:
        return (self.height*2) + (self.width*2)
    
    def to_dict(self) -> dict:
        object_dict = {
                       "shape_id": self.id,
                       "shape_type": self.shape_type,
                       "width": self.width,
                       "height": self.height
                        }  
        return object_dict 
    
    def __str__(self) -> str:
        return f'shape id: {self.id} shape type: {self.shape_type} width: {self.width} height: {self.height}'