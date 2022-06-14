import json
import os

import redis
from itemadapter import ItemAdapter

ARC_LISTS = os.getenv("ARC_LISTS", "arc").split(",")


class YamsPipeline(object):
    redis_client = redis.Redis(
        host=os.getenv("YAMS_REDIS_HOST", "localhost"),
        port=int(os.getenv("YAMS_REDIS_PORT", 6379)),
    )

    def redis_publish(
        self,
        rdb,
        item,
        item_project,
        item_media_type,
        item_subproject=None,
    ):
        item_project = item_project.replace(".", "-")
        item_subproject = item_subproject.replace(".", "-") if item_subproject else None

        item_source = (
            item_project if not item_subproject else f"{item_project}.{item_subproject}"
        )

        for arc_list in ARC_LISTS:
            routing_key = f"{arc_list}.{item_source}.{item_media_type}"
            rdb.lpush(routing_key, item)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["_id"] = item["url"]
        adapter["source"] = spider.name
        adapter["media_type"] = spider.media_type

        self.redis_publish(
            self.redis_client,
            item=json.dumps(adapter.asdict(), ensure_ascii=False, sort_keys=True),
            item_project=spider.name,
            item_media_type=spider.media_type,
        )

        return item
