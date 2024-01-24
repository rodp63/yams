from setuptools import find_packages, setup

setup(
    name="cli-yams",
    version="1.1",
    license="MIT",
    description="Yet Another Media Scraper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yams=yams.commands.__main__:cli",
        ],
    },
    install_requires=["nltk>=3.5", "scrapy>=2.6", "click>=8.1", "alive-progress>=2.4"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
