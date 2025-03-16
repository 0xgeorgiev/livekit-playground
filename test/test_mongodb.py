"""
Tests for MongoDB functionality
"""
import pytest
import mongomock
import pymongo
from datetime import datetime
from unittest.mock import patch, MagicMock
from fluwid_agent.mongodb.customers_collection import CustomersDatabase
from fluwid_agent.tools.customer_data import CustomerDataTool

# Sample customer data for testing
SAMPLE_CUSTOMERS = [
    {
        "name": "Teodor Georgiev",
        "age": 25,
        "language": "Bulgarian",
        "visits": [
            {
                "date": "2024-01-15",
                "coach": "Stefan",
                "duration": 15,
                "notes": ["Initial assessment", "Enthusiastic about technology"]
            },
            {
                "date": "2024-01-22",
                "coach": "Stefan",
                "duration": 15,
                "notes": ["Reported improvement in back stiffness"]
            }
        ],
        "symptoms": [
            "Lower back pain",
            "Poor posture from desk work",
            "Decreased mobility"
        ],
        "communications": [
            {
                "type": "Email",
                "date": "2024-01-16",
                "status": "Sent"
            },
            {
                "type": "Call",
                "date": "2024-01-24",
                "status": "Completed"
            }
        ],
        "notes": [
            {
                "text": "Found Osteostrong through Facebook",
                "timestamp": datetime(2024, 1, 15, 10, 30)
            },
            {
                "text": "Concerned about time commitment",
                "timestamp": datetime(2024, 1, 22, 14, 15)
            }
        ]
    },
    {
        "name": "Maria Santos",
        "age": 42,
        "language": "English",
        "visits": [
            {
                "date": "2024-02-01",
                "coach": "Elena",
                "duration": 15,
                "notes": ["Initial assessment", "Clear strength goals"]
            }
        ],
        "symptoms": [
            "Osteoporosis concerns",
            "Joint stiffness"
        ],
        "communications": [
            {
                "type": "Email",
                "date": "2024-02-02",
                "status": "Sent"
            }
        ],
        "notes": [
            {
                "text": "Doctor referral",
                "timestamp": datetime(2024, 2, 1, 9, 45)
            }
        ]
    }
]

@pytest.fixture
def mock_mongodb():
    """Create a mock MongoDB client and populate with test data"""
    with patch('pymongo.MongoClient') as mock_client:
        # Create a mongomock client
        mock_mongo = mongomock.MongoClient()
        mock_client.return_value = mock_mongo
        
        # Set up the database and collection
        db = mock_mongo["fluwit_agent"]
        collection = db["agent_contexts"]
        
        # Insert test data
        collection.insert_many(SAMPLE_CUSTOMERS)
        
        yield mock_mongo

@pytest.fixture
def customers_db(mock_mongodb):
    """Create a CustomersDatabase instance with mocked MongoDB"""
    return CustomersDatabase()

@pytest.fixture
def customer_tool(customers_db):
    """Create a CustomerDataTool instance with mocked database"""
    tool = CustomerDataTool()
    tool.db = customers_db
    return tool

class TestCustomersDatabase:
    """Tests for the CustomersDatabase class"""
    
    def test_init_connection(self, mock_mongodb):
        """Test database connection initialization"""
        db = CustomersDatabase()
        assert db.cluster is not None
        assert db.collection is not None
    
    def test_init_connection_failure(self):
        """Test handling of connection failure"""
        with patch('pymongo.MongoClient', side_effect=pymongo.errors.ConnectionFailure("Connection error")):
            with pytest.raises(pymongo.errors.ConnectionFailure):
                CustomersDatabase()
    
    def test_close_connection(self, mock_mongodb):
        """Test connection closing on object destruction"""
        db = CustomersDatabase()
        # Mock the close method to check if it's called
        db.cluster.close = MagicMock()
        
        # Manually call __del__ since it's not guaranteed to be called in tests
        db.__del__()
        
        db.cluster.close.assert_called_once()
    
    def test_close_connection_error(self, mock_mongodb):
        """Test handling of error during connection closing"""
        db = CustomersDatabase()
        # Mock the close method to raise an exception
        db.cluster.close = MagicMock(side_effect=Exception("Close error"))
        
        # Should raise RuntimeError
        with pytest.raises(RuntimeError):
            db.__del__()

