# learn-scrapy
:spider: Free Scrapy Tutorials To Learn Web Scraping

## Source Code

Source code developed in https://scrapinghub.com/learn-scrapy

## Installation

Use the package manager [poetry](https://python-poetry.org) to install dependencies.

`poetry install`

## Usage

```bash
# quotes
poetry run scrapy runspider quotes.py -o quotes.json
# authors
poetry run scrapy runspider authors.py -o authors.json
# quotes scroll
poetry run scrapy runspider quotes_scroll.py -o quotes_scroll.json
# login
poetry run scrapy runspider login.py -o login.json
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
