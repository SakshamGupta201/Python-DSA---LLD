"""
Notification engine interface.
Defines the contract for notification delivery engines.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .notification_interface import INotification


class INotificationEngine(ABC):
    """Abstract base class for notification engines that handle delivery."""
    
    @abstractmethod
    def update(self, notification: "INotification") -> None:
        """
        Observer pattern update method.
        
        Args:
            notification: The notification to process
        """
        pass
    
    @abstractmethod
    def send_notification(self, notification: "INotification") -> None:
        """
        Send the notification using this engine's delivery method.
        
        Args:
            notification: The notification to send
        """
        pass
