import random

CONTENT_CATEGORIES = [
    "Motivation",
    "Discipline",
    "Money mindset",
    "Success habits",
    "Personal growth",
    "Confidence",
    "Financial freedom",
    "Daily motivation",
    "Overcoming failure",
    "Productivity",
]

IDEAS = {
    "Motivation": [
        "Why you must never give up",
        "The power of starting today",
        "Stop waiting for the perfect moment",
        "Your future depends on today's actions",
        "How to keep going when life gets hard",
    ],
    "Discipline": [
        "Discipline beats motivation",
        "How to build strong habits",
        "Stop making excuses",
        "Small actions create big results",
        "Consistency is more important than perfection",
    ],
    "Money mindset": [
        "Why your mindset affects your money",
        "5 habits that keep people financially stuck",
        "Think long term, not short term",
        "Learn to control spending",
        "Building wealth starts with discipline",
    ],
    "Success habits": [
        "Morning habits that change your life",
        "How successful people use their time",
        "Stop wasting your energy",
        "The importance of consistency",
        "Focus on your goals every day",
    ],
    "Personal growth": [
        "Become better than yesterday",
        "Learn from your mistakes",
        "Why growth requires discomfort",
        "Stop comparing yourself to others",
        "Change begins with small steps",
    ],
    "Confidence": [
        "Believe in yourself when nobody else does",
        "How to stop doubting yourself",
        "Your value is not defined by others",
        "Build confidence through action",
        "Stop asking for permission to succeed",
    ],
    "Financial freedom": [
        "Financial freedom starts with discipline",
        "Why saving money matters",
        "Build skills before chasing money",
        "Think about your future",
        "Avoid unnecessary expenses",
    ],
    "Daily motivation": [
        "One message you need to hear today",
        "Never quit on yourself",
        "Your time is valuable",
        "Take action today",
        "You are stronger than your excuses",
    ],
    "Overcoming failure": [
        "Failure is part of success",
        "Learn to get back up",
        "Turn mistakes into lessons",
        "Don't let one failure define you",
        "Keep moving forward",
    ],
    "Productivity": [
        "Focus on one important task",
        "Stop procrastinating",
        "Protect your time",
        "How to work smarter",
        "Remove distractions from your life",
    ],
}


def generate_ideas(count=5, category=None):
    if count <= 0:
        return []

    if category and category in IDEAS:
        pool = IDEAS[category]
    else:
        pool = [idea for ideas in IDEAS.values() for idea in ideas]

    if count <= len(pool):
        return random.sample(pool, count)

    result = []
    while len(result) < count:
        result.extend(random.sample(pool, len(pool)))

    return result[:count]


def get_categories():
    return CONTENT_CATEGORIES.copy()


if __name__ == "__main__":
    for index, idea in enumerate(generate_ideas(10), 1):
        print(f"{index}. {idea}")
