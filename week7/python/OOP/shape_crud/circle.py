import logging
from shape import Shape


logger = logging.getLogger(__name__)

class Circle(Shape):
    pay = 3.14159

    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius
    
    @property
    def get_area(self) -> float:
        return self.radius ** 2 * Circle.pay
    
    @property
    def get_perimeter(self) -> float:
        return 2 * Circle.pay * self.radius
    
    def to_dict(self) -> dict:
        object_dict = {
                       "shape_id": self.id,
                       "shape_type": self.shape_type,
                       "radius": self.radius
                        }  
        logger.debug("object id %s converted to a dict.", self.id)
        return object_dict 
    
    def __str__(self) -> str:
        return f'shape id: {self.id} shape type: {self.shape_type}\
              radius: {self.radius} area: {self.get_area} perimeter: {self.get_perimeter}'