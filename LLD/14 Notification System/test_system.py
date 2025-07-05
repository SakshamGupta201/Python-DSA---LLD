"""
Simple tests for the notification system.
Demonstrates the functionality and validates the refactored architecture.
"""

from notification_system import (
    NotificationService,
    SimpleNotification,
    NotificationWithTimestamp,
    NotificationWithSignature,
    NotificationObservable
)


def test_singleton_pattern():
    """Test that NotificationService implements singleton pattern correctly."""
    print("Testing Singleton Pattern...")
    
    service1 = NotificationService()
    service2 = NotificationService()
    
    assert service1 is service2, "NotificationService should be a singleton"
    print("✓ Singleton pattern working correctly\n")


def test_decorator_pattern():
    """Test the decorator pattern implementation."""
    print("Testing Decorator Pattern...")
    
    base = SimpleNotification("Test message")
    assert base.get_content() == "Test message"
    
    with_timestamp = NotificationWithTimestamp(base)
    timestamp_content = with_timestamp.get_content()
    assert "Test message" in timestamp_content
    assert "Timestamp:" in timestamp_content
    
    with_signature = NotificationWithSignature(with_timestamp, "Test User")
    signature_content = with_signature.get_content()
    assert "Test message" in signature_content
    assert "Timestamp:" in signature_content
    assert "Signature: Test User" in signature_content
    
    print("✓ Decorator pattern working correctly\n")


def test_observer_pattern():
    """Test the observer pattern implementation."""
    print("Testing Observer Pattern...")
    
    observable = NotificationObservable()
    
    # Track notifications received
    received_notifications = []
    
    class TestObserver:
        def update(self, notification):
            received_notifications.append(notification.get_content())
    
    observer = TestObserver()
    observable.add_observer(observer)
    
    notification = SimpleNotification("Observer test")
    observable.set_notification(notification)
    
    assert len(received_notifications) == 1
    assert received_notifications[0] == "Observer test"
    
    print("✓ Observer pattern working correctly\n")


def test_multiple_engines():
    """Test multiple notification engines."""
    print("Testing Multiple Engines...")
    
    service = NotificationService()
    observable = service.get_observable()
    
    # Clear any existing observers
    observable._observers.clear()
    
    # Track sent notifications
    sent_notifications = []
    
    class TrackingEngine:
        def __init__(self, engine_type):
            self.engine_type = engine_type
        
        def update(self, notification):
            sent_notifications.append(f"{self.engine_type}: {notification.get_content()}")
    
    # Add multiple engines
    email_engine = TrackingEngine("Email")
    sms_engine = TrackingEngine("SMS")
    push_engine = TrackingEngine("Push")
    
    observable.add_observer(email_engine)
    observable.add_observer(sms_engine)
    observable.add_observer(push_engine)
    
    # Send notification
    notification = SimpleNotification("Multi-engine test")
    service.send_notification(notification)
    
    assert len(sent_notifications) == 3
    assert any("Email:" in notif for notif in sent_notifications)
    assert any("SMS:" in notif for notif in sent_notifications)
    assert any("Push:" in notif for notif in sent_notifications)
    
    print("✓ Multiple engines working correctly\n")


def test_notification_history():
    """Test notification history functionality."""
    print("Testing Notification History...")
    
    service = NotificationService()
    
    # Clear history
    service.clear_history()
    
    # Send some notifications
    service.send_notification(SimpleNotification("Message 1"))
    service.send_notification(SimpleNotification("Message 2"))
    service.send_notification(SimpleNotification("Message 3"))
    
    history = service.get_notification_history()
    assert len(history) == 3
    
    # Verify history contents
    contents = [notif.get_content() for notif in history]
    assert "Message 1" in contents
    assert "Message 2" in contents
    assert "Message 3" in contents
    
    print("✓ Notification history working correctly\n")


def run_all_tests():
    """Run all tests."""
    print("=" * 50)
    print("NOTIFICATION SYSTEM TESTS")
    print("=" * 50)
    print()
    
    try:
        test_singleton_pattern()
        test_decorator_pattern()
        test_observer_pattern()
        test_multiple_engines()
        test_notification_history()
        
        print("=" * 50)
        print("ALL TESTS PASSED! ✓")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    run_all_tests()
