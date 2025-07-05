"""
Notification observable implementation.
Concrete implementation of the observable pattern for notifications.
"""

from typing import List, Optional
from ..interfaces.observer_interface import IObeservable, IObserver
from ..interfaces.notification_interface import INotification


class NotificationObservable(IObeservable):
    """Concrete observable that manages notification observers."""
    
    def __init__(self):
        """Initialize the observable with empty observer list."""
        self._observers: List[IObserver] = []
        self._notification: Optional[INotification] = None

    def add_observer(self, observer: IObserver) -> None:
        """
        Add an observer to the notification list.
        
        Args:
            observer: The observer to add
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        """
        Remove an observer from the notification list.
        
        Args:
            observer: The observer to remove
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        """Notify all registered observers of the current notification."""
        if self._notification is not None:
            for observer in self._observers:
                observer.update(self._notification)

    def set_notification(self, notification: INotification) -> None:
        """
        Set a new notification and notify all observers.
        
        Args:
            notification: The new notification to set
        """
        self._notification = notification
        self.notify_observers()
        
    def get_notification(self) -> Optional[INotification]:
        """
        Get the current notification.
        
        Returns:
            Optional[INotification]: The current notification or None
        """
        return self._notification
