import re
from collections import defaultdict

# parses auth.log / secure log to catch repeated failed attempts
FAILED_REGEX = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")

def parse_auth_log(log_path, threshold=5):
    attempts = defaultdict(int)
    users_targeted = defaultdict(set)
    
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                match = FAILED_REGEX.search(line)
                if match:
                    user, ip = match.groups()
                    attempts[ip] += 1
                    users_targeted[ip].add(user)
    except FileNotFoundError:
        print(f"Log file not found: {log_path}")
        return {}
        
    flagged_ips = {}
    for ip, count in attempts.items():
        if count >= threshold:
            flagged_ips[ip] = {
                "attempts": count,
                "targeted_usernames": list(users_targeted[ip])
            }
    return flagged_ips

if __name__ == "__main__":
    print("Auth log parser module ready.")
