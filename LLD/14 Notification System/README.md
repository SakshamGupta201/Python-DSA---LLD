# Notification System

A comprehensive, extensible notification system implemented in Python using multiple design patterns for maximum flexibility and maintainability.

## Design Patterns Used

- **Observer Pattern**: For notification distribution and event handling
- **Decorator Pattern**: For enhancing notifications with additional features
- **Singleton Pattern**: For service management and global access

## Architecture Overview

```
notification_system/
├── interfaces/           # Abstract base classes and contracts
│   ├── notification_interface.py
│   ├── observer_interface.py
│   └── engine_interface.py
├── notifications/        # Notification implementations
│   ├── simple_notification.py
│   └── notification_decorators.py
├── observers/           # Observer pattern implementations
│   ├── logger_observer.py
│   └── notification_observable.py
├── engines/             # Notification delivery engines
│   ├── email_engine.py
│   ├── sms_engine.py
│   └── push_engine.py
└── services/            # Core service layer
    └── notification_service.py
```

## Features

### Notification Types
- **SimpleNotification**: Basic notification with plain text content
- **NotificationWithTimestamp**: Adds timestamp to notifications
- **NotificationWithSignature**: Adds signature to notifications
- **Custom Decorators**: Easy to extend with new features

### Delivery Engines
- **EmailNotificationEngine**: SMTP-based email delivery
- **SMSNotificationEngine**: SMS message delivery
- **PushNotificationEngine**: Mobile push notification delivery

### Observer System
- **LoggerObserver**: Console logging for notifications
- **NotificationObservable**: Manages observer registration and notification

## Usage Examples

### Basic Usage

```python
from notification_system import (
    NotificationService,
    SimpleNotification,
    LoggerObserver
)
from notification_system.engines import EmailNotificationEngine

# Get singleton service instance
service = NotificationService()
observable = service.get_observable()

# Register observers
logger = LoggerObserver()
email_engine = EmailNotificationEngine()

observable.add_observer(logger)
observable.add_observer(email_engine)

# Send notification
notification = SimpleNotification("Hello World!")
service.send_notification(notification)
```

### Enhanced Notifications with Decorators

```python
from notification_system import (
    SimpleNotification,
    NotificationWithTimestamp,
    NotificationWithSignature
)

# Create base notification
base = SimpleNotification("Important message")

# Add timestamp
with_timestamp = NotificationWithTimestamp(base)

# Add signature
with_signature = NotificationWithSignature(with_timestamp, "Admin")

# Send enhanced notification
service.send_notification(with_signature)
```

### Multiple Delivery Channels

```python
from notification_system.engines import (
    EmailNotificationEngine,
    SMSNotificationEngine,
    PushNotificationEngine
)

# Create multiple engines
email_engine = EmailNotificationEngine("smtp.gmail.com", 587)
sms_engine = SMSNotificationEngine("+1234567890")
push_engine = PushNotificationEngine("device_token_123")

# Register all engines
observable.add_observer(email_engine)
observable.add_observer(sms_engine)
observable.add_observer(push_engine)

# Single notification will be sent through all channels
service.send_notification(notification)
```

## Extensibility

### Adding New Notification Types

```python
from notification_system.interfaces import INotification

class CustomNotification(INotification):
    def __init__(self, title: str, body: str, priority: str):
        self.title = title
        self.body = body
        self.priority = priority
    
    def get_content(self) -> str:
        return f"[{self.priority}] {self.title}: {self.body}"
```

### Adding New Delivery Engines

```python
from notification_system.interfaces import INotificationEngine

class SlackNotificationEngine(INotificationEngine):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def update(self, notification):
        self.send_notification(notification)
    
    def send_notification(self, notification):
        # Implement Slack API integration
        pass
```

### Adding New Decorators

```python
from notification_system.notifications import NotificationDecorator

class NotificationWithPriority(NotificationDecorator):
    def __init__(self, notification, priority: str):
        super().__init__(notification)
        self.priority = priority
    
    def get_content(self) -> str:
        return f"[{self.priority}] {self._notification.get_content()}"
```

## Benefits of This Architecture

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Loose Coupling**: Components communicate through interfaces
3. **High Cohesion**: Related functionality is grouped together
4. **Extensibility**: Easy to add new notification types and delivery channels
5. **Testability**: Each component can be tested in isolation
6. **Maintainability**: Clear structure makes the code easy to understand and modify
7. **Reusability**: Components can be reused in different contexts

## Running the Example

```bash
cd "d:\Programming\Python\LLD\14 Notification System"
python example_usage.py
```

## Testing

Each module can be tested independently due to the modular design:

```python
# Test notification creation
notification = SimpleNotification("Test")
assert notification.get_content() == "Test"

# Test decorators
enhanced = NotificationWithTimestamp(notification)
assert "Timestamp:" in enhanced.get_content()

# Test observer pattern
observable = NotificationObservable()
observer = LoggerObserver()
observable.add_observer(observer)
# ... test notification delivery
```

This refactored architecture provides a solid foundation for a production-ready notification system that can easily evolve with changing requirements.
