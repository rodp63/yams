import json
import os

from itemadapter import ItemAdapter

import yams.info as info
from yams.utils import get_bar


class YamsPipeline(object):
    def open_spider(self, spider):
        filename = os.environ.get(info.news["env"]["output"]["value"])
        self.out_type = "stdout"
        self.bar = get_bar()
        if filename:
            self.out_type = "file"
            self.filename = filename
            self.data = []

    def close_spider(self, spider):
        if self.out_type == "file":
            with open(self.filename, "w", encoding="utf-8") as fd:
                json.dump(self.data, fd, indent=2, ensure_ascii=False)

    def process_item(self, item, spider):
        out_item = ItemAdapter(item).asdict()
        if self.out_type == "file":
            self.data.append(out_item)
        else:
            print(json.dumps(out_item, ensure_ascii=False))
        self.bar()
        return item
