"""Data retrieval logic for Reddit content"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class ContentRetriever:
    """Retrieves Reddit posts and comments for a user"""

    def __init__(self, client):
        """
        Initialize retriever with Reddit client

        Args:
            client: RedditClient instance
        """
        self.client = client
        self.user = client.get_user()

    def get_submissions(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Retrieve user's submissions (posts)

        Args:
            limit: Maximum number of submissions to retrieve (None = all)

        Returns:
            List of submission data dicts
        """
        submissions = []

        for submission in self.user.submissions.new(limit=limit):
            submissions.append({
                "type": "submission",
                "id": submission.id,
                "title": submission.title,
                "selftext": submission.selftext,
                "url": submission.url,
                "subreddit": str(submission.subreddit),
                "score": submission.score,
                "upvote_ratio": submission.upvote_ratio,
                "num_comments": submission.num_comments,
                "created_utc": submission.created_utc,
                "created_datetime": datetime.fromtimestamp(submission.created_utc).isoformat(),
                "permalink": f"https://reddit.com{submission.permalink}",
                "is_self": submission.is_self,
                "link_flair_text": submission.link_flair_text,
                "gilded": submission.gilded,
                "total_awards_received": submission.total_awards_received,
            })

        return submissions

    def get_comments(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Retrieve user's comments

        Args:
            limit: Maximum number of comments to retrieve (None = all)

        Returns:
            List of comment data dicts
        """
        comments = []

        for comment in self.user.comments.new(limit=limit):
            # Get parent submission for context
            submission = comment.submission

            comments.append({
                "type": "comment",
                "id": comment.id,
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "score": comment.score,
                "created_utc": comment.created_utc,
                "created_datetime": datetime.fromtimestamp(comment.created_utc).isoformat(),
                "permalink": f"https://reddit.com{comment.permalink}",
                "gilded": comment.gilded,
                "total_awards_received": comment.total_awards_received,
                "parent_post_title": submission.title,
                "parent_post_url": f"https://reddit.com{submission.permalink}",
            })

        return comments

    def get_all_content(self, limit: Optional[int] = None) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve both submissions and comments

        Args:
            limit: Maximum number of each type to retrieve (None = all)

        Returns:
            Dict with 'submissions' and 'comments' keys
        """
        return {
            "submissions": self.get_submissions(limit),
            "comments": self.get_comments(limit),
        }
