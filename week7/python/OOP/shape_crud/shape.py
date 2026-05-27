from abc import ABC, abstractmethod
import logging_setup

logger = logging_setup.set_logger(__name__)

class Shape(ABC):
    def __init__(self, shape_id, shape_type):
        self.id = shape_id
        self.shape_type = shape_type
        logger.debug("object %s created, id %s", self.shape_type, self.id)

    @property
    def get_area(self):
        pass

    @property
    def get_perimeter(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    
    @abstractmethod
    def __str__(self):
        pass


