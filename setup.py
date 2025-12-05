from setuptools import setup, find_packages

setup(
    name="reddit-reaper",
    version="0.1.0",
    description="CLI tool to retrieve Reddit user information",
    author="pborenstein",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "reddit-reaper=reddit_reaper.cli:main",
        ],
    },
)
