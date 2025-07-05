"""
Comprehensive demonstration of the refactored notification system.
Shows all features and design patterns in action.
"""

from notification_system import (
    NotificationService,
    SimpleNotification,
    NotificationWithTimestamp,
    NotificationWithSignature,
    LoggerObserver
)
from notification_system.engines import (
    EmailNotificationEngine,
    SMSNotificationEngine,
    PushNotificationEngine
)


def demonstrate_full_system():
    """Demonstrate the complete notification system functionality."""
    print("🔔 COMPREHENSIVE NOTIFICATION SYSTEM DEMONSTRATION")
    print("=" * 60)
    print()
    
    # 1. Initialize the singleton service
    print("1️⃣ Initializing Notification Service (Singleton Pattern)")
    service = NotificationService()
    observable = service.get_observable()
    print("   ✓ Service initialized")
    print()
    
    # 2. Create multiple delivery engines
    print("2️⃣ Setting up Multiple Delivery Engines")
    email_engine = EmailNotificationEngine("smtp.company.com", 587)
    sms_engine = SMSNotificationEngine("+1-555-0123")
    push_engine = PushNotificationEngine("device_abc123")
    logger = LoggerObserver()
    
    # Register all observers
    observable.add_observer(email_engine)
    observable.add_observer(sms_engine)
    observable.add_observer(push_engine)
    observable.add_observer(logger)
    
    print("   ✓ Email Engine registered")
    print("   ✓ SMS Engine registered")
    print("   ✓ Push Notification Engine registered")
    print("   ✓ Logger Observer registered")
    print()
    
    # 3. Demonstrate decorator pattern
    print("3️⃣ Creating Enhanced Notifications (Decorator Pattern)")
    
    # Basic notification
    base_notification = SimpleNotification("System maintenance scheduled for tonight")
    print(f"   📝 Base: {base_notification.get_content()}")
    
    # Add timestamp
    timed_notification = NotificationWithTimestamp(base_notification)
    print(f"   🕐 With timestamp: {timed_notification.get_content()}")
    
    # Add signature
    signed_notification = NotificationWithSignature(timed_notification, "IT Admin")
    print(f"   ✍️  With signature: {signed_notification.get_content()}")
    print()
    
    # 4. Send notifications and demonstrate observer pattern
    print("4️⃣ Broadcasting Notifications (Observer Pattern)")
    print("   📤 Sending notification to all registered engines...")
    print("   " + "-" * 50)
    
    service.send_notification(signed_notification)
    
    print("   " + "-" * 50)
    print("   ✓ Notification delivered through all channels")
    print()
    
    # 5. Send multiple notifications
    print("5️⃣ Sending Multiple Notifications")
    
    notifications = [
        SimpleNotification("Welcome to our service!"),
        NotificationWithTimestamp(SimpleNotification("Your order has been processed")),
        NotificationWithSignature(
            NotificationWithTimestamp(SimpleNotification("Payment confirmation")),
            "Finance Team"
        )
    ]
    
    for i, notification in enumerate(notifications, 1):
        print(f"   📨 Sending notification {i}: {notification.get_content()}")
        service.send_notification(notification)
    
    print()
    
    # 6. Display statistics
    print("6️⃣ System Statistics")
    history = service.get_notification_history()
    print(f"   📊 Total notifications sent: {len(history)}")
    print(f"   🎯 Active observers: {len(observable._observers)}")
    print()
    
    # 7. Demonstrate observer management
    print("7️⃣ Dynamic Observer Management")
    print("   🔌 Removing SMS engine...")
    observable.remove_observer(sms_engine)
    
    print("   📤 Sending notification without SMS:")
    print("   " + "-" * 30)
    service.send_notification(SimpleNotification("SMS engine removed"))
    print("   " + "-" * 30)
    print("   ✓ Notification sent only to remaining engines")
    print()
    
    # 8. Final summary
    print("8️⃣ Demonstration Complete!")
    print("   🎉 All design patterns successfully demonstrated:")
    print("      • Singleton Pattern: Single service instance")
    print("      • Observer Pattern: Multiple delivery channels")
    print("      • Decorator Pattern: Enhanced notifications")
    print("   🏗️  Architecture benefits:")
    print("      • Modular and maintainable code")
    print("      • Easy to extend with new features")
    print("      • Loose coupling between components")
    print("      • High cohesion within modules")
    print()
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_full_system()
