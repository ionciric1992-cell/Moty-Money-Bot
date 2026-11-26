
from datetime import datetime

from config import (
    BOT_NAME,
    TIKTOK_USERNAME,
    IDEAS_PER_DAY,
    SCRIPTS_PER_DAY,
    REPORT_INTERVAL_DAYS,
)

import ideas
import scripts
import analytics
import accounts


def show_daily_plan():
    print("=" * 40)
    print(BOT_NAME)
    print(f"Account: {TIKTOK_USERNAME}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 40)

    print(f"\nIdeas today: {IDEAS_PER_DAY}")
    print(f"Scripts today: {SCRIPTS_PER_DAY}")

    print("\nTasks:")
    print("- Analyze content performance")
    print("- Find new content ideas")
    print("- Prepare video scripts")
    print("- Review TikTok accounts")
    print(f"- Weekly report every {REPORT_INTERVAL_DAYS} days")

    print("\nAutomatic posting: DISABLED")


def show_ideas():
    print("\n--- Content Ideas ---")
    for i, idea in enumerate(ideas.generate_ideas(IDEAS_PER_DAY), 1):
        print(f"{i}. {idea}")


def create_script():
    topic = input("Enter video topic: ").strip()

    if not topic:
        topic = "Motivation"

    scripts.print_script(topic)


def show_analytics():
    analytics.analyze_performance()


def show_accounts():
    accounts.list_accounts()


def main_menu():
    while True:
        print("\n" + "=" * 40)
        print(BOT_NAME)
        print("MOTY MONEY BOT")
        print("=" * 40)

        print("1. Daily plan")
        print("2. Generate content ideas")
        print("3. Create video script")
        print("4. Analyze performance")
        print("5. Show TikTok accounts")
        print("0. Exit")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            show_daily_plan()

        elif choice == "2":
            show_ideas()

        elif choice == "3":
            create_script()

        elif choice == "4":
            show_analytics()

        elif choice == "5":
            show_accounts()

        elif choice == "0":
            print("Moty Money Bot stopped.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()
