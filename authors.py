import scrapy


class AuthorSpider(scrapy.Spider):
    name = "authors"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        urls = response.css("div.quote > span > a::attr(href)").getall()
        for url in urls:
            yield response.follow(url=url, callback=self.parse_details)
        # follow pagination link
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
            "name": response.css("h3.author-title::text").get(),
            "birth-date": response.css("span.author-born-date::text").get(),
        }
