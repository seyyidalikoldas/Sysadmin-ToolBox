from inactive_users import find_inactive_accounts

def main():
    print("[*] Testing inactive user detection...")
    sample_users = [
        {"username": "jdoe", "last_login": "2024-01-15T09:00:00"},
        {"username": "admin_backup", "last_login": None},
        {"username": "active_dev", "last_login": "2025-03-01T14:30:00"}
    ]
    res = find_inactive_accounts(sample_users, inactive_days=90)
    print("Found stale accounts:", res)

if __name__ == "__main__":
    main()
