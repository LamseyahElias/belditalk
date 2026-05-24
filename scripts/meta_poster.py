#!/usr/bin/env python3
"""
Belditalk Meta (Facebook/Instagram) Auto-Posting Script
Posts scheduled content to the BeldiTalk Facebook Page.

Usage:
    python3 meta_poster.py --post "Your post text here"
    python3 meta_poster.py --post "Post text" --image /path/to/image.jpg
    python3 meta_poster.py --schedule "Post text" --time "2026-06-01T10:00:00"
    
Requires META_PAGE_TOKEN in ~/.hermes/.env
Page ID: 1047439671795847
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime, timezone
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

PAGE_TOKEN = os.environ.get("META_PAGE_TOKEN", "")
PAGE_ID = "1047439671795847"
GRAPH_API = f"https://graph.facebook.com/v21.0/{PAGE_ID}"

if not PAGE_TOKEN:
    print("ERROR: META_PAGE_TOKEN not found in environment")
    sys.exit(1)


def post_text(message: str, scheduled_time: str = None) -> dict:
    """Post text to the Facebook page."""
    data = {
        "message": message,
        "access_token": PAGE_TOKEN,
    }
    if scheduled_time:
        # Convert to Unix timestamp
        dt = datetime.fromisoformat(scheduled_time)
        data["scheduled_publish_time"] = str(int(dt.timestamp()))
        data["published"] = "false"
    
    cmd = ["curl", "-s", "-X", "POST", f"{GRAPH_API}/feed"]
    for k, v in data.items():
        cmd.extend(["-F", f"{k}={v}"])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def post_with_image(message: str, image_path: str) -> dict:
    """Post text with an image to the Facebook page."""
    cmd = [
        "curl", "-s", "-X", "POST", f"{GRAPH_API}/photos",
        "-F", f"message={message}",
        "-F", f"source=@{image_path}",
        "-F", f"access_token={PAGE_TOKEN}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def post_link(message: str, link: str) -> dict:
    """Post text with a link preview."""
    cmd = [
        "curl", "-s", "-X", "POST", f"{GRAPH_API}/feed",
        "-F", f"message={message}",
        "-F", f"link={link}",
        "-F", f"access_token={PAGE_TOKEN}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def get_page_posts(limit: int = 5) -> dict:
    """Get recent posts from the page."""
    cmd = [
        "curl", "-s",
        f"{GRAPH_API}/feed?fields=message,created_time,id&limit={limit}&access_token={PAGE_TOKEN}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Belditalk Meta Auto-Poster")
    parser.add_argument("--post", type=str, help="Text to post")
    parser.add_argument("--image", type=str, help="Image path to attach")
    parser.add_argument("--link", type=str, help="Link to attach")
    parser.add_argument("--schedule", type=str, help="Schedule post text")
    parser.add_argument("--time", type=str, help="Schedule time (ISO format)")
    parser.add_argument("--list", action="store_true", help="List recent posts")
    
    args = parser.parse_args()
    
    if args.list:
        posts = get_page_posts()
        for p in posts.get("data", []):
            msg = p.get("message", "(no text)")[:80]
            print(f"[{p['created_time']}] {msg}")
    elif args.schedule and args.time:
        result = post_text(args.schedule, args.time)
        print(f"Scheduled: {json.dumps(result, indent=2)}")
    elif args.post and args.image:
        result = post_with_image(args.post, args.image)
        print(f"Posted with image: {json.dumps(result, indent=2)}")
    elif args.post and args.link:
        result = post_link(args.post, args.link)
        print(f"Posted with link: {json.dumps(result, indent=2)}")
    elif args.post:
        result = post_text(args.post)
        print(f"Posted: {json.dumps(result, indent=2)}")
    else:
        parser.print_help()
