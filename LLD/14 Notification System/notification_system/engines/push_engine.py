"""
Push notification engine implementation.
Handles push notifications to mobile apps and devices.
"""

from ..interfaces.engine_interface import INotificationEngine
from ..interfaces.notification_interface import INotification


class PushNotificationEngine(INotificationEngine):
    """Notification engine for sending push notifications."""
    
    def __init__(self, device_token: str):
        """
        Initialize the push notification engine.
        
        Args:
            device_token: Device token for push notification delivery
        """
        self.device_token = device_token

    def update(self, notification: INotification) -> None:
        """
        Observer pattern update method that triggers push notification sending.
        
        Args:
            notification: The notification to send via push
        """
        self.send_notification(notification)

    def send_notification(self, notification: INotification) -> None:
        """
        Send notification via push notification.
        
        Args:
            notification: The notification to send
        """
        print(
            f"Sending Push Notification to {self.device_token}: "
            f"{notification.get_content()}"
        )
