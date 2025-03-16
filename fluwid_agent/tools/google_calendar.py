"""
Tool for interacting with Google Calendar
"""
from datetime import datetime
from livekit.agents import llm
from typing import Annotated, Optional
from fluwid_agent.tools.base import BaseTool

class GoogleCalendarTool(BaseTool):
    """
    Tool for reading and writing to Google Calendar
    """
    def __init__(self) -> None:
        super().__init__()
        # In a real implementation, you would initialize the Google Calendar API client here
        # For now, we'll create a mock implementation
        self._calendar = {}
        
    @llm.ai_callable(description="Check availability for a time slot")
    def check_availability(
        self,
        date: Annotated[
            str,
            llm.TypeInfo(description="The date to check in format YYYY-MM-DD")
        ],
        start_time: Annotated[
            str,
            llm.TypeInfo(description="The start time in format HH:MM (24-hour)")
        ],
        end_time: Annotated[
            str,
            llm.TypeInfo(description="The end time in format HH:MM (24-hour)")
        ]
    ) -> str:
        """
        Checks if a time slot is available in the calendar
        """
        try:
            # Parse date and times
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_datetime = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")
            
            # In a real implementation, you would query the Google Calendar API here
            # For now, we'll use our mock calendar
            day_key = date_obj.isoformat()
            if day_key not in self._calendar:
                return f"The time slot on {date} from {start_time} to {end_time} is available."
                
            # Check for conflicts
            for event in self._calendar.get(day_key, []):
                event_start = datetime.fromisoformat(event['start'])
                event_end = datetime.fromisoformat(event['end'])
                
                # Check if there's an overlap
                if (start_datetime < event_end and end_datetime > event_start):
                    return f"The time slot on {date} from {start_time} to {end_time} conflicts with event: {event['title']}"
            
            return f"The time slot on {date} from {start_time} to {end_time} is available."
            
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."
        except Exception as e:
            return f"Error checking availability: {str(e)}"
    
    @llm.ai_callable(description="Schedule an appointment")
    def schedule_appointment(
        self,
        title: Annotated[
            str,
            llm.TypeInfo(description="The title of the appointment")
        ],
        date: Annotated[
            str,
            llm.TypeInfo(description="The date for the appointment in format YYYY-MM-DD")
        ],
        start_time: Annotated[
            str,
            llm.TypeInfo(description="The start time in format HH:MM (24-hour)")
        ],
        end_time: Annotated[
            str,
            llm.TypeInfo(description="The end time in format HH:MM (24-hour)")
        ],
        customer_name: Annotated[
            str,
            llm.TypeInfo(description="The name of the customer")
        ],
        description: Annotated[
            Optional[str],
            llm.TypeInfo(description="Optional description for the appointment")
        ] = None
    ) -> str:
        """
        Schedules a new appointment in the calendar
        """
        try:
            # Parse date and times
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_datetime = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")
            
            # Check availability first
            availability = self.check_availability(date, start_time, end_time)
            if "conflicts" in availability:
                return f"Cannot schedule appointment: {availability}"
            
            # Create the event
            event = {
                'title': title,
                'start': start_datetime.isoformat(),
                'end': end_datetime.isoformat(),
                'customer': customer_name,
                'description': description or ""
            }
            
            # Add to our mock calendar
            day_key = date_obj.isoformat()
            if day_key not in self._calendar:
                self._calendar[day_key] = []
            self._calendar[day_key].append(event)
            
            # In a real implementation, you would use the Google Calendar API to create the event
            
            return f"Appointment scheduled: {title} with {customer_name} on {date} from {start_time} to {end_time}"
            
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."
        except Exception as e:
            return f"Error scheduling appointment: {str(e)}"
    
    @llm.ai_callable(description="List appointments for a date")
    def list_appointments(
        self,
        date: Annotated[
            str,
            llm.TypeInfo(description="The date to list appointments for in format YYYY-MM-DD")
        ]
    ) -> str:
        """
        Lists all appointments scheduled for a specific date
        """
        try:
            # Parse date
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            day_key = date_obj.isoformat()
            
            if day_key not in self._calendar or not self._calendar[day_key]:
                return f"No appointments scheduled for {date}."
            
            # Format the appointments
            appointments = self._calendar[day_key]
            result = f"Appointments for {date}:\n"
            
            for i, event in enumerate(appointments):
                start_time = datetime.fromisoformat(event['start']).strftime("%H:%M")
                end_time = datetime.fromisoformat(event['end']).strftime("%H:%M")
                result += f"{i+1}. {start_time}-{end_time}: {event['title']} with {event['customer']}\n"
                
            return result
            
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
        except Exception as e:
            return f"Error listing appointments: {str(e)}" 