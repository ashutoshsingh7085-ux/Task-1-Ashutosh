"""
Rule-Based AI Chatbot
DecodeLabs | AI Industrial Training Kit | Project 1

Architecture (IPO model):
    INPUT   -> sanitize raw text (lowercase, trim, normalize)
    PROCESS -> dictionary lookup (O(1)) with a fallback
    OUTPUT  -> print response, loop until the exit command
"""

import re

BOT_NAME = "DecoBot"

# Knowledge base: key = sanitized user intent, value = bot response.
RESPONSES = {
    # Greetings
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's on your mind?",
    "good morning": "Good morning! Hope you have a productive day.",
    "good evening": "Good evening! How was your day?",
    # Small talk
    "how are you": "I'm just a bunch of if-else logic, but I'm running perfectly!",
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot built at DecodeLabs.",
    "who made you": "I was built by an AI intern at DecodeLabs as Project 1.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    # Domain knowledge
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "what is a rule based chatbot": (
        "A chatbot that replies using predefined rules instead of learning from data."
    ),
    "what is decodelabs": "DecodeLabs is the training platform behind this internship project.",
    "help": "Try: hello, how are you, what is ai, what is your name, or type 'exit' to quit.",
}

FALLBACK = "I do not understand. Type 'help' to see what I can answer."

# Clean-break commands that terminate the loop.
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}


def sanitize(raw_input: str) -> str:
    """Normalize raw input: lowercase, trim, collapse spaces, drop trailing punctuation."""
    text = raw_input.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]+$", "", text).strip()
    return text


def get_response(clean_input: str) -> str:
    """Atomic lookup + fallback using dict.get()."""
    return RESPONSES.get(clean_input, FALLBACK)


def main() -> None:
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}. Type 'help' for ideas or 'exit' to quit.")

    while True:  # The heartbeat: runs until the kill command
        try:
            raw_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Session closed. Goodbye!")
            break

        clean_input = sanitize(raw_input)

        if not clean_input:  # ignore empty input
            continue

        if clean_input in EXIT_COMMANDS:
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_response(clean_input)}")


if __name__ == "__main__":
    main()
