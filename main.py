from datetime import datetime
from config import (
    BOT_NAME,
    TIKTOK_USERNAME,
    IDEAS_PER_DAY,
    SCRIPTS_PER_DAY,
    REPORT_INTERVAL_DAYS,
)

def show_daily_plan():
    print("=" * 40)
    print(BOT_NAME)
    print(f"Account: {TIKTOK_USERNAME}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 40)

    print(f"\nToday's content ideas: {IDEAS_PER_DAY}")
    print(f"Scripts to prepare: {SCRIPTS_PER_DAY}")

    print("\nTasks:")
    print("- Analyze content performance")
    print("- Find new content ideas")
    print("- Prepare video scripts")
    print("- Suggest monetization opportunities")
    print(f"- Weekly report every {REPORT_INTERVAL_DAYS} days")

    print("\nAutomatic posting: DISABLED")
    print("Bot is ready for the next development stage.")

if __name__ == "__main__":
    show_daily_plan()
