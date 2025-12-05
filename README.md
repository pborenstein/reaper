# Reddit Reaper

A command-line tool to retrieve Reddit user information.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Get user info as JSON
reddit-reaper -u pborenstein --format json

# Get user info as Markdown
reddit-reaper -u pborenstein --format markdown
```

## Features

- Retrieves public Reddit user data
- Outputs in JSON or Markdown format
- No authentication required for public data

## Sources

- [Reddit Data API Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)
- [PRAW Documentation](https://praw.readthedocs.io/)
