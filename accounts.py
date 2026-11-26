import json
import os

ACCOUNTS_FILE = "accounts.json"


def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return []

    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=2, ensure_ascii=False)


def add_account(username, niche, goal):
    accounts = load_accounts()

    account = {
        "username": username,
        "niche": niche,
        "goal": goal,
        "active": True
    }

    if any(a["username"] == username for a in accounts):
        print(f"Account already exists: {username}")
        return

    accounts.append(account)
    save_accounts(accounts)
    print(f"Account added: {username}")


def list_accounts():
    accounts = load_accounts()

    if not accounts:
        print("No TikTok accounts configured.")
        return

    print("\n--- Moty Accounts ---")

    for account in accounts:
        print(
            f"Username: {account['username']} | "
            f"Niche: {account['niche']} | "
            f"Goal: {account['goal']} | "
            f"Active: {account['active']}"
        )


if __name__ == "__main__":
    list_accounts()
