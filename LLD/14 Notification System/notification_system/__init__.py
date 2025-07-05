"""
Notification System Package

A comprehensive notification system implementing multiple design patterns:
- Observer Pattern: For notification distribution
- Decorator Pattern: For notification enhancement 
- Singleton Pattern: For service management

This package provides a flexible and extensible notification framework
that supports multiple delivery channels (email, SMS, push notifications)
with features like timestamps and signatures.

Usage:
    from notification_system import NotificationService, SimpleNotification
    from notification_system.engines import EmailNotificationEngine
    from notification_system.observers import LoggerObserver
    
    # Get the singleton service instance
    service = NotificationService()
    observable = service.get_observable()
    
    # Register observers
    email_engine = EmailNotificationEngine()
    logger = LoggerObserver()
    observable.add_observer(email_engine)
    observable.add_observer(logger)
    
    # Send notification
    notification = SimpleNotification("Hello World!")
    service.send_notification(notification)
"""

# Core interfaces
from .interfaces import (
    INotification,
    IObserver,
    IObeservable,
    INotificationEngine
)

# Notification implementations
from .notifications import (
    SimpleNotification,
    NotificationDecorator,
    NotificationWithTimestamp,
    NotificationWithSignature
)

# Observer implementations
from .observers import (
    LoggerObserver,
    NotificationObservable
)

# Notification engines
from .engines import (
    EmailNotificationEngine,
    SMSNotificationEngine,
    PushNotificationEngine
)

# Services
from .services import NotificationService

# Version info
__version__ = "1.0.0"
__author__ = "Notification System Team"

# Public API
__all__ = [
    # Interfaces
    'INotification',
    'IObserver', 
    'IObeservable',
    'INotificationEngine',
    
    # Notifications
    'SimpleNotification',
    'NotificationDecorator',
    'NotificationWithTimestamp',
    'NotificationWithSignature',
    
    # Observers
    'LoggerObserver',
    'NotificationObservable',
    
    # Engines
    'EmailNotificationEngine',
    'SMSNotificationEngine',
    'PushNotificationEngine',
    
    # Services
    'NotificationService'
]
