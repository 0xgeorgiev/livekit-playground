"""
Tools for the assistant to use
"""
from typing import Annotated
from livekit.agents import llm

class AssistantTool(llm.FunctionContext):
    """
    Tool for the assistant to use
    """
    def __init__(self) -> None:
        super().__init__()
        # Initialize mock user database with plain text data
        self._users_db = {
            "Teodor Georgiev": """
                Personal Information:
                - Name: Teodor Georgiev
                - Age: 25
                - Language: Bulgarian

                Visit History:
                - First Session: January 15, 2024
                - Second Session: January 22, 2024
                - Coach: Stefan
                - Session Duration: 15 minutes each

                Initial Symptoms:
                - Lower back pain
                - Poor posture from desk work
                - Decreased mobility
                - Early signs of bone density concerns

                Session Details:
                First Visit (15/01/2024):
                - Completed full circuit assessment
                - Initial measurements recorded
                - Showed enthusiasm about the technology
                - Expressed concerns about time commitment

                Second Visit (22/01/2024):
                - Reported slight improvement in back stiffness
                - Completed full session with increased confidence
                - Mentioned some muscle soreness after first session
                - Asked questions about long-term results

                Communication History:
                - Welcome email sent: January 16, 2024
                - Follow-up call: January 24, 2024
                - Last contact: February 1, 2024
                - Status: No response to recent follow-up

                Additional Notes:
                - Found Osteostrong through Facebook
                - Primary motivation: Back pain relief
                - Price sensitivity: Moderate
            """,
            "Maria Santos": """
                Personal Information:
                - Name: Maria Santos
                - Age: 42
                - Language: English

                Visit History:
                - First Session: February 1, 2024
                - Second Session: February 8, 2024
                - Coach: Elena
                - Session Duration: 15 minutes each

                Initial Symptoms:
                - Osteoporosis concerns
                - Joint stiffness
                - Balance issues

                Session Details:
                First Visit (01/02/2024):
                - Initial assessment completed
                - Very motivated about bone health improvement
                - Previous experience with physical therapy
                - Clear goals set for strength improvement

                Second Visit (08/02/2024):
                - Adapted well to all machines
                - Reported feeling more energetic
                - Interested in nutrition advice
                - Scheduled next session

                Communication History:
                - Welcome email sent: February 2, 2024
                - Follow-up call: February 10, 2024
                - Last contact: February 15, 2024
                - Status: Active member, responsive

                Additional Notes:
                - Found Osteostrong through doctor referral
                - Primary motivation: Bone density improvement
                - Price sensitivity: Low
            """
        }

    @llm.ai_callable(description="Get user data by name")
    def get_user_data(
        self,
        name: Annotated[
            str, 
            llm.TypeInfo(description="The full name of the user written in English to fetch data for")
        ]
    ) -> str:
        """
        Returns information about the specified user in plain text format.
        """
        print(f"Fetching user data for {name}")
        return self._users_db.get(name, "User not found")

