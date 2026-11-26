import csv
import os
from datetime import datetime

DATA_FILE = "performance.csv"

HEADERS = [
    "date",
    "username",
    "topic",
    "views",
    "likes",
    "comments",
    "shares",
    "engagement",
]


def record_video(username, topic, views, likes, comments, shares):
    if not isinstance(views, int) or views < 0:
        raise ValueError("Views must be a non-negative integer")

    if any(not isinstance(value, int) or value < 0
           for value in (likes, comments, shares)):
        raise ValueError("Engagement metrics must be non-negative integers")

    file_exists = os.path.exists(DATA_FILE)
    file_empty = file_exists and os.path.getsize(DATA_FILE) == 0

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or file_empty:
            writer.writerow(HEADERS)

        engagement = 0
        if views > 0:
            engagement = (likes + comments + shares) / views * 100

        writer.writerow([
            datetime.now().isoformat(),
            username,
            topic,
            views,
            likes,
            comments,
            shares,
            round(engagement, 2),
        ])


def load_performance():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def analyze_performance():
    rows = load_performance()

    if not rows:
        print("No performance data yet.")
        return []

    print("\n--- Moty Analytics ---")

    for row in rows:
        print(
            f"{row.get('username', 'Unknown')} | "
            f"{row.get('topic', 'Unknown')} | "
            f"{row.get('views', 0)} views | "
            f"{row.get('engagement', 0)}% engagement"
        )

    return rows


if __name__ == "__main__":
    analyze_performance()
