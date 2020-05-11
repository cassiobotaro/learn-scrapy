import scrapy


class LoginSpider(scrapy.Spider):
    name = "login_spider"
    login_url = "http://quotes.toscrape.com/login"
    start_urls = [login_url]

    def parse(self, response):
        data = {
            "username": "abc",
            "password": "abc",
        }
        yield scrapy.FormRequest.from_response(
            response=response,
            url=self.login_url,
            formdata=data,
            callback=self.parse_quotes,
        )

    def parse_quotes(self, response):
        """Parse the main page after the spider is logged in"""
        for q in response.css("div.quote"):
            yield {
                "author_name": q.css("small.author::text").get(),
                "author_url": q.css(
                    'small.author ~ a[href*="goodreads.com"]::attr(href)'
                ).get(),
            }
