# -*- coding: utf-8 -*-
BOT_NAME = "splash_based_project"

SPIDER_MODULES = ["splash_based_project.spiders"]
NEWSPIDER_MODULE = "splash_based_project.spiders"
ROBOTSTXT_OBEY = True

SPLASH_URL = "http://localhost:8050"
DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,  # noqa:E501
}
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
}
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
