"""
Interfaces package for the notification system.
Defines abstract base classes and contracts for the notification system components.
"""

from .notification_interface import INotification
from .observer_interface import IObserver, IObeservable
from .engine_interface import INotificationEngine

__all__ = [
    'INotification',
    'IObserver', 
    'IObeservable',
    'INotificationEngine'
]
