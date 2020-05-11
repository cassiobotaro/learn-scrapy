# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotejsSpider(scrapy.Spider):
    name = "quotejs"

    def start_requests(self):
        yield SplashRequest(
            url="http://quotes.toscrape.com/js", callback=self.parse
        )

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags > a.tag::text").getall(),
            }
