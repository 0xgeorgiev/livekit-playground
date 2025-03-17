"""
Connection to MongoDB database.
Store AI agent contexts and their current status.
"""
import uuid
import logging
import datetime
from pymongo import MongoClient
from fluwid_agent.configuration import MONGODB
from pymongo.errors import ConnectionFailure, OperationFailure, PyMongoError, DuplicateKeyError


class CustomersDatabase:
    """
    Database for storing and retrieving customer data.
    Mock implementation of CRM.
    """
    def __init__(self):
        """
        Initialize database connection

        :raises:    ConnectionFailure
        """
        try:
            self.cluster = MongoClient(MONGODB.cluster)
            self.collection = self.cluster[MONGODB.database][MONGODB.agent_contexts_collection]

        except ConnectionFailure as ex:
            raise ConnectionFailure(f"Could not connect to MongoDB database: {str(ex)}") from ex

    def __del__(self):
        """
        Close the connection to the MongoDB cluster

        :raises:     RuntimeError
        """
        try:
            self.cluster.close()

        except Exception as ex:
            raise RuntimeError(f"Error closing MongoDB connection: {str(ex)}") from ex
