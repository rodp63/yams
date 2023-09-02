import json
import os

from itemadapter import ItemAdapter

import yams.info as info


class YamsPipeline(object):
    def open_spider(self, spider):
        filename = os.environ.get(info.news["env"]["output"]["value"])
        self.out_type = "stdout"
        if filename:
            self.out_type = "file"
            self.filename = filename
            self.data = []

    def close_spider(self, spider):
        if self.out_type == "file":
            with open(self.filename, "w", encoding="utf-8") as fd:
                json.dump(self.data, fd, indent=2)

    def process_item(self, item, spider):
        out_item = ItemAdapter(item).asdict()
        if self.out_type == "file":
            self.data.append(out_item)
        else:
            print(out_item)
        return item
