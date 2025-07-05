"""
Configuration settings for the notification system.
"""

from typing import Dict, Any


class NotificationConfig:
    """Configuration class for notification system settings."""
    
    # Email configuration
    EMAIL_SETTINGS: Dict[str, Any] = {
        'default_smtp_server': 'smtp.example.com',
        'default_port': 587,
        'timeout': 30,
        'use_tls': True
    }
    
    # SMS configuration  
    SMS_SETTINGS: Dict[str, Any] = {
        'default_provider': 'twilio',
        'retry_attempts': 3,
        'timeout': 15
    }
    
    # Push notification configuration
    PUSH_SETTINGS: Dict[str, Any] = {
        'default_provider': 'firebase',
        'batch_size': 100,
        'retry_attempts': 2
    }
    
    # Logging configuration
    LOGGING_SETTINGS: Dict[str, Any] = {
        'log_level': 'INFO',
        'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'enable_file_logging': False
    }
    
    # General settings
    GENERAL_SETTINGS: Dict[str, Any] = {
        'max_notification_history': 1000,
        'enable_notification_queuing': False,
        'default_timezone': 'UTC'
    }
