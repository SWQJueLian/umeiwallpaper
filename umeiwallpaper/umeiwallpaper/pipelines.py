# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline


class MyImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        # info里面有spider对象的属性 # scrapy.pipelines.media.MediaPipeline.SpiderInfo

        adapter = ItemAdapter(item)
        img_name = adapter.get("name")
        dirname = adapter.get("dirname")
        # print(f"{img_name=}")
        return f"{dirname}/{img_name}.jpg"
