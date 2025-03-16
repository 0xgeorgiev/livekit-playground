"""
Tool for accessing customer data from MongoDB
"""
from typing import Annotated
from livekit.agents import llm
from fluwid_agent.tools.base import BaseTool
from fluwid_agent.mongodb.customers_collection import CustomersDatabase

class CustomerDataTool(BaseTool):
    """
    Tool for accessing and managing customer information from MongoDB
    """
    def __init__(self) -> None:
        super().__init__()
        self.db = CustomersDatabase()

    @llm.ai_callable(description="Get customer data by name")
    def get_customer_data(
        self,
        name: Annotated[
            str, 
            llm.TypeInfo(description="The full name of the customer to fetch data for")
        ]
    ) -> str:
        """
        Returns information about the specified customer in plain text format.
        
        Retrieves customer data from MongoDB and formats it as a readable text.
        """
        try:
            # Query MongoDB for customer data
            customer = self.db.collection.find_one({"name": name})
            
            if not customer:
                return f"Customer not found: {name}"
            
            # Format customer data as text
            customer_info = f"""
                Personal Information:
                - Name: {customer.get('name', 'Unknown')}
                - Age: {customer.get('age', 'Unknown')}
                - Language: {customer.get('language', 'Unknown')}

                Visit History:
                {self._format_visits(customer.get('visits', []))}

                Initial Symptoms:
                {self._format_list(customer.get('symptoms', []))}

                Communication History:
                {self._format_communications(customer.get('communications', []))}

                Additional Notes:
                {self._format_list(customer.get('notes', []))}
            """
            
            return customer_info.strip()
            
        except Exception as e:
            return f"Error retrieving customer data: {str(e)}"
    
    @llm.ai_callable(description="Add a note to customer record")
    def add_customer_note(
        self,
        name: Annotated[
            str,
            llm.TypeInfo(description="The full name of the customer")
        ],
        note: Annotated[
            str,
            llm.TypeInfo(description="The note to add to the customer record")
        ]
    ) -> str:
        """
        Adds a note to the customer's record in the database
        """
        try:
            # Add timestamp to note
            from datetime import datetime
            timestamped_note = {
                "text": note,
                "timestamp": datetime.now()
            }
            
            # Update customer record
            result = self.db.collection.update_one(
                {"name": name},
                {"$push": {"notes": timestamped_note}}
            )
            
            if result.matched_count == 0:
                return f"Customer not found: {name}"
                
            return f"Note added to {name}'s record"
            
        except Exception as e:
            return f"Error adding note: {str(e)}"
    
    def _format_visits(self, visits):
        """Format visit history as text"""
        if not visits:
            return "- No visits recorded"
            
        visit_text = ""
        for i, visit in enumerate(visits):
            visit_text += f"Visit {i+1} ({visit.get('date', 'Unknown date')}):\n"
            visit_text += f"- Coach: {visit.get('coach', 'Unknown')}\n"
            visit_text += f"- Duration: {visit.get('duration', 'Unknown')} minutes\n"
            
            if 'notes' in visit:
                visit_text += "- Notes:\n"
                for note in visit['notes']:
                    visit_text += f"  * {note}\n"
                    
        return visit_text
    
    def _format_communications(self, communications):
        """Format communication history as text"""
        if not communications:
            return "- No communications recorded"
            
        comm_text = ""
        for comm in communications:
            comm_text += f"- {comm.get('type', 'Contact')}: {comm.get('date', 'Unknown date')}"
            if 'status' in comm:
                comm_text += f", Status: {comm['status']}"
            comm_text += "\n"
            
        return comm_text
    
    def _format_list(self, items):
        """Format a list of items as text"""
        if not items:
            return "- None recorded"
            
        return "\n".join(f"- {item}" for item in items) 
