import scrapy
from scrapy.http import HtmlResponse

from umeiwallpaper.items import UMeiItem


class UmeiSpider(scrapy.Spider):
    name = "umei"
    allowed_domains = ["umei.cc"]
    # start_urls = ["https://www.umei.cc/meinvtupian/meinvmote/235660.htm"]
    start_urls = ["https://www.umei.cc/bizhitupian/huyanbizhi/"]

    def parse(self, response: HtmlResponse, **kwargs):

        lists_xpath = "//div[@class='item masonry_brick']/div/div[@class='img']/a"

        selector_list = response.xpath(lists_xpath)

        for selector in selector_list:
            url = selector.xpath("./@href").get()
            # title = selector.xpath("./img/@alt").get()
            print(f"列表：{url=}")
            # print(f"{title=}")

            yield scrapy.Request("https://www.umei.cc" + url, callback=self.parse_item, dont_filter=False)

    def parse_item(self, response: HtmlResponse):
        last_page = response.xpath('//a[contains(text(),"尾页")]/@href').get()
        if last_page:
            count = int(last_page.split("/")[-1].rsplit(".", 1)[0].split("_")[1])
        else:
            count = 1
        # print(f"{count=}")
        for i in range(count):
            if i == 0:
                # url = self.start_urls[0]
                url = response.url
            else:
                url = f"{response.url.rsplit('.', 1)[0]}_{i + 1}.htm"
            print(f"{url=}")
            yield scrapy.Request(url, callback=self.parse_detail, dont_filter=False)

    def parse_detail(self, response: HtmlResponse):

        img_url = response.xpath("//div[@class='big-pic']/a/img/@src").get()
        name = response.url.split("/")[-1].split(".")[0]
        title = response.xpath('//div[contains(@class, "imgtitle")]/h1/text()').get()

        u_mei_item = UMeiItem()
        u_mei_item["name"] = name
        u_mei_item["dirname"] = title
        u_mei_item["image_urls"] = [img_url, ]

        # print(u_mei_item)

        yield u_mei_item
