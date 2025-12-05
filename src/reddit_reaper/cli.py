"""Command-line interface for Reddit Reaper"""
import argparse
import sys
from pathlib import Path

from .config import load_config
from .client import RedditClient
from .retriever import ContentRetriever
from .formatter import format_json, add_summary_stats


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Retrieve your own Reddit content for repurposing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  reddit-reaper                           # Get all your content
  reddit-reaper --limit 100               # Get last 100 of each type
  reddit-reaper --type posts              # Only submissions
  reddit-reaper --type comments           # Only comments
  reddit-reaper --output my_reddit.json   # Save to file
  reddit-reaper --stats                   # Include summary statistics
        """
    )

    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to config file (default: config.json)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of items to retrieve (default: all)"
    )

    parser.add_argument(
        "--type",
        choices=["posts", "comments", "all"],
        default="all",
        help="Type of content to retrieve (default: all)"
    )

    parser.add_argument(
        "--output", "-o",
        help="Output file (default: stdout)"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Include summary statistics"
    )

    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print JSON (default: true)"
    )

    args = parser.parse_args()

    try:
        # Load config
        print("Loading configuration...", file=sys.stderr)
        config = load_config(args.config)

        # Initialize client
        print("Connecting to Reddit...", file=sys.stderr)
        client = RedditClient(config)
        client.test_connection()

        # Retrieve content
        retriever = ContentRetriever(client)

        if args.type == "posts":
            print(f"Retrieving submissions...", file=sys.stderr)
            data = {"submissions": retriever.get_submissions(args.limit)}
        elif args.type == "comments":
            print(f"Retrieving comments...", file=sys.stderr)
            data = {"comments": retriever.get_comments(args.limit)}
        else:
            print(f"Retrieving all content...", file=sys.stderr)
            data = retriever.get_all_content(args.limit)

        # Add stats if requested
        if args.stats:
            data = add_summary_stats(data)

        # Format output
        output = format_json(data, pretty=args.pretty)

        # Write output
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(output)
            print(f"Output written to {args.output}", file=sys.stderr)
        else:
            print(output)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted.", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
