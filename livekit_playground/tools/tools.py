"""
Tools for the assistant to use
"""
from datetime import datetime
from typing import Optional, Annotated
from livekit.agents import llm
from livekit_playground.models.models import ClientProfile, PersonalInfo, VisitHistory, SessionDetails, CommunicationHistory


class AssistantTool(llm.FunctionContext):
    """
    Tool for the assistant to use
    """
    def __init__(self) -> None:
        super().__init__()
        # Initialize mock user database
        self._users_db = {
            "Teodor Georgiev": ClientProfile(
                personal_info=PersonalInfo(
                    name="Teodor Georgiev",
                    age=25,
                    language="Bulgarian"
                ),
                visit_history=VisitHistory(
                    first_session=datetime(2024, 1, 15),
                    second_session=datetime(2024, 1, 22),
                    coach="Stefan",
                    session_duration="15 minutes each"
                ),
                initial_symptoms=[
                    "Lower back pain",
                    "Poor posture from desk work",
                    "Decreased mobility",
                    "Early signs of bone density concerns"
                ],
                session_details=[
                    SessionDetails(
                        date=datetime(2024, 1, 15),
                        notes=[
                            "Completed full circuit assessment",
                            "Initial measurements recorded",
                            "Showed enthusiasm about the technology",
                            "Expressed concerns about time commitment"
                        ]
                    ),
                    SessionDetails(
                        date=datetime(2024, 1, 22),
                        notes=[
                            "Reported slight improvement in back stiffness",
                            "Completed full session with increased confidence",
                            "Mentioned some muscle soreness after first session",
                            "Asked questions about long-term results"
                        ]
                    )
                ],
                communication_history=CommunicationHistory(
                    welcome_email_date=datetime(2024, 1, 16),
                    follow_up_call_date=datetime(2024, 1, 24),
                    last_contact_date=datetime(2024, 2, 1),
                    status="No response to recent follow-up"
                ),
                additional_notes=[
                    "Found Osteostrong through Facebook",
                    "Primary motivation: Back pain relief",
                    "Price sensitivity: Moderate"
                ]
            ),
            "Maria Santos": ClientProfile(
                personal_info=PersonalInfo(
                    name="Maria Santos",
                    age=42,
                    language="English"
                ),
                visit_history=VisitHistory(
                    first_session=datetime(2024, 2, 1),
                    second_session=datetime(2024, 2, 8),
                    coach="Elena",
                    session_duration="15 minutes each"
                ),
                initial_symptoms=[
                    "Osteoporosis concerns",
                    "Joint stiffness",
                    "Balance issues"
                ],
                session_details=[
                    SessionDetails(
                        date=datetime(2024, 2, 1),
                        notes=[
                            "Initial assessment completed",
                            "Very motivated about bone health improvement",
                            "Previous experience with physical therapy",
                            "Clear goals set for strength improvement"
                        ]
                    ),
                    SessionDetails(
                        date=datetime(2024, 2, 8),
                        notes=[
                            "Adapted well to all machines",
                            "Reported feeling more energetic",
                            "Interested in nutrition advice",
                            "Scheduled next session"
                        ]
                    )
                ],
                communication_history=CommunicationHistory(
                    welcome_email_date=datetime(2024, 2, 2),
                    follow_up_call_date=datetime(2024, 2, 10),
                    last_contact_date=datetime(2024, 2, 15),
                    status="Active member, responsive"
                ),
                additional_notes=[
                    "Found Osteostrong through doctor referral",
                    "Primary motivation: Bone density improvement",
                    "Price sensitivity: Low"
                ]
            )
        }

    @llm.ai_callable(description="Get user data by name")
    def get_user_data(
        self,
        name: Annotated[
            str, 
            llm.TypeInfo(description="The full name of the user to fetch data for")
        ]
    ) -> Optional[ClientProfile]:
        """
        Returns structured information about the specified user including personal details, 
        visit history, symptoms, and communication history.
        """
        return self._users_db.get(name)

