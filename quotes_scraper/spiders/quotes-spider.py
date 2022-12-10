import scrapy
from quotes_scraper.items import QuoteItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    """A class representing a scraper."""
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]
    
    def parse(self, response, **kwargs):
        """Parse the response object for quotes."""
        self.logger.info("hello this is my first spider")
        quotes = response.css('div.quote')
        for quote in quotes:
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css('quote_content', '.text::text')
            loader.add_css('tags', '.tag::text')
            quote_item = loader.load_item()
            author_url = quote.css('.author + a::attr(href)').get()
            yield response.follow(author_url, self.parse_author, meta={'quote_item': quote_item})

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
            
    def parse_author(self, response):
        quote_item = response.meta['quote_item']
        loader = ItemLoader(item=quote_item, response=response)
        loader.add_css('author_name', '.author-title::text')
        loader.add_css('author_birthday', '.author-born-date::text')
        loader.add_css('author_bornlocation', '.author-born-location::text')
        loader.add_css('author_bio', '.author-description::text')
        yield loader.load_item()