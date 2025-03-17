"""
Example test
"""
def add(a, b):
    return a + b

def test_add():
    # Basic assertion
    assert add(1, 2) == 3
    
    # Multiple assertions in one test
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    
def test_add_fails():
    # This will pass because the assertion correctly identifies that 2+2 is not 5
    assert add(2, 2) != 5

# Using pytest fixtures to set up test data
import pytest

@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_numbers):
    # Use the fixture data in a test
    assert sum(sample_numbers) == 15
    assert len(sample_numbers) == 5
