import json
import os

from itemadapter import ItemAdapter

import yams.info as info


class YamsPipeline(object):
    def open_spider(self, spider):
        filename = os.environ.get(info.news["env"]["output"]["value"])
        self.out_type = "stdout"
        if filename:
            self.outfile = open(filename, "w")
            self.out_type = "file"

    def close_spider(self, spider):
        if self.out_type == "file":
            self.outfile.close()

    def process_item(self, item, spider):
        out_item = json.dumps(ItemAdapter(item).asdict(), indent=2)
        if self.out_type == "file":
            self.file.write(out_item + "\n")
        else:
            print(out_item)
        return item
