from datetime import date, datetime, timedelta

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

_bar = None


def str_to_date(str_date):
    return datetime.strptime(str_date, "%Y-%m-%d").date()


def date_to_str(datetime_date):
    return datetime_date.strftime("%Y-%m-%d")


def date_range(start_date, end_date, inclusive=False):
    start_date = str_to_date(start_date)
    end_date = str_to_date(end_date)
    for n in range(int((end_date - start_date).days) + int(inclusive)):
        yield start_date + timedelta(n)


def today(to_str=False):
    return str(date.today()) if to_str else date.today()


def days_ago(days, to_str=False):
    d_ago = date.today() - timedelta(days=days)
    return str(d_ago) if to_str else d_ago


def get_crawler():
    settings = Settings()
    settings.setmodule("yams.settings")
    return CrawlerProcess(settings)


def init_bar(bar):
    global _bar
    _bar = bar


def remove_bar():
    global _bar
    _bar = None


def get_bar():
    return _bar
