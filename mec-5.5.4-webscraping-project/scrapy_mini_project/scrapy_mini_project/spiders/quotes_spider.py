import scrapy

# Example 1: "scrapy crawl quotes"

#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#        'http://quotes.toscrape.com/page/2/',
#    ]
#
#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)


# Example 2: "scrapy crawl quotes -o quotes.json"

#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#        'http://quotes.toscrape.com/page/2/',
#    ]
#
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.css('small.author::text').get(),
#                'tags': quote.css('div.tags a.tag::text').getall(),
#            }


# Example 3: "scrapy crawl quotes -o quotes.json"
# This example recursively follows the link to the next page, extracting data from it.

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

