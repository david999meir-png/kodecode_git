import logging
from shape import Shape

logger = logging.getLogger(__name__)


class Tringle(Shape):
    def __init__(self, shape_id, shape_type, side_1, side_2, side_3):
        super().__init__(shape_id, shape_type)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    @property
    def get_area(self) -> float:
        s = self.get_perimeter / 2
        return (s * (s-self.side_1) * (s-self.side_2) * (s-self.side_3)) ** 0.5

    @property
    def get_perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3

    def to_dict(self) -> dict:
        object_dict = {
            "shape_id": self.id,
            "shape_type": self.shape_type,
            "side_1": self.side_1,
            "side_2": self.side_2,
            "side_3": self.side_3,
        }
        logger.debug("object id %s converted to a dict.", self.id)
        return object_dict

    def __str__(self) -> str:
        return f"shape id: {self.id} shape type: {self.shape_type} side 1: {self.side_1} side 2:\
              {self.side_2} side 3: {self.side_3} area: {round(self.get_area, 3)} perimeter: {self.get_perimeter}"
