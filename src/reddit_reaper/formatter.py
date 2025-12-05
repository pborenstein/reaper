"""Output formatting for Reddit data"""
import json
from typing import Dict, Any


def format_json(data: Dict[str, Any], pretty: bool = True) -> str:
    """
    Format data as JSON

    Args:
        data: Data to format
        pretty: Pretty-print with indentation (default: True)

    Returns:
        JSON string
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)


def add_summary_stats(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add summary statistics to retrieved data

    Args:
        data: Data dict with 'submissions' and 'comments'

    Returns:
        Data dict with added 'summary' section
    """
    submissions = data.get("submissions", [])
    comments = data.get("comments", [])

    # Aggregate by subreddit
    subreddit_stats = {}

    for sub in submissions:
        sr = sub["subreddit"]
        if sr not in subreddit_stats:
            subreddit_stats[sr] = {"posts": 0, "comments": 0, "total_score": 0}
        subreddit_stats[sr]["posts"] += 1
        subreddit_stats[sr]["total_score"] += sub["score"]

    for com in comments:
        sr = com["subreddit"]
        if sr not in subreddit_stats:
            subreddit_stats[sr] = {"posts": 0, "comments": 0, "total_score": 0}
        subreddit_stats[sr]["comments"] += 1
        subreddit_stats[sr]["total_score"] += com["score"]

    # Calculate averages
    for sr, stats in subreddit_stats.items():
        total_items = stats["posts"] + stats["comments"]
        stats["avg_score"] = stats["total_score"] / total_items if total_items > 0 else 0

    # Sort by total score
    sorted_subreddits = sorted(
        subreddit_stats.items(),
        key=lambda x: x[1]["total_score"],
        reverse=True
    )

    data["summary"] = {
        "total_submissions": len(submissions),
        "total_comments": len(comments),
        "total_items": len(submissions) + len(comments),
        "by_subreddit": dict(sorted_subreddits),
    }

    return data
