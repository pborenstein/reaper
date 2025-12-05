"""Reddit API client for retrieving user data"""
import requests
import time


class RedditClient:
    """Client for fetching public Reddit user data"""

    BASE_URL = "https://www.reddit.com"
    USER_AGENT = "reddit-reaper/0.1.0"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.USER_AGENT})

    def get_user_info(self, username):
        """
        Fetch user information from Reddit's public JSON endpoint

        Args:
            username: Reddit username to look up

        Returns:
            dict: User data including account info and recent posts

        Raises:
            ValueError: If user not found or API error
        """
        # Get user about data
        about_url = f"{self.BASE_URL}/user/{username}/about.json"
        about_response = self._make_request(about_url)

        if "error" in about_response:
            raise ValueError(f"User '{username}' not found")

        user_data = about_response.get("data", {})

        # Get user's recent posts/comments
        overview_url = f"{self.BASE_URL}/user/{username}.json"
        overview_response = self._make_request(overview_url)

        posts = []
        if "data" in overview_response:
            children = overview_response["data"].get("children", [])
            for child in children:
                post_data = child.get("data", {})
                posts.append({
                    "type": child.get("kind"),
                    "subreddit": post_data.get("subreddit"),
                    "title": post_data.get("title") or post_data.get("link_title"),
                    "body": post_data.get("selftext") or post_data.get("body"),
                    "score": post_data.get("score"),
                    "created_utc": post_data.get("created_utc"),
                    "permalink": post_data.get("permalink"),
                })

        return {
            "username": user_data.get("name"),
            "id": user_data.get("id"),
            "created_utc": user_data.get("created_utc"),
            "link_karma": user_data.get("link_karma"),
            "comment_karma": user_data.get("comment_karma"),
            "total_karma": user_data.get("total_karma"),
            "is_gold": user_data.get("is_gold"),
            "is_mod": user_data.get("is_mod"),
            "verified": user_data.get("verified"),
            "icon_img": user_data.get("icon_img"),
            "recent_activity": posts[:10],  # Limit to 10 most recent
        }

    def _make_request(self, url):
        """Make HTTP request with error handling and rate limiting"""
        try:
            time.sleep(1)  # Basic rate limiting
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {"error": 404}
            raise ValueError(f"HTTP error: {e}")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Request failed: {e}")
