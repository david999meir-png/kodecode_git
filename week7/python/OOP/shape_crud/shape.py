from abc import ABC, abstractmethod
import logging_setup

logger = logging_setup.set_logger(__name__)

class Shape(ABC):
    def __init__(self, shape_id, shape_type):
        self.id = shape_id
        self.shape_type = shape_type
        logger.debug("object %s created, id %s", self.shape_type, self.id)

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
