"""
Notification service implementation.
Main service class implementing the Singleton pattern for managing notifications.
"""

from typing import List
from ..interfaces.notification_interface import INotification
from ..observers.notification_observable import NotificationObservable


class NotificationService:
    """Singleton service for managing notifications and their delivery."""
    
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern implementation.
        
        Returns:
            NotificationService: The singleton instance
        """
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the notification service if not already initialized."""
        if not NotificationService._initialized:
            self.notifications: List[INotification] = []
            self._observable = NotificationObservable()
            NotificationService._initialized = True

    def send_notification(self, notification: INotification) -> None:
        """
        Send a notification through the system.
        
        Args:
            notification: The notification to send
        """
        self.notifications.append(notification)
        self._observable.set_notification(notification)

    def get_observable(self) -> NotificationObservable:
        """
        Get the observable instance for registering observers.
        
        Returns:
            NotificationObservable: The observable instance
        """
        return self._observable
    
    def get_notification_history(self) -> List[INotification]:
        """
        Get the history of all sent notifications.
        
        Returns:
            List[INotification]: List of all sent notifications
        """
        return self.notifications.copy()
    
    def clear_history(self) -> None:
        """Clear the notification history."""
        self.notifications.clear()
