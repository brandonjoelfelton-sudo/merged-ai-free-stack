#!/usr/bin/env python3
"""trend_scan.py — free 'Grok Bot': Google Trends + Hacker News + Reddit. Stdlib only."""
import json, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

UA = {"User-Agent": "merged-ai-free-stack/1.0"}

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def google_trends(geo="US", limit=20):
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={geo}"
    root = ET.fromstring(fetch(url))
    out = []
    for item in root.iter("item"):
        out.append({"trend": item.findtext("title", ""),
                    "approx_traffic": item.findtext("{https://trends.google.com/trends/trendingsearches/daily}approx_traffic", "")})
        if len(out) >= limit:
            break
    return out

def hacker_news(limit=15):
    data = json.loads(fetch(f"https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage={limit}"))
    return [{"title": h.get("title"), "url": h.get("url"), "points": h.get("points")} for h in data.get("hits", [])]

def reddit_hot(limit=15):
    data = json.loads(fetch(f"https://www.reddit.com/r/all/hot.json?limit={limit}"))
    return [{"title": c["data"].get("title"), "subreddit": c["data"].get("subreddit"),
             "score": c["data"].get("score"),
             "url": "https://www.reddit.com" + c["data"].get("permalink", "")}
            for c in data.get("data", {}).get("children", []) if not c["data"].get("stickied")]

def main():
    digest = {"scanned_at": datetime.now(timezone.utc).isoformat(),
              "google_trends": [], "hacker_news": [], "reddit_hot": [], "errors": []}
    for name, fn in (("google_trends", google_trends), ("hacker_news", hacker_news), ("reddit_hot", reddit_hot)):
        try:
            digest[name] = fn()
        except Exception as e:
            digest["errors"].append(f"{name}: {e}")
    text = json.dumps(digest, indent=2)
    print(text)
    if "--webhook" in sys.argv:
        url = sys.argv[sys.argv.index("--webhook") + 1]
        req = urllib.request.Request(url, data=text.encode(),
                                     headers={**UA, "Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"POSTed to webhook -> HTTP {r.status}", file=sys.stderr)

if __name__ == "__main__":
    main()
