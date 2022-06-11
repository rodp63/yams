from setuptools import find_packages, setup

setup(
    name="yams",
    version="0.1",
    description="Yet Another Media Scraper",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yams=yams.commands.__main__:cli",
        ],
    },
)
