import json
import os
import re
import signal

import nltk
from scrapy import Request, Spider, signals

from yans.utils import date_range, today


class APISpider(Spider):
    media_type = "newspaper"

    since = None
    to = None
    keywords = None
    pagination_url = (
        "{}/pf/api/v3/content/fetch/story-feed-by-section-and-date-v2?query="
    )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(APISpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        return spider

    def item_scraped(self, item):
        os.kill(os.getpid(), signal.SIGUSR1)

    def get_tokens(self, text):
        text = re.sub(r"[(),:'\"\.!?]", "", text)
        tokens = [tk.lower() for tk in nltk.tokenize.word_tokenize(text)]
        tokens = [tk for tk in tokens if tk.isalpha()]

        accents = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
        for a in accents:
            tokens = [tk.replace(a[0], a[1]) for tk in tokens]

        tokens = [tk for tk in tokens if not tk in self.stop_words]
        tokens = [self.stemmer.stem(tk) for tk in tokens]
        return tokens

    def start_requests(self):
        if not self.keywords:
            self.logger.error("You must define the keywords, terminating...")
            return

        self.stemmer = nltk.stem.SnowballStemmer("spanish")
        self.stop_words = nltk.corpus.stopwords.words("spanish")
        self.keywords = [self.stemmer.stem(tk) for tk in self.keywords.split(",")]

        if not self.since:
            self.since = "2015-01-01"
        if not self.to:
            self.to = today(to_str=True)

        self.pagination_url = self.pagination_url.format(self.base_url)

        for day in date_range(self.since, self.to):
            query_data = {"date": str(day), "from": "0", "size": "100"}
            yield Request(
                self.pagination_url + json.dumps(query_data),
                callback=self.parse_pagination,
                meta={"day": str(day)},
            )

    def contains_keywords(self, text):
        tokens = self.get_tokens(text)
        for tk in self.keywords:
            if tk in tokens:
                return True
        return False

    def parse_post(self, response):
        def get_from_css(statement):
            chain = response.css(statement).getall()
            return " ".join(chain).strip()

        item = {}
        item["url"] = response.url
        item["date"] = response.meta.get("day")
        item["title"] = (
            get_from_css(".sht__title ::text")
            or get_from_css(".section-video__title ::text")
            or get_from_css(".story-header__news-title ::text")
        )
        item["summary"] = (
            get_from_css(".sht__summary ::text")
            or get_from_css(".section-video__subtitle ::text")
            or get_from_css(".story-header__news-summary ::text")
        )
        item["body"] = (
            get_from_css(".story-contents__font-paragraph ::text")
            or get_from_css(".sht__list ::text")
            or get_from_css(".section-video__list-items ::text")
            or get_from_css(".story-content__font--secondary ::text")
        )

        yield item

    def parse_pagination(self, response):
        parsed_response = json.loads(response.text)
        posts = parsed_response["content_elements"]

        for post in posts:
            header = post["headlines"]["basic"]
            subheader = post["subheadlines"]["basic"]
            if self.contains_keywords(header + " " + subheader):
                try:
                    url = self.base_url + post["websites"][self.name]["website_url"]
                except:
                    continue
                yield Request(
                    url,
                    callback=self.parse_post,
                    meta={"day": response.meta["day"]},
                )

        if "next" in parsed_response:
            query_data = {
                "date": response.meta["day"],
                "from": parsed_response["next"],
                "size": "100",
            }
            yield Request(
                self.pagination_url + json.dumps(query_data),
                callback=self.parse_pagination,
                meta={"day": response.meta["day"]},
            )


class CorreoSpider(APISpider):
    name = "diariocorreo"
    source = "diariocorreo"
    allowed_domains = ["diariocorreo.pe"]
    base_url = "https://diariocorreo.pe"


class ElComercioSpider(APISpider):
    name = "elcomercio"
    source = "elcomercio"
    allowed_domains = ["elcomercio.pe"]
    base_url = "https://elcomercio.pe"


class Peu21Spider(APISpider):
    name = "peru21"
    source = "peru21"
    allowed_domains = ["peru21.pe"]
    base_url = "https://peru21.pe"
