"""
SMS notification engine implementation.
Handles SMS delivery to mobile devices.
"""

from ..interfaces.engine_interface import INotificationEngine
from ..interfaces.notification_interface import INotification


class SMSNotificationEngine(INotificationEngine):
    """Notification engine for sending SMS messages."""
    
    def __init__(self, phone_number: str):
        """
        Initialize the SMS engine.
        
        Args:
            phone_number: Target phone number for SMS delivery
        """
        self.phone_number = phone_number

    def update(self, notification: INotification) -> None:
        """
        Observer pattern update method that triggers SMS sending.
        
        Args:
            notification: The notification to send via SMS
        """
        self.send_notification(notification)

    def send_notification(self, notification: INotification) -> None:
        """
        Send notification via SMS.
        
        Args:
            notification: The notification to send
        """
        print(f"Sending SMS to {self.phone_number}: {notification.get_content()}")
