def analyze_sentiment(text: str) -> str:
    if "angry" in text.lower() or "not working" in text.lower():
        return "Negative"
    return "Neutral"

def classify_priority(text: str) -> str:
    urgent_keywords = ["immediately", "critical", "urgent", "cannot access"]
    if any(word in text.lower() for word in urgent_keywords):
        return "Urgent"
    return "Not Urgent"
