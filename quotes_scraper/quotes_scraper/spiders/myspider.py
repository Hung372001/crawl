import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://dirtycoins.vn/shop"]

    def parse(self, response):
        for listProduct in response.css("div.product-grid-view"):
            image = listProduct.css("img.lazyload::src").get()
            title = listProduct.css("div.product-content>h3>a::text").get()

            price = listProduct.css("span.regular-price::text").get()
            yield {
                "text": image,
                "title": title,
                "price":price
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)