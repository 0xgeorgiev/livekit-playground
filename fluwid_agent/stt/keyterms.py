"""
Keyterms for Deepgram speech-to-text recognition in Bulgarian.

Keyterms are phrases or terms with associated weights that Deepgram will prioritize recognizing.
Higher weights (0-1) indicate higher priority for recognition.
"""

# Keyterms are phrases with weights that Deepgram should prioritize recognizing
# The format is a dictionary where keys are terms and values are weights (0-1)
KEYTERMS = {
    # Greeting phrases
    "здравей": 0.8,
    "добро утро": 0.8,
    "добър ден": 0.8,
    "добър вечер": 0.8,
    "как си": 0.7,
    
    # Command phrases
    "моля помогни ми": 0.9,
    "имам въпрос": 0.9,
    "искам да": 0.8,
    "можеш ли да": 0.8,
    "трябва да": 0.7,
    
    # Navigation phrases
    "върни се назад": 0.8,
    "отиди на": 0.8,
    "покажи ми": 0.9,
    "отвори това": 0.8,
    "затвори това": 0.8,
    
    # Confirmation phrases
    "да, разбира се": 0.7,
    "не, благодаря": 0.7,
    "съгласен съм": 0.6,
    "не съм съгласен": 0.6,
    
    # Time-related phrases
    "в колко часа": 0.7,
    "след колко време": 0.7,
    "кога ще": 0.7,
    
    # Application-specific phrases (customize these for your use case)
    "създай ново съобщение": 0.9,
    "изпрати имейл до": 0.9,
    "насрочи среща за": 0.9,
    "добави в календара": 0.9,
    "създай напомняне за": 0.9,
    "запази този файл": 0.8,
    "отвори последния документ": 0.8
}
