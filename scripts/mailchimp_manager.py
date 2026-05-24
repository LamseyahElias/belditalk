#!/usr/bin/env python3
"""
Belditalk Mailchimp Subscriber Manager
Add subscribers, tag them, and check list stats.

Usage:
    python3 mailchimp_manager.py --add email@example.com --fname "John"
    python3 mailchimp_manager.py --add email@example.com --tag "website-signup"
    python3 mailchimp_manager.py --stats
    python3 mailchimp_manager.py --recent 10
"""

import os
import sys
import json
import hashlib
import argparse
import subprocess
from pathlib import Path

# Load env
env_path = Path.home() / ".hermes" / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, _, val = line.partition('=')
            val = val.strip().strip("'\"")
            os.environ.setdefault(key.strip(), val)

API_KEY = os.environ.get("MAILCHIMP_API_KEY", "")
DC = API_KEY.split("-")[-1] if "-" in API_KEY else "us10"
LIST_ID = "7317b7b5dd"
BASE = f"https://{DC}.api.mailchimp.com/3.0"

if not API_KEY:
    print("ERROR: MAILCHIMP_API_KEY not found")
    sys.exit(1)


def mc_curl(method, endpoint, data=None):
    cmd = ["curl", "-s", "-X", method, "-u", f"x:{API_KEY}",
           "-H", "Content-Type: application/json", f"{BASE}{endpoint}"]
    if data:
        cmd.extend(["-d", json.dumps(data)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout) if result.stdout else {}


def add_subscriber(email, fname="", lname="", tags=None):
    data = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {}
    }
    if fname: data["merge_fields"]["FNAME"] = fname
    if lname: data["merge_fields"]["LNAME"] = lname
    if tags: data["tags"] = [{"name": t, "status": "active"} for t in tags]
    
    return mc_curl("POST", f"/lists/{LIST_ID}/members", data)


def get_stats():
    data = mc_curl("GET", f"/lists/{LIST_ID}")
    stats = data.get("stats", {})
    return {
        "name": data.get("name"),
        "members": stats.get("member_count", 0),
        "unsubscribes": stats.get("unsubscribe_count", 0),
        "open_rate": stats.get("open_rate", 0),
        "click_rate": stats.get("click_rate", 0),
    }


def get_recent(count=10):
    data = mc_curl("GET", f"/lists/{LIST_ID}/members?count={count}&sort_field=timestamp_opt&sort_dir=DESC")
    return [{"email": m["email_address"], "name": m.get("merge_fields", {}).get("FNAME", ""), 
             "joined": m["timestamp_opt"]} for m in data.get("members", [])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Belditalk Mailchimp Manager")
    parser.add_argument("--add", type=str, help="Email to add")
    parser.add_argument("--fname", type=str, default="", help="First name")
    parser.add_argument("--lname", type=str, default="", help="Last name")
    parser.add_argument("--tag", type=str, help="Tag to apply")
    parser.add_argument("--stats", action="store_true", help="Show list stats")
    parser.add_argument("--recent", type=int, help="Show N recent subscribers")
    
    args = parser.parse_args()
    
    if args.stats:
        s = get_stats()
        print(f"List: {s['name']}")
        print(f"Members: {s['members']}")
        print(f"Unsubscribes: {s['unsubscribes']}")
        print(f"Open rate: {s['open_rate']:.1%}")
        print(f"Click rate: {s['click_rate']:.1%}")
    elif args.recent:
        for sub in get_recent(args.recent):
            print(f"{sub['joined']} | {sub['email']} | {sub['name']}")
    elif args.add:
        tags = [args.tag] if args.tag else ["website-signup"]
        result = add_subscriber(args.add, args.fname, args.lname, tags)
        if "id" in result:
            print(f"Added: {args.add}")
        else:
            print(f"Error: {result.get('detail', result)}")
    else:
        parser.print_help()
