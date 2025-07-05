from abc import ABC, abstractmethod
from datetime import datetime


class INotification(ABC):
    @abstractmethod
    def get_content(): ...


class SimpleNotification(INotification):
    def __init__(self, content: str):
        self.content = content

    def get_content(self):
        return self.content


class NotificationDecorator(INotification):
    def __init__(self, notification: INotification):
        self._notification = notification

    def get_content(self):
        return self._notification.get_content()


class NotificationWithTimestamp(NotificationDecorator):
    def __init__(self, notification: INotification):
        super().__init__(notification)

    def get_content(self):
        return f"{self._notification.get_content()} (Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"


class NotificationWithSignature(NotificationDecorator):
    def __init__(self, notification: INotification, signature: str):
        super().__init__(notification)
        self.signature = signature

    def get_content(self):
        return f"{self._notification.get_content()} (Signature: {self.signature})"


class IObeservable(ABC):
    @abstractmethod
    def add_observer(self, observer: "IObserver"): ...

    @abstractmethod
    def remove_observer(self, observer: "IObserver"): ...

    @abstractmethod
    def notify_observers(self): ...


class IObserver(ABC):
    @abstractmethod
    def update(): ...


# Concrete Observable
class NotificationObservable(IObeservable):
    def __init__(self):
        self._observers: list[IObserver] = []
        self._notification = None

    def add_observer(self, observer: IObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._notification)

    def set_notification(self, notification: INotification):
        self._notification = notification
        self.notify_observers()


# Concrete Observer 1
class LoggerObserver(IObserver):
    def update(self, notification: INotification):
        print(f"Logger: {notification.get_content()}")


class NotificationEngine(IObserver):
    @abstractmethod
    def update(self, notification: INotification): ...


class INotificationEngine(NotificationEngine, ABC):
    @abstractmethod
    def send_notification(self, notification: INotification): ...


class EmailNotificationEngine(INotificationEngine):

    def __init__(self, smtp_server: str = "smtp.example.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port

    def update(self, notification: INotification):
        self.send_notification(notification)

    def send_notification(self, notification: INotification):
        print(
            f"Sending Email via {self.smtp_server}:{self.port} - Content: {notification.get_content()}"
        )


class SMSNotificationEngine(INotificationEngine):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, notification: INotification):
        self.send_notification(notification)

    def send_notification(self, notification: INotification):
        print(f"Sending SMS to {self.phone_number}: {notification.get_content()}")


class PushNotificationEngine(INotificationEngine):
    def __init__(self, device_token: str):
        self.device_token = device_token

    def update(self, notification: INotification):
        self.send_notification(notification)

    def send_notification(self, notification: INotification):
        print(
            f"Sending Push Notification to {self.device_token}: {notification.get_content()}"
        )


class NotificationService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.notifications: list[INotification] = []
            self._observable = NotificationObservable()
            self.initialized = True

    def send_notification(self, notification: INotification):
        self.notifications.append(notification)
        self._observable.set_notification(notification)

    def get_observable(self):
        return self._observable


notification_service = NotificationService()
notification_observable = notification_service.get_observable()
logger = LoggerObserver()
email_notification_engine = EmailNotificationEngine(
    smtp_server="smtp.example.com", port=587
)

notification_observable.add_observer(logger)
notification_observable.add_observer(email_notification_engine)

notification = SimpleNotification("Hello, World!")
timestamp_notification = NotificationWithTimestamp(notification)
signature_notification = NotificationWithSignature(timestamp_notification, "John Doe")

notification_service.send_notification(signature_notification)
