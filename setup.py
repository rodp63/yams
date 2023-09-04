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
    install_requires=["nltk>=3.5", "scrapy>=2.6", "click>=8.1", "alive-progress>=2.4"],
)
