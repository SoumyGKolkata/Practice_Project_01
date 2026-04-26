def simple_ai_response(text: str) -> str:
    text = text.lower()

    if "hello" in text:
        return "Hi there! 👋"
    elif "how are you" in text:
        return "I'm just code, but I'm doing great!"
    else:
        return f"You said: {text}"