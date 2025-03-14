"""
Keywords for Deepgram speech-to-text recognition in Bulgarian.

Keywords are specific words that Deepgram will prioritize recognizing.
These are typically important words that might be frequently used in your application context.
"""

# Keywords are specific words that Deepgram should prioritize recognizing
# The format is a list of strings
KEYWORDS = [
    # Common command words
    "старт", "спри", "продължи", "назад", "напред",
    "помощ", "изход", "затвори", "отвори", "покажи",
    
    # Numbers
    "нула", "едно", "две", "три", "четири", "пет", 
    "шест", "седем", "осем", "девет", "десет",
    
    # Time-related words
    "днес", "утре", "вчера", "сега", "после",
    "сутрин", "вечер", "нощ", "ден", "седмица",
    
    # Question words
    "кой", "какво", "кога", "къде", "защо", "как",
    
    # Common affirmative/negative responses
    "да", "не", "може би", "разбира се", "никога",
    
    # Application-specific terms (customize these for your use case)
    "съобщение", "имейл", "календар", "среща", "напомняне",
    "задача", "проект", "документ", "файл", "папка"
]
