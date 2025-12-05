# Reddit Reaper - Claude Instructions

## Project Overview

Reddit Reaper is a Python CLI tool that retrieves a user's own Reddit posts and comments for personal analysis and repurposing. The tool uses PRAW (Python Reddit API Wrapper) to fetch content via OAuth authentication.

## Architecture

### Module Structure

- `src/reddit_reaper/`
  - `cli.py` - Command-line interface using argparse
  - `client.py` - Reddit API client wrapper (PRAW)
  - `config.py` - Configuration loading from config.json
  - `retriever.py` - Content retrieval logic
  - `formatter.py` - Output formatting (JSON, stats)

### Key Technologies

- **Python**: 3.9+
- **PRAW**: Reddit API wrapper for OAuth authentication and data retrieval
- **Package Manager**: uv for dependency management
- **Installation**: Editable install via `uv tool install --editable .`

## Configuration

- Configuration stored in `config.json` (not version controlled)
- Example configuration in `config.example.json`
- Requires Reddit API credentials (client_id, client_secret, username)
- Users create credentials at https://www.reddit.com/prefs/apps

## Development Guidelines

### Python Standards

- Use Python 3.9+ features
- Follow PEP 8 style guidelines
- Always work inside a venv (important user preference)
- Use uv for dependency management

### Code Organization

- Keep modules focused on single responsibilities
- CLI in cli.py, API logic in client.py, data processing in retriever.py
- Configuration logic isolated in config.py
- Output formatting separated in formatter.py

### Security Considerations

- Never commit API credentials
- config.json is gitignored
- OAuth-based authentication only
- Rate limiting handled by PRAW

## Features

### Current Functionality

- Retrieve user's submissions (posts) and comments
- Filter by content type (posts only, comments only, or both)
- Limit number of results
- Include engagement statistics (by subreddit, top content)
- JSON output format
- Rate-limit aware via PRAW

### CLI Options

- `--limit N` - Limit number of items retrieved
- `--type [posts|comments|all]` - Filter content type
- `--stats` - Include statistics summary
- `--output FILE` - Save to specific JSON file

## Output Format

Structured JSON with three main sections:

1. `submissions` - Array of post objects
2. `comments` - Array of comment objects
3. `summary` - Statistics (total counts, by_subreddit breakdown)

Each item includes:

- Content (title/selftext for posts, body for comments)
- Metadata (subreddit, score, timestamps)
- Engagement (num_comments, awards)
- Links (permalink to original)

## Testing and Running

```bash
# Install in development mode
uv sync
uv tool install --editable .

# Run the tool
reddit-reaper --limit 10 --stats
```

## Version Control

- Main branch: `claude/reddit-data-retrieval-tool-011ZuKrso6mFbvJdyeMs2uWF`
- Using git worktrees for development
- .gitignore includes config.json, Python artifacts, .DS_Store

## Purpose and Use Cases

This tool is for personal content retrieval, not content scraping or third-party data collection. Use cases:

- Repurposing your own writing on other platforms
- Analyzing which subreddits give you engagement
- Identifying high-performing content worth expanding
- Exporting personal Reddit history

## Important Notes

- Rate limiting handled automatically by PRAW
- OAuth authentication ensures secure access
- Only retrieves authenticated user's own content
- JSON output designed for further processing by other tools
