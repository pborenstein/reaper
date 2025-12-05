"""PRAW client wrapper for Reddit API"""
import praw
from typing import Dict, Any


class RedditClient:
    """Wrapper around PRAW for authenticated Reddit access"""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize Reddit client with OAuth credentials

        Args:
            config: Configuration dict with reddit credentials
        """
        reddit_config = config["reddit"]

        self.reddit = praw.Reddit(
            client_id=reddit_config["client_id"],
            client_secret=reddit_config["client_secret"],
            user_agent=reddit_config["user_agent"],
            username=reddit_config["username"],
        )

        self.username = reddit_config["username"]

    def get_user(self):
        """Get the authenticated user's redditor object"""
        return self.reddit.redditor(self.username)

    def test_connection(self) -> bool:
        """
        Test if credentials are valid

        Returns:
            True if connection successful

        Raises:
            Exception if authentication fails
        """
        try:
            # Try to access user info
            user = self.get_user()
            _ = user.id  # Force API call
            return True
        except Exception as e:
            raise Exception(f"Authentication failed: {e}")
