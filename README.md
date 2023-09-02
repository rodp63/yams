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

# Examples

```bash
$ yams start newspaper --help 
Usage: yams start newspaper [OPTIONS] SOURCE

Options:
  -k, --keyword TEXT      Set one keyword for post retrieval  [required]
  -o, --output FILE       Save output to json FILE instead of stdout
  -s, --since [%Y-%m-%d]  Set the lower date of the posts to retrieve
  -t, --to [%Y-%m-%d]     Set the upper date of the posts to retrieve
  --exact-match           Look for the exact match of the keywords
  -h, --help              Show this message and exit.

# Get all the posts containing the word 'peru' in the last month (by default).
$ yams start newspaper elcomercio -k peru
# Get all the post containing the exact word 'congreso' between two dates and save it in a file.
$ yams start newspaper elcomercio -k congreso -s '2023-01-01' -t '2023-06-30' -o output.json --exact-match
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
