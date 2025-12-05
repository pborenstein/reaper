# Reddit Reaper - Project Plan

## Goal
Retrieve your own Reddit writing (posts and comments) to make it easier to repurpose. Include engagement statistics to help determine what content is worth repurposing.

## Use Case
Personal content mining tool - analyze your Reddit history to:
- Extract your writing for repurposing elsewhere
- Identify which subreddits give you the most engagement
- Find high-performing content by topic/subject
- Export data for analysis

## Technical Approach

### Authentication
- Use PRAW (Python Reddit API Wrapper) with your personal OAuth token
- Store credentials in `config.json` (add to `.gitignore`)
- Provide `config.example.json` as template
- OAuth scopes needed: `identity`, `history`, `read`

### Data to Retrieve
1. **Posts (submissions)**
   - Title, selftext, url
   - Subreddit
   - Score (upvotes), upvote ratio
   - Number of comments
   - Created timestamp
   - Awards/gildings
   - Post flair

2. **Comments**
   - Body text
   - Parent post title/link
   - Subreddit
   - Score
   - Created timestamp
   - Context (what you were replying to)

3. **Engagement Stats**
   - By subreddit: total posts, avg score, total comments received
   - By time period: monthly/yearly trends
   - Top performers: highest scoring posts/comments
   - Subject analysis: word frequency in high-engagement content

### Output Format
- JSON structure (schema TBD after initial data exploration)
- Options:
  - `--output <file>` - save to file
  - stdout by default
  - `--pretty` - pretty-print JSON

### CLI Interface

```bash
# Basic usage - retrieve all your content
reddit-reaper

# Limit results
reddit-reaper --limit 100

# Filter by time
reddit-reaper --after 2024-01-01 --before 2024-12-31

# Only posts or only comments
reddit-reaper --type posts
reddit-reaper --type comments

# Specific subreddit
reddit-reaper --subreddit python

# Show stats
reddit-reaper --stats

# Export to file
reddit-reaper --output my_reddit_history.json
```

## Project Structure (following temoa conventions)

```
reaper/
├── docs/
│   └── REAPER_PLAN.md
├── src/
│   └── reddit_reaper/
│       ├── __init__.py
│       ├── cli.py          # argparse CLI interface
│       ├── client.py       # PRAW wrapper
│       ├── config.py       # Config loading
│       ├── retriever.py    # Data retrieval logic
│       ├── stats.py        # Engagement analysis
│       └── formatter.py    # JSON output formatting
├── tests/
│   └── test_*.py
├── .gitignore
├── config.example.json
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## Installation & Setup

Following temoa pattern:
```bash
git clone https://github.com/pborenstein/reaper
cd reaper

# Copy and configure OAuth credentials
cp config.example.json config.json
# Edit config.json with your Reddit app credentials

# Install dependencies and tool
uv sync
uv tool install --editable .

# Use globally
reddit-reaper --help
```

## Dependencies
- `praw` - Reddit API wrapper
- Python 3.9+ (for modern type hints)

## Configuration File Structure

`config.example.json`:
```json
{
  "reddit": {
    "client_id": "your_client_id_here",
    "client_secret": "your_client_secret_here",
    "user_agent": "reddit-reaper/0.1.0 by u/yourusername",
    "username": "yourusername"
  }
}
```

## Implementation Phases

### Phase 1: Basic Data Retrieval
- [ ] Project setup (pyproject.toml, uv)
- [ ] Config loading system
- [ ] PRAW client wrapper
- [ ] Basic CLI with argparse
- [ ] Retrieve posts and comments
- [ ] JSON output to stdout

### Phase 2: Filtering & Options
- [ ] Time-based filtering (--after, --before)
- [ ] Type filtering (--type posts/comments)
- [ ] Subreddit filtering
- [ ] Limit option
- [ ] Output to file

### Phase 3: Engagement Statistics
- [ ] Aggregate stats by subreddit
- [ ] Identify top-performing content
- [ ] Time-series analysis
- [ ] Subject/keyword analysis
- [ ] Stats output format

### Phase 4: Polish
- [ ] Error handling (rate limits, network errors)
- [ ] Progress indicators for large retrievals
- [ ] Caching to avoid re-fetching
- [ ] Documentation
- [ ] Tests

## Rate Limits & Considerations
- Reddit API: 100 queries/min for free tier
- PRAW handles rate limiting automatically
- For large histories, may need pagination
- Consider caching retrieved data

## Future Enhancements (Maybe)
- Markdown output format
- HTML export
- Search within your content
- Export to specific formats (Medium, blog posts, etc.)
- Sentiment analysis
- Thread reconstruction (full conversation context)

## Questions to Resolve During Implementation
1. What's the actual data structure from PRAW? (will inform JSON schema)
2. How far back does your history go? (affects pagination strategy)
3. Do we need deleted/removed content handling?
4. Should we include linked media (images, videos)?
5. Export edited history or just current version?

## References
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Reddit Data API Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)
- [Reddit API Rate Limits](https://support.reddithelp.com/hc/en-us/articles/16160319875092)
- [URS (existing tool)](https://github.com/JosephLai241/URS) - for comparison
