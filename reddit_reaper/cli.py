"""Command-line interface for Reddit Reaper"""
import argparse
import sys
from .client import RedditClient
from .formatters import format_json, format_markdown


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Retrieve Reddit user information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  reddit-reaper -u pborenstein --format json
  reddit-reaper -u pborenstein --format markdown
        """
    )

    parser.add_argument(
        "-u", "--user",
        required=True,
        help="Reddit username to look up"
    )

    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        client = RedditClient()
        print(f"Fetching data for u/{args.user}...", file=sys.stderr)
        user_data = client.get_user_info(args.user)

        if args.format == "json":
            output = format_json(user_data)
        else:
            output = format_markdown(user_data)

        print(output)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