class TestCustomerDataTool:
    """Tests for the CustomerDataTool class"""
    
    def test_get_customer_data_existing(self, customer_tool):
        """Test retrieving data for an existing customer"""
        result = customer_tool.get_customer_data("Teodor Georgiev")
        
        # Check that the result contains expected information
        assert "Teodor Georgiev" in result
        assert "25" in result
        assert "Bulgarian" in result
        assert "Lower back pain" in result
        assert "Stefan" in result
        assert "2024-01-15" in result
    
    def test_get_customer_data_nonexistent(self, customer_tool):
        """Test retrieving data for a non-existent customer"""
        result = customer_tool.get_customer_data("Nonexistent Customer")
        assert "Customer not found" in result
    
    def test_get_customer_data_error(self, customer_tool):
        """Test error handling during data retrieval"""
        # Mock find_one to raise an exception
        customer_tool.db.collection.find_one = MagicMock(side_effect=Exception("Database error"))
        
        result = customer_tool.get_customer_data("Teodor Georgiev")
        assert "Error retrieving customer data" in result
    
    def test_add_customer_note_existing(self, customer_tool):
        """Test adding a note to an existing customer"""
        result = customer_tool.add_customer_note(
            "Teodor Georgiev", 
            "Interested in long-term membership"
        )
        
        # Verify the note was added
        assert "Note added to Teodor Georgiev's record" in result
        
        # Check that update_one was called with correct parameters
        customer_tool.db.collection.update_one.assert_called_once()
        args, kwargs = customer_tool.db.collection.update_one.call_args
        assert args[0] == {"name": "Teodor Georgiev"}
        assert "$push" in args[1]
        assert "notes" in args[1]["$push"]
        assert args[1]["$push"]["notes"]["text"] == "Interested in long-term membership"
    
    def test_add_customer_note_nonexistent(self, customer_tool):
        """Test adding a note to a non-existent customer"""
        # Mock update_one to return a result with matched_count=0
        mock_result = MagicMock()
        mock_result.matched_count = 0
        customer_tool.db.collection.update_one = MagicMock(return_value=mock_result)
        
        result = customer_tool.add_customer_note(
            "Nonexistent Customer", 
            "This note shouldn't be added"
        )
        
        assert "Customer not found" in result
    
    def test_add_customer_note_error(self, customer_tool):
        """Test error handling when adding a note"""
        # Mock update_one to raise an exception
        customer_tool.db.collection.update_one = MagicMock(side_effect=Exception("Database error"))
        
        result = customer_tool.add_customer_note(
            "Teodor Georgiev", 
            "This note will cause an error"
        )
        
        assert "Error adding note" in result
    
    def test_format_visits(self, customer_tool):
        """Test formatting of visit history"""
        visits = [
            {
                "date": "2024-03-01",
                "coach": "Alex",
                "duration": 20,
                "notes": ["Progress check", "Increased resistance"]
            }
        ]
        
        result = customer_tool._format_visits(visits)
        
        assert "Visit 1 (2024-03-01)" in result
        assert "Coach: Alex" in result
        assert "Duration: 20 minutes" in result
        assert "Progress check" in result
        assert "Increased resistance" in result
    
    def test_format_empty_visits(self, customer_tool):
        """Test formatting of empty visit history"""
        result = customer_tool._format_visits([])
        assert "No visits recorded" in result
    
    def test_format_communications(self, customer_tool):
        """Test formatting of communication history"""
        communications = [
            {
                "type": "SMS",
                "date": "2024-03-05",
                "status": "Delivered"
            }
        ]
        
        result = customer_tool._format_communications(communications)
        
        assert "SMS: 2024-03-05" in result
        assert "Status: Delivered" in result
    
    def test_format_empty_communications(self, customer_tool):
        """Test formatting of empty communication history"""
        result = customer_tool._format_communications([])
        assert "No communications recorded" in result
    
    def test_format_list(self, customer_tool):
        """Test formatting of general list items"""
        items = ["Item 1", "Item 2", "Item 3"]
        result = customer_tool._format_list(items)
        
        assert "- Item 1" in result
        assert "- Item 2" in result
        assert "- Item 3" in result
    
    def test_format_empty_list(self, customer_tool):
        """Test formatting of empty list"""
        result = customer_tool._format_list([])
        assert "None recorded" in result