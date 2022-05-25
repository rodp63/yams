from setuptools import setup, find_packages

setup(
    name="yans",
    version="0.1",
    description="Yet Another Newspaper Scraper",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yans=yans.__main__:cli",
        ],
    },
)
