"""
Simple notification implementation.
Basic concrete implementation of the INotification interface.
"""

from ..interfaces.notification_interface import INotification


class SimpleNotification(INotification):
    """A simple notification with plain text content."""
    
    def __init__(self, content: str):
        """
        Initialize a simple notification.
        
        Args:
            content: The notification message content
        """
        self.content = content

    def get_content(self) -> str:
        """
        Get the notification content.
        
        Returns:
            str: The notification content
        """
        return self.content
