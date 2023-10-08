import os.path

BOT_NAME = "umeiwallpaper"

SPIDER_MODULES = ["umeiwallpaper.spiders"]
NEWSPIDER_MODULE = "umeiwallpaper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.2

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# 单独设置还不行，需要下载http2支持包，Twisted[http2]>=17.9.0
DOWNLOAD_HANDLERS = {
    "https": "scrapy.core.downloader.handlers.http2.H2DownloadHandler",
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "umeiwallpaper.pipelines.MyImagePipeline": 300,
}

# 图片管道下载存储根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(BASE_DIR, "Downloads")

# 你可以自定，也可以用默认的，默认就这2个值
IMAGES_URLS_FIELD = "image_urls"
IMAGES_RESULT_FIELD = "images"

# 允许重定向下载（有一些http会重定向到https，不允许就提示301状态码）
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# # # The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# # # The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 5
# # # The average number of requests Scrapy should be sending in parallel to
# # # each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# # # Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"



