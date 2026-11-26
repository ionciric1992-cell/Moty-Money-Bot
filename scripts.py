
import random

HOOKS = [
    "Stop scrolling for a second!",
    "Nobody tells you this!",
    "Here are 3 things you should know!",
    "This could change the way you think!",
    "Most people don't know this!",
    "Wait until you hear this!",
    "You might be making this mistake!",
    "Here is something worth remembering!",
]

BODY_TEMPLATES = [
    "Take a moment to think about how this applies to your everyday life.",
    "Small changes can make a bigger difference than you expect.",
    "Learning something new starts with curiosity and consistency.",
    "The best results often come from simple actions repeated daily.",
    "Don't ignore the little things. They can become important over time.",
]

CTAS = [
    "Follow for more!",
    "What do you think? Comment below!",
    "Save this video for later!",
    "Share this with someone who needs it!",
    "Follow Moty for the next video!",
]

def generate_script(topic="general"):
    hook = random.choice(HOOKS)
    body = random.choice(BODY_TEMPLATES)
    cta = random.choice(CTAS)

    script = {
        "topic": topic,
        "hook": hook,
        "body": body,
        "cta": cta,
    }

    return script

def print_script(topic="general"):
    script = generate_script(topic)

    print("=" * 40)
    print("MOTY VIDEO SCRIPT")
    print("=" * 40)
    print(f"Topic: {script['topic']}")
    print(f"\nHOOK:\n{script['hook']}")
    print(f"\nBODY:\n{script['body']}")
    print(f"\nCTA:\n{script['cta']}")
    print("=" * 40)

if __name__ == "__main__":
    print_script("Motivation")
