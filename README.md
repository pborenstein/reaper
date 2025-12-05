# Reddit Reaper

A command-line tool to retrieve your own Reddit content for repurposing.

## Purpose

Retrieve your Reddit posts and comments to:
- Repurpose your writing elsewhere
- Analyze which subreddits give you the most engagement
- Identify high-performing content worth expanding
- Export your Reddit history as JSON

## Installation

```bash
# Clone repository
git clone https://github.com/pborenstein/reaper
cd reaper

# Set up configuration
cp config.example.json config.json
# Edit config.json with your Reddit API credentials

# Install with uv
uv sync
uv tool install --editable .
```

## Configuration

Create a Reddit app at https://www.reddit.com/prefs/apps to get credentials:

1. Click "create app" or "create another app"
2. Choose "script" type
3. Use `http://localhost:8080` as redirect URI
4. Copy your `client_id` and `client_secret`

Edit `config.json`:
```json
{
  "reddit": {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "user_agent": "reddit-reaper/0.1.0 by u/your_username",
    "username": "your_username"
  }
}
```

## Usage

```bash
# Get all your content
reddit-reaper

# Limit results
reddit-reaper --limit 100

# Only posts or only comments
reddit-reaper --type posts
reddit-reaper --type comments

# Include engagement statistics
reddit-reaper --stats

# Save to file
reddit-reaper --output my_reddit_history.json

# Combine options
reddit-reaper --limit 50 --stats --output recent.json
```

## Features

- Retrieves all your Reddit posts and comments via OAuth
- Includes engagement metrics (scores, awards, comment counts)
- Optional statistics: activity by subreddit, top content
- JSON output (easy to process with other tools)
- Rate-limit aware (uses PRAW)

## Output Format

JSON structure:
```json
{
  "submissions": [
    {
      "type": "submission",
      "title": "Post title",
      "selftext": "Post body...",
      "subreddit": "python",
      "score": 123,
      "num_comments": 45,
      "created_datetime": "2024-01-15T12:34:56",
      "permalink": "https://reddit.com/r/python/...",
      ...
    }
  ],
  "comments": [
    {
      "type": "comment",
      "body": "Comment text...",
      "subreddit": "programming",
      "score": 67,
      "parent_post_title": "The post you commented on",
      "created_datetime": "2024-01-16T08:22:11",
      ...
    }
  ],
  "summary": {
    "total_submissions": 42,
    "total_comments": 156,
    "by_subreddit": { ... }
  }
}
```

## License

MIT
