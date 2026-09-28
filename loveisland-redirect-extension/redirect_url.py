from __future__ import annotations

import argparse
import sys
import webbrowser
from urllib.parse import urlparse

REDIRECT_URL = "https://www.upsvr.gov.sk/ke.html?page_id=232158"
MATCH_TEXT = "loveisland"


def destination_for(url: str) -> str:
    """Return the redirect destination when the URL contains LoveIsland."""
    if MATCH_TEXT in url.casefold():
        return REDIRECT_URL
    return url


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Open a URL, redirecting LoveIsland URLs to the configured page."
    )
    parser.add_argument("url", help="The URL to open")
    args = parser.parse_args()

    parsed = urlparse(args.url)
    if parsed.scheme not in {"http", "https"}:
        parser.error("url must start with http:// or https://")

    destination = destination_for(args.url)
    print(f"Opening: {destination}")
    webbrowser.open(destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
