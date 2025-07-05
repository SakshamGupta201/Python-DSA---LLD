"""
Observer pattern interfaces.
Defines the observer and observable contracts for the notification system.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .notification_interface import INotification


class IObserver(ABC):
    """Abstract base class for all observers."""
    
    @abstractmethod
    def update(self, notification: "INotification") -> None:
        """
        Called when the observable notifies its observers.
        
        Args:
            notification: The notification that triggered the update
        """
        pass


class IObeservable(ABC):
    """Abstract base class for observable objects."""
    
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        """
        Add an observer to the observable.
        
        Args:
            observer: The observer to add
        """
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        """
        Remove an observer from the observable.
        
        Args:
            observer: The observer to remove
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """Notify all registered observers of a change."""
        pass
