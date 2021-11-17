import scrapy

class GrapingSpider(scrapy.Spider):
    name = 'graping'

    start_urls = ['https://www.google.com/search?q=biplob+manna']

    def parse(self, response, **kwargs):
        self.logger.info("scraping google.com with the name...")

        links = response.css('a::attr(href)').getall()
        relevant_links = [] # list of links which are relevant to search terms

        for link in links:
            relevant_link = self.filter_links(link)
            if relevant_link is not None:
                relevant_links.append(relevant_link)
            # yield {
            #     "link": link
            # }
        
        for link in relevant_links:
            yield {
                "link": link
            }
        
    def filter_links(self, link, filter_text=["biplob", "manna"]):
        if "search" in link:
            return None
        for text in filter_text:
            if text not in link:
                return None
        return link[link.find('https'):]