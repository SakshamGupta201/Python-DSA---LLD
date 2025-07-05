"""
Notification decorators implementing the Decorator pattern.
Provides enhanced notifications with additional features like timestamps and signatures.
"""

from datetime import datetime
from ..interfaces.notification_interface import INotification


class NotificationDecorator(INotification):
    """Base decorator class for notifications."""
    
    def __init__(self, notification: INotification):
        """
        Initialize the decorator with a notification to wrap.
        
        Args:
            notification: The notification to decorate
        """
        self._notification = notification

    def get_content(self) -> str:
        """
        Get the content from the wrapped notification.
        
        Returns:
            str: The notification content
        """
        return self._notification.get_content()


class NotificationWithTimestamp(NotificationDecorator):
    """Decorator that adds a timestamp to notifications."""
    
    def __init__(self, notification: INotification):
        """
        Initialize the timestamp decorator.
        
        Args:
            notification: The notification to add timestamp to
        """
        super().__init__(notification)

    def get_content(self) -> str:
        """
        Get the notification content with timestamp.
        
        Returns:
            str: The notification content with timestamp
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{self._notification.get_content()} (Timestamp: {timestamp})"


class NotificationWithSignature(NotificationDecorator):
    """Decorator that adds a signature to notifications."""
    
    def __init__(self, notification: INotification, signature: str):
        """
        Initialize the signature decorator.
        
        Args:
            notification: The notification to add signature to
            signature: The signature to append
        """
        super().__init__(notification)
        self.signature = signature

    def get_content(self) -> str:
        """
        Get the notification content with signature.
        
        Returns:
            str: The notification content with signature
        """
        return f"{self._notification.get_content()} (Signature: {self.signature})"
