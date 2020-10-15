import scrapy


class BookstoscrapeSpider(scrapy.Spider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        urls = response.css("h3 > a::attr(href)").getall()
        yield from response.follow_all(urls, callback=self.parse_details)
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_details(self, response):
        cover_url = response.css(".thumbnail img::attr(src)").get()
        yield {"image_urls": [
            response.urljoin(cover_url),
            ]}
