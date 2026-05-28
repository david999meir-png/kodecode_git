from abc import ABC, abstractmethod
import logging_setup

logger = logging_setup.set_logger(__name__)

class Shape(ABC):
    def __init__(self, shape_id, shape_type):
        self.id = shape_id
        self.shape_type = shape_type
        logger.debug("object %s created, id %s", self.shape_type, self.id)

    @property
    def get_area(self) -> float:
        """Calculates and returns the area of the shape."""

        pass

    @property
    def get_perimeter(self) -> float:
        """Calculates and returns the perimeter of the shape."""

        pass

    @abstractmethod
    def to_dict(self) -> None:
        """Converts the shape object into a dictionary format."""

        pass
    
    @classmethod
    def from_dict(cls, data: dict) -> "Shape":
        """Creates a new shape object from a given dictionary."""

        logger.debug("create a new object of %s", cls)
        return cls(**data)
    
    @abstractmethod
    def __str__(self) -> str:
        pass


