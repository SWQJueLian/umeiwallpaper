# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UMeiItem(scrapy.Item):
    name = scrapy.Field()
    # 如果要使用图片管道，这个字段必须是这个名字，否则你自己要继承图片管道类，重写相关的方法。
    # 这里字段要写入图片的下载url地址。
    image_urls = scrapy.Field()

    # images是用于存放下载图片的结果
    images = scrapy.Field()
    dirname = scrapy.Field()
