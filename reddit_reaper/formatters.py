"""Output formatters for Reddit user data"""
import json
from datetime import datetime


def format_json(data):
    """Format user data as pretty JSON"""
    return json.dumps(data, indent=2, ensure_ascii=False)


def format_markdown(data):
    """Format user data as Markdown"""
    username = data.get("username", "Unknown")
    created = data.get("created_utc")
    created_date = datetime.fromtimestamp(created).strftime("%Y-%m-%d") if created else "Unknown"

    md = f"# Reddit User: {username}\n\n"
    md += "## Account Information\n\n"
    md += f"- **Username**: u/{username}\n"
    md += f"- **Account Created**: {created_date}\n"
    md += f"- **Link Karma**: {data.get('link_karma', 0):,}\n"
    md += f"- **Comment Karma**: {data.get('comment_karma', 0):,}\n"
    md += f"- **Total Karma**: {data.get('total_karma', 0):,}\n"
    md += f"- **Reddit Gold**: {'Yes' if data.get('is_gold') else 'No'}\n"
    md += f"- **Moderator**: {'Yes' if data.get('is_mod') else 'No'}\n"
    md += f"- **Verified**: {'Yes' if data.get('verified') else 'No'}\n"

    recent = data.get("recent_activity", [])
    if recent:
        md += "\n## Recent Activity\n\n"
        for i, post in enumerate(recent, 1):
            post_type = "Comment" if post["type"] == "t1" else "Post"
            title = post.get("title") or "(comment)"
            subreddit = post.get("subreddit", "unknown")
            score = post.get("score", 0)

            md += f"### {i}. {post_type} in r/{subreddit}\n"
            if post.get("title"):
                md += f"**{title}**\n\n"
            if post.get("body"):
                body = post["body"][:200]
                if len(post["body"]) > 200:
                    body += "..."
                md += f"{body}\n\n"
            md += f"- Score: {score}\n"
            if post.get("permalink"):
                md += f"- Link: https://reddit.com{post['permalink']}\n"
            md += "\n"

    return md
