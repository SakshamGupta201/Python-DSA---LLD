"""
Example usage of the refactored notification system.

This example demonstrates how to use the notification system with various
engines and decorators. It maintains the same functionality as the original
main.py but with improved organization and readability.
"""

from notification_system import (
    NotificationService,
    SimpleNotification,
    NotificationWithTimestamp,
    NotificationWithSignature,
    LoggerObserver
)
from notification_system.engines import EmailNotificationEngine


def main():
    """Demonstrate the notification system functionality."""
    print("=== Notification System Demo ===\n")
    
    # Get the singleton notification service
    notification_service = NotificationService()
    notification_observable = notification_service.get_observable()
    
    # Create and register observers
    logger = LoggerObserver()
    email_engine = EmailNotificationEngine(
        smtp_server="smtp.example.com", 
        port=587
    )
    
    # Register observers with the observable
    notification_observable.add_observer(logger)
    notification_observable.add_observer(email_engine)
    
    print("Registered observers: Logger and Email Engine\n")
    
    # Create a simple notification
    base_notification = SimpleNotification("Hello, World!")
    print(f"Base notification: {base_notification.get_content()}\n")
    
    # Enhance the notification with decorators
    timestamp_notification = NotificationWithTimestamp(base_notification)
    print(f"With timestamp: {timestamp_notification.get_content()}\n")
    
    signature_notification = NotificationWithSignature(
        timestamp_notification, 
        "John Doe"
    )
    print(f"With signature: {signature_notification.get_content()}\n")
    
    # Send the enhanced notification
    print("Sending notification through the system:")
    print("-" * 50)
    notification_service.send_notification(signature_notification)
    
    print("-" * 50)
    print(f"\nTotal notifications sent: {len(notification_service.get_notification_history())}")


if __name__ == "__main__":
    main()
