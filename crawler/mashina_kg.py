import httpx
from parsel import Selector


class MashinaCrawler:
    MAIN_URL = "https://www.mashina.kg/search/all/"
    BASE_URL = "https://www.mashina.kg"

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text

    def get_title(self):
        html = Selector(self.page)
        title = html.css("title::text").get()
        return title

    def get_car_links(self):
        html = Selector(self.page)
        links = html.css(".list-item a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:3]

if __name__ == "__main__":
    crawler = MashinaCrawler()
    crawler.get_page()
    # print("Title", crawler.get_title())
    crawler.get_car_links()