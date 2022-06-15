BOT_NAME = "yams"
SPIDER_MODULES = ["yams.spiders"]
NEWSPIDER_MODULE = "yams.spiders"

ROBOTSTXT_OBEY = False
LOG_LEVEL = "ERROR"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
)

ITEM_PIPELINES = {
    "yams.pipelines.YamsPipeline": 300,
}
