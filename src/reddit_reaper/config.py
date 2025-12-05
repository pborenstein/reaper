"""Configuration loading for Reddit Reaper"""
import json
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from JSON file

    Args:
        config_path: Path to config file (default: config.json)

    Returns:
        Dict containing configuration

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config is invalid
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Config file not found: {config_path}\n"
            "Copy config.example.json to config.json and add your credentials"
        )

    try:
        with open(path) as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}")

    # Validate required fields
    if "reddit" not in config:
        raise ValueError("Config must contain 'reddit' section")

    reddit_config = config["reddit"]
    required_fields = ["client_id", "client_secret", "user_agent", "username"]

    missing = [f for f in required_fields if f not in reddit_config]
    if missing:
        raise ValueError(f"Missing required fields in reddit config: {', '.join(missing)}")

    return config
