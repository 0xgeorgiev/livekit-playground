"""
Integration tests for MongoDB functionality
Requires a real MongoDB connection
"""
import pytest
import os
from datetime import datetime
from fluwid_agent.mongodb.customers_collection import CustomersDatabase
from fluwid_agent.tools.customer_data import CustomerDataTool

# Skip all tests if MONGODB_INTEGRATION_TEST environment variable is not set
pytestmark = pytest.mark.skipif(
    os.environ.get("MONGODB_INTEGRATION_TEST") != "1",
    reason="MongoDB integration tests are disabled"
)

@pytest.fixture
def setup_test_db():
    """Set up a test database and clean it after tests"""
    # Create database connection
    db = CustomersDatabase()
    
    # Use a test collection
    original_collection = db.collection
    db.collection = db.cluster[db.collection.database.name]["test_agent_contexts"]
    
    # Clear any existing data
    db.collection.delete_many({})
    
    # Insert test customer
    db.collection.insert_one({
        "name": "Test Customer",
        "age": 30,
        "language": "English",
        "visits": [],
        "symptoms": ["Test symptom"],
        "communications": [],
        "notes": []
    })
    
    yield db
    
    # Clean up
    db.collection.delete_many({})
    db.collection = original_collection

@pytest.fixture
def customer_tool(setup_test_db):
    """Create CustomerDataTool with test database"""
    tool = CustomerDataTool()
    tool.db = setup_test_db
    return tool

class TestMongoDBIntegration:
    """Integration tests with real MongoDB connection"""
    
    def test_get_customer(self, customer_tool):
        """Test retrieving a customer from the database"""
        result = customer_tool.get_customer_data("Test Customer")
        assert "Test Customer" in result
        assert "30" in result
        assert "Test symptom" in result
    
    def test_add_note(self, customer_tool, setup_test_db):
        """Test adding a note to a customer"""
        # Add a note
        result = customer_tool.add_customer_note(
            "Test Customer",
            "Integration test note"
        )
        assert "Note added to Test Customer's record" in result
        
        # Verify the note was added to the database
        customer = setup_test_db.collection.find_one({"name": "Test Customer"})
        assert customer is not None
        assert len(customer["notes"]) == 1
        assert customer["notes"][0]["text"] == "Integration test note"