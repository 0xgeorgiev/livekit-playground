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


class AssistantContextDatabase:
    """
    Database for storing and retrieving AI agent contexts
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

    def create_context(self, context_data):
        """
        Store a new agent context in the MongoDB collection

        :param context_data:    The context data for the AI agent

        :return:                The ID of the inserted context
        :raises:                DuplicateKeyError, OperationFailure, PyMongoError, RuntimeError
        """
        try:
            # Check if a context with the same agent_id already exists
            if 'agent_id' in context_data and context_data.get('agent_id'):
                existing_context = self.collection.find_one({'agent_id': context_data.get('agent_id')})
                if existing_context:
                    raise DuplicateKeyError(f"Context for agent_id {context_data.get('agent_id')} already exists")

            context_id = str(uuid.uuid4())
            doc = {
                '_id': context_id,
                'agent_id': context_data.get('agent_id'),
                'name': context_data.get('name'),
                'context': context_data.get('context', {}),
                'status': context_data.get('status', 'active'),
                'created_at': datetime.datetime.now(datetime.UTC),
                'updated_at': datetime.datetime.now(datetime.UTC),
                'metadata': context_data.get('metadata', {})
            }
            result = self.collection.insert_one(document=doc)

            if result:
                logging.info(f'Created context with ID {context_id}')
                return context_id

            raise RuntimeError(f"Could not create context with ID {context_id}")

        except DuplicateKeyError as ex:
            raise DuplicateKeyError(f"Duplicate key error: {str(ex)}") from ex

        except OperationFailure as ex:
            raise OperationFailure(f"Operation failure: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"General PyMongo error: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when creating context: {str(ex)}") from ex

    def update_context(self, context_id, update_data):
        """
        Update an existing agent context

        :param context_id:      The ID of the context to update
        :param update_data:     Dictionary containing the fields to update

        :return:                The ID of the updated context
        :raises:                ValueError, OperationFailure, PyMongoError, RuntimeError
        """
        try:
            # Add updated_at timestamp
            update_data['updated_at'] = datetime.datetime.utcnow()
            
            result = self.collection.update_one(
                {'_id': context_id},
                {'$set': update_data}
            )

            if result.modified_count:
                logging.info(f"Updated context {context_id}")
                return context_id

            raise RuntimeError(f"Could not update context {context_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to update context {context_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to update context {context_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when updating context {context_id}: {str(ex)}") from ex

    def update_context_status(self, context_id, status):
        """
        Update the status of an agent context

        :param context_id:      The ID of the context
        :param status:          New status of the context (e.g., 'active', 'archived', 'paused')

        :return:                The ID of the updated context
        :raises:                ValueError, OperationFailure, PyMongoError, RuntimeError
        """
        try:
            valid_statuses = ['active', 'archived', 'paused', 'completed']
            if status not in valid_statuses:
                raise ValueError(f"Invalid status: {status}. Allowed values are {', '.join(valid_statuses)}")

            result = self.collection.update_one(
                {'_id': context_id},
                {'$set': {
                    'status': status,
                    'updated_at': datetime.datetime.utcnow()
                }}
            )

            if result.modified_count:
                logging.info(f"Updated status of context {context_id} to {status}")
                return context_id

            raise RuntimeError(f"Could not update status of context {context_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to update status for context {context_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to update status for context {context_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when updating status of context {context_id}: {str(ex)}") from ex

    def delete_context(self, context_id):
        """
        Delete an agent context from the MongoDB collection

        :param context_id:      The ID of the context to delete

        :return:                The ID of the deleted context
        :raises:                OperationFailure, PyMongoError, RuntimeError
        """
        try:
            deleted = self.collection.delete_one({'_id': context_id})

            if deleted.deleted_count:
                logging.info(f"Deleted context {context_id}")
                return context_id

            raise RuntimeError(f"Could not delete context {context_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to delete context {context_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to delete context {context_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when deleting context {context_id}: {str(ex)}") from ex

    def get_contexts(self, status=None, agent_id=None):
        """
        Retrieve agent contexts from the database.
        Optionally filter by status or agent_id.

        :param status:   The status to filter for (optional)
        :param agent_id: The agent_id to filter for (optional)

        :return:         List containing all matching contexts
        :raises:         OperationFailure, PyMongoError, RuntimeError
        """
        try:
            query = {}
            if status:
                query["status"] = status
            if agent_id:
                query["agent_id"] = agent_id
                
            results = list(self.collection.find(query))
            return results

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to retrieve contexts: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to retrieve contexts: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when retrieving contexts: {str(ex)}") from ex

    def get_context_by_id(self, context_id):
        """
        Retrieve a specific context by its ID

        :param context_id:  The ID of the context to retrieve

        :return:            Dictionary representation of the context
        :raises:            OperationFailure, PyMongoError, RuntimeError
        """
        try:
            if not context_id:
                raise ValueError("Context ID must be provided")

            result = self.collection.find_one({'_id': context_id})

            if result:
                return result

            raise RuntimeError(f"No context found with ID {context_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to retrieve context {context_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to retrieve context {context_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when retrieving context {context_id}: {str(ex)}") from ex

    def get_context_by_agent_id(self, agent_id):
        """
        Retrieve a context by agent_id

        :param agent_id:    The agent_id to search for

        :return:            Dictionary representation of the context
        :raises:            OperationFailure, PyMongoError, RuntimeError
        """
        try:
            if not agent_id:
                raise ValueError("Agent ID must be provided")

            result = self.collection.find_one({'agent_id': agent_id})

            if result:
                return result

            raise RuntimeError(f"No context found for agent_id {agent_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to retrieve context for agent_id {agent_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to retrieve context for agent_id {agent_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when retrieving context for agent_id {agent_id}: {str(ex)}") from ex

    def append_to_context(self, context_id, key, value):
        """
        Append or update a specific key in the context field

        :param context_id:  The ID of the context to update
        :param key:         The key to update in the context field
        :param value:       The value to set for the key

        :return:            The ID of the updated context
        :raises:            OperationFailure, PyMongoError, RuntimeError
        """
        try:
            result = self.collection.update_one(
                {'_id': context_id},
                {
                    '$set': {
                        f'context.{key}': value,
                        'updated_at': datetime.datetime.utcnow()
                    }
                }
            )

            if result.modified_count:
                logging.info(f"Updated context {context_id}, added/modified key: {key}")
                return context_id

            raise RuntimeError(f"Could not update context {context_id}")

        except OperationFailure as ex:
            raise OperationFailure(f"Failed to update context {context_id}: {str(ex)}") from ex

        except PyMongoError as ex:
            raise PyMongoError(f"Failed to update context {context_id}: {str(ex)}") from ex

        except Exception as ex:
            raise RuntimeError(f"Unknown failure when updating context {context_id}: {str(ex)}") from ex

    def __del__(self):
        """
        Close the connection to the MongoDB cluster

        :raises:     RuntimeError
        """
        try:
            self.cluster.close()

        except Exception as ex:
            raise RuntimeError(f"Error closing MongoDB connection: {str(ex)}") from ex
