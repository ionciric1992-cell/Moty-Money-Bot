import random

HOOKS = [
    "Stop scrolling. This message is for you.",
    "Nobody tells you this about success.",
    "If you want to change your life, listen.",
    "The biggest mistake people make is this.",
    "Read this if you feel stuck in life.",
    "Your future self will thank you for this.",
    "Here is a truth you need to hear today.",
    "Stop waiting for the perfect moment.",
]

BODIES = [
    "Success does not happen overnight. Small actions repeated every day create powerful results. Focus on progress, not perfection.",
    "Discipline means doing what needs to be done even when motivation disappears. Your habits shape your future.",
    "You do not need everyone's approval. You need a clear goal, patience and the courage to keep moving forward.",
    "Failure is not the end. Every mistake can teach you something that helps you become stronger and smarter.",
    "Protect your time, focus on your goals and stop wasting energy on things that do not help you grow.",
    "Your financial future depends on the decisions you make today. Learn, save, improve your skills and think long term.",
]

CTAS = [
    "Follow for daily motivation.",
    "Save this video and remember it.",
    "Share this with someone who needs it.",
    "Comment START if you are ready to change.",
    "Follow and take the next step today.",
    "Save this message for later.",
]

HASHTAGS = [
    "#motivation",
    "#mindset",
    "#discipline",
    "#success",
    "#selfgrowth",
    "#money",
    "#inspiration",
    "#motymoney",
]


def generate_script(topic="Motivation"):
    topic = topic.strip() or "Motivation"

    hook = random.choice(HOOKS)
    body = random.choice(BODIES)
    cta = random.choice(CTAS)

    hashtags = random.sample(HASHTAGS, 5)

    return {
        "topic": topic,
        "hook": hook,
        "body": body,
        "cta": cta,
        "hashtags": hashtags,
        "duration_seconds": 20,
    }


def print_script(topic="Motivation"):
    result = generate_script(topic)

    print("\n--- Moty Video Script ---")
    print(f"Topic: {result['topic']}")
    print(f"Duration: {result['duration_seconds']} seconds")
    print(f"\nHOOK:\n{result['hook']}")
    print(f"\nBODY:\n{result['body']}")
    print(f"\nCTA:\n{result['cta']}")
    print("\nHASHTAGS:")
    print(" ".join(result["hashtags"]))

    return result


if __name__ == "__main__":
    print_script("Motivation")
