import logging
from shape import Shape


logger = logging.getLogger(__name__)

class Tringle(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side
    
    @property
    def get_area(self) -> float:
        return (3**0.5/4) * (self.side**2)
    
    @property
    def get_perimeter(self) -> float:
        return self.side * 3
    
    def to_dict(self) -> dict:
        object_dict = {
                        "shape_id": self.id,
                       "shape_type": self.shape_type,
                       "side": self.side
                        }  
        return object_dict 
    
    def __str__(self) -> str:
        return f'shape id: {self.id} shape type: {self.shape_type} side: {self.side}'