"""
Notification interface definition.
Defines the contract that all notification objects must implement.
"""

from abc import ABC, abstractmethod


class INotification(ABC):
    """Abstract base class for all notification types."""
    
    @abstractmethod
    def get_content(self) -> str:
        """
        Get the content of the notification.
        
        Returns:
            str: The notification content
        """
        pass
