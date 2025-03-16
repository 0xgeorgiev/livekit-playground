"""
Pytest configuration for livekit_playground tests
"""
import os
import sys
import pytest

# Configure pytest
def pytest_configure(config):
    """Configure pytest"""
    # Register custom markers
    config.addinivalue_line("markers", "mongodb: mark test as requiring MongoDB")
    config.addinivalue_line("markers", "integration: mark test as an integration test")