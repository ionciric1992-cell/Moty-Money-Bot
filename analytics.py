import csv
import os
from datetime import datetime

DATA_FILE = "performance.csv"


def record_video(username, topic, views, likes, comments, shares):
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "date",
                "username",
                "topic",
                "views",
                "likes",
                "comments",
                "shares",
                "engagement"
            ])

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
            round(engagement, 2)
        ])


def analyze_performance():
    if not os.path.exists(DATA_FILE):
        print("No performance data yet.")
        return

    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No records found.")
        return

    print("\n--- Moty Analytics ---")

    for row in rows:
        print(
            f"{row['username']} | "
            f"{row['topic']} | "
            f"{row['views']} views | "
            f"{row['engagement']}% engagement"
        )


if __name__ == "__main__":
    analyze_performance()
