"""
Pynexia Technology - Simple Rule-Based Chatbot
Beginner-friendly terminal chatbot using predefined rules and regex patterns.

Run:
    python chatbot.py
"""

import random
import re
from datetime import datetime


# 1. Intent patterns: each intent has keywords/patterns that identify user meaning.
INTENT_PATTERNS = {
    "greeting": [
        r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b"
    ],
    "goodbye": [
        r"\b(bye|goodbye|exit|quit|see you)\b"
    ],
    "thanks": [
        r"\b(thank you|thanks|thx)\b"
    ],
    "name": [
        r"\b(your name|who are you|what are you called)\b"
    ],
    "capabilities": [
        r"\b(what can you do|help|your features|how can you help)\b"
    ],
    "python": [
        r"\b(python|learn python)\b"
    ],
    "artificial_intelligence": [
        r"\b(artificial intelligence|what is ai|about ai)\b"
    ],
    "machine_learning": [
        r"\b(machine learning|what is ml)\b"
    ],
    "internship": [
        r"\b(internship|pynexia|training program)\b"
    ],
    "time": [
        r"\b(time|current time)\b"
    ],
    "date": [
        r"\b(date|today's date|today date)\b"
    ],
}


# 2. Intent mappings: predefined responses for each recognized intent.
RESPONSES = {
    "greeting": [
        "Hello! Welcome. How can I help you today?",
        "Hi there! What would you like to know?",
        "Hey! I'm happy to chat with you."
    ],
    "goodbye": [
        "Goodbye! Have a great day.",
        "See you soon. Keep learning!",
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help. Do you have another question?"
    ],
    "name": [
        "I'm PyBot, a simple rule-based chatbot built using Python."
    ],
    "capabilities": [
        "I can respond to greetings and answer basic questions about Python, AI, "
        "Machine Learning, and internships. You can also ask me for the date or time."
    ],
    "python": [
        "Python is a beginner-friendly programming language used in web development, "
        "automation, data science, and artificial intelligence."
    ],
    "artificial_intelligence": [
        "Artificial Intelligence (AI) is a field of computer science focused on "
        "building systems that perform tasks that usually require human intelligence."
    ],
    "machine_learning": [
        "Machine Learning is a branch of AI in which computers learn patterns from "
        "data and use those patterns to make predictions or decisions."
    ],
    "internship": [
        "An internship helps students gain practical experience and understand how "
        "technical skills are used in real-world projects."
    ],
}


def clean_text(user_text):
    """Convert text to lowercase and remove unnecessary punctuation/extra spaces."""
    cleaned = user_text.lower().strip()
    cleaned = re.sub(r"[^a-z0-9\s']", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def detect_intent(cleaned_text):
    """Return the first matching intent, or 'unknown' if no rule matches."""
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, cleaned_text):
                return intent
    return "unknown"


def generate_response(intent):
    """Generate a response using if-then rules and predefined intent mappings."""
    if intent in RESPONSES:
        return random.choice(RESPONSES[intent])

    if intent == "time":
        return "The current time is " + datetime.now().strftime("%I:%M %p") + "."

    if intent == "date":
        return "Today's date is " + datetime.now().strftime("%d %B %Y") + "."

    # Default response when no pattern matches.
    return (
        "I'm sorry, I don't understand that yet. "
        "Try asking about Python, AI, Machine Learning, or internships. "
        "You can type 'help' to see what I can do."
    )


def run_chatbot():
    """Run the continuous terminal conversation until the user exits."""
    print("=" * 58)
    print("                 PyBot - Rule-Based Chatbot")
    print("=" * 58)
    print("Hello! I'm PyBot. Type 'help' for topics or 'bye' to exit.")
    print("-" * 58)

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("PyBot: Please type a message so I can help.")
            continue

        cleaned = clean_text(user_input)
        intent = detect_intent(cleaned)
        response = generate_response(intent)

        # Save both sides of the conversation in memory for this session.
        conversation_history.append(
            {"user": user_input, "intent": intent, "bot": response}
        )

        print("PyBot:", response)

        if intent == "goodbye":
            print("-" * 58)
            print(f"Conversation ended. Messages exchanged: {len(conversation_history)}")
            print("Thank you for chatting with PyBot!")
            break


if __name__ == "__main__":
    run_chatbot()
