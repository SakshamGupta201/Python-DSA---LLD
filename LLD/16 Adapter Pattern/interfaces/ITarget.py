from abc import ABC, abstractmethod

class ITarget(ABC):
    """Abstract base class for the target interface in the Adapter Pattern."""
    
    @abstractmethod
    def get_json_data(self) -> str:
        """
        Get the data in JSON format.
        
        Returns:
            str: The data in JSON format
        """
        pass