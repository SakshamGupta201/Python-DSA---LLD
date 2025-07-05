"""
Logger observer implementation.
Simple observer that logs notifications to console.
"""

from ..interfaces.observer_interface import IObserver
from ..interfaces.notification_interface import INotification


class LoggerObserver(IObserver):
    """Observer that logs notifications to the console."""
    
    def update(self, notification: INotification) -> None:
        """
        Log the notification content.
        
        Args:
            notification: The notification to log
        """
        print(f"Logger: {notification.get_content()}")
