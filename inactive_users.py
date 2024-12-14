from datetime import datetime, timedelta

def find_inactive_accounts(user_records, inactive_days=60):
    cutoff = datetime.now() - timedelta(days=inactive_days)
    inactive = []
    
    for u in user_records:
        last_login = u.get("last_login")
        if not last_login:
            inactive.append({"username": u.get("username"), "reason": "never_logged_in"})
            continue
            
        if isinstance(last_login, str):
            try:
                last_login = datetime.fromisoformat(last_login)
            except Exception:
                continue
                
        if last_login < cutoff:
            inactive.append({
                "username": u.get("username"),
                "last_seen": str(last_login.date()),
                "days_idle": (datetime.now() - last_login).days
            })
            
    return inactive
