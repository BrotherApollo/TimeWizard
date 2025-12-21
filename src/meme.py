import random
import os

def random_meme():
    memes = os.listdir("assets/")
    choice = random.choice(memes)
    return f"assets/{choice}"


def spongify(s):
    return "".join([s[i].upper() if i % 2 else s[i].lower() for i in range(len(s))])

def get_reacts(message) -> list[str]:
    TIME_CARD_REACTS = {
        "bot": "🤖",
        "timecard": "📝",
        "sign": "✍️",
        "errors": "⚠️",
        "helpdesk": "🤯",
        "holiday": "🌴",
        "never": "🙃",
        "jimmy": "👨‍💼",
        "charge codes": "💳",
        "PTO": "🏖️",
        "payroll": "💰",
        "email": "📧",
        "week": "📅",
        "today": "📅",
        "check": "✅",
        "hours": "🕰️",
        "ASAP": "🏃",
    }
    reactions = []
    for keyword, emoji in TIME_CARD_REACTS.items():
        if keyword in message:
            reactions.append(emoji)
            
    return reactions