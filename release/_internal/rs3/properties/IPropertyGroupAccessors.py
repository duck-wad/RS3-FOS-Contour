from abc import ABC, abstractmethod

class IPropertyGroupAccessors(ABC):
    @abstractmethod
    def getProperties(self):
        """Retrieve properties as a dictionary."""
        pass

    @abstractmethod
    def setProperties(self, **kwargs):
        """Set properties using keyword arguments."""
        pass