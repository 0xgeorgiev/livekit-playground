"""
Models for the assistant
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class PersonalInfo:
    name: str
    age: int
    language: str

@dataclass
class VisitHistory:
    first_session: datetime
    second_session: datetime
    coach: str
    session_duration: str

@dataclass
class SessionDetails:
    date: datetime
    notes: List[str]

@dataclass
class CommunicationHistory:
    welcome_email_date: datetime
    follow_up_call_date: datetime
    last_contact_date: datetime
    status: str

@dataclass
class ClientProfile:
    personal_info: PersonalInfo
    visit_history: VisitHistory
    initial_symptoms: List[str]
    session_details: List[SessionDetails]
    communication_history: CommunicationHistory
    additional_notes: List[str]
    