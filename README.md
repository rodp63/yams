# Yet Another Media Scraper
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This project aims to provide a seamless access to news and media information.
A simple Python scraper to collect posts from the most popular Peruvian news websites (for now):

- [x] El Correo: [https://diariocorreo.pe/](https://diariocorreo.pe/).
- [x] El Comercio: [https://elcomercio.pe/](https://elcomercio.pe/).
- [x] Perú 21: [https://peru21.pe/](https://peru21.pe/).
- [ ] Gestión: [https://gestion.pe/](https://gestion.pe/).
- [ ] La República: [https://larepublica.pe/](https://larepublica.pe/).
- [ ] CNN News: [https://edition.cnn.com/](https://edition.cnn.com/).
- [ ] BBC News: [https://www.bbc.com/](https://www.bbc.com/).

## Installation

Standard installation via `pip`:
```zsh
$ pip install yams
```

Or, you can install it manually:
```zsh
$ git clone https://github.com/rodp63/yams.git
$ cd yams
$ pip install .
```

## Quickstart

Let's start by getting all the posts from _El Comercio_ containing the keyword `"peru"` in the last month (by default).

```zsh
$ yams start newspaper elcomercio -k peru
```

We can define the date range to extract the information by using the `-s` and `-t` options.
Let's get all the post from _Perú 21_ containing the keyword `"congreso"` from the last half of the year 2023.

```zsh
$ yams start newspaper peru21 -k congreso -s '2023-07-01' -t '2023-12-31'
```

As you may notice, the output is printed on the screen by default.
Generally we want to save the information in a file, we can store the output in a JSON file by using the `-o` option.
Let's get all the post from _El Correo_ containing the keyword `"futbol"` from the last month and save the output in the file `futbol_posts.json`.

```zsh
$ yams start newspaper diariocorreo -k futbol -o futbol_posts
```

We have been using a single keyword, however, we can use as many as we want.
Let's get all the post from _El Comercio_ containing the words `"messi"` or `"ronaldo"` from the last month.

```zsh
$ yams start newspaper elcomercio -k messi -k ronaldo
```

Although we can use keywords with more than one word (e.g. `-k "chipi chapa"`), it is not recommended since the keywords are stemmed and splited into clean words.
But sometimes we want to search for exact terms, considering accents or Letter case.
In such situations we can use the `--exact-match` option.
Let's get all the post from _Perú 21_ containing the exact keyword `"Luis Advíncula"` from the last month.

```zsh
$ yams start newspaper peru21 -k "Luis Advíncula" --exact-match
```

The task parameters are always displayed at the beginning of the process,
This way we are always aware of the details of the search that is about to start.
We can also define parameters by using environment variables, very useful when we want to execute YAMS within containers for example.
We can check them using the `info` command.

```zsh
$ yams info
...
  Environment:
    YAMS_NEWSPAPER: 
    YAMS_NEWSPAPER_SINCE: 
    YAMS_NEWSPAPER_TO: 
    YAMS_NEWSPAPER_KEYWORDS:
    YAMS_NEWSPAPER_OUTPUT:
```

Let's get all the post from _El Correo_ containing the keyword `"ambiente"` from the last month using environment variables.

```zsh
$ export YAMS_NEWSPAPER="diariocorreo"
$ export YAMS_NEWSPAPER_KEYWORDS="ambiente"
$ yams start newspaper
```

Please refer to the `Dockerfile` and `manifest.yaml` files to run YAMS within Docker and Kubernetes.