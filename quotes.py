# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        self.log("I just fisited: " + response.url)
        for quote in response.css("div.quote"):
            yield {
                "author_name": quote.css("small.author::text").get(),
                "text": quote.css("span.text::text").get(),
                "tags": quote.css("a.tag::text").getall(),
            }
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)
