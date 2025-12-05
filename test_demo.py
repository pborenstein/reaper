"""Demo test with mock data to show functionality"""
from reddit_reaper.formatters import format_json, format_markdown

mock_data = {
    "username": "pborenstein",
    "id": "abc123",
    "created_utc": 1420070400,
    "link_karma": 15234,
    "comment_karma": 48756,
    "total_karma": 63990,
    "is_gold": False,
    "is_mod": True,
    "verified": True,
    "icon_img": "https://example.com/icon.png",
    "recent_activity": [
        {
            "type": "t1",
            "subreddit": "python",
            "title": None,
            "body": "This is a great point about async/await patterns!",
            "score": 45,
            "created_utc": 1704067200,
            "permalink": "/r/python/comments/xyz/comment/abc"
        },
        {
            "type": "t3",
            "subreddit": "programming",
            "title": "Best practices for CLI tools",
            "body": "I've been building CLI tools for years...",
            "score": 128,
            "created_utc": 1704153600,
            "permalink": "/r/programming/comments/123/best_practices"
        }
    ]
}

print("=" * 60)
print("JSON OUTPUT:")
print("=" * 60)
print(format_json(mock_data))

print("\n" + "=" * 60)
print("MARKDOWN OUTPUT:")
print("=" * 60)
print(format_markdown(mock_data))
