
import random

CONTENT_CATEGORIES = [
    "Funny and relatable moments",
    "Motivation and inspiration",
    "Curiosity and surprising facts",
    "Short storytelling",
    "Tips and useful tricks",
    "Behind the scenes",
    "Questions for the audience",
    "Trending topics",
    "Mistakes people make",
    "Before and after",
    "Top 3 things",
    "Myth vs reality",
    "Things nobody tells you",
    "A short personal story",
    "Audience challenge",
]

HOOKS = [
    "Stop scrolling if you...",
    "Nobody talks about this...",
    "3 things you should know...",
    "I wish I knew this earlier...",
    "This might surprise you...",
    "Most people make this mistake...",
    "Watch until the end...",
    "Here is something interesting...",
    "Did you know?",
    "The truth about...",
]

def generate_ideas(count=5):
    ideas = []

    for i in range(count):
        category = random.choice(CONTENT_CATEGORIES)
        hook = random.choice(HOOKS)

        idea = f"{hook} | Topic: {category}"
        ideas.append(idea)

    return ideas

if __name__ == "__main__":
    print("Moty Money Bot - Content Ideas")
    print("=" * 35)

    for i, idea in enumerate(generate_ideas(5), 1):
        print(f"{i}. {idea}")
