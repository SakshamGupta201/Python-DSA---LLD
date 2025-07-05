"""
Email notification engine implementation.
Handles email delivery through SMTP.
"""

from ..interfaces.engine_interface import INotificationEngine
from ..interfaces.notification_interface import INotification


class EmailNotificationEngine(INotificationEngine):
    """Notification engine for sending emails via SMTP."""
    
    def __init__(self, smtp_server: str = "smtp.example.com", port: int = 587):
        """
        Initialize the email engine.
        
        Args:
            smtp_server: SMTP server hostname
            port: SMTP server port
        """
        self.smtp_server = smtp_server
        self.port = port

    def update(self, notification: INotification) -> None:
        """
        Observer pattern update method that triggers email sending.
        
        Args:
            notification: The notification to send via email
        """
        self.send_notification(notification)

    def send_notification(self, notification: INotification) -> None:
        """
        Send notification via email.
        
        Args:
            notification: The notification to send
        """
        print(
            f"Sending Email via {self.smtp_server}:{self.port} - "
            f"Content: {notification.get_content()}"
        )
