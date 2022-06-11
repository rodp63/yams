# Yet Another Media Scraper
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

```bash
$ yams
Usage: yams [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  info   Display useful information
  start  Start a crawling process
```

## Installation

```bash
$ python setup.py install
```

## Deployment 

```bash
$ make build-image
$ make upload-image
```

## Formatting 

```bash
$ make lint
```
