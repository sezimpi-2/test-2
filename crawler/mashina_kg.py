import asyncio
import httpx
from parsel import Selector
from time import perf_counter


class MashinaCrawler:
    MAIN_URL = "https://www.mashina.kg/search/all/"
    BASE_URL = "https://www.mashina.kg"

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        print("Page: ", url)
        return response.text

    def get_title(self):
        html = Selector(self.page)
        title = html.css("title::text").get()
        return title

    def get_car_links(self, page: str):
        html = Selector(page)
        links = html.css(".list-item a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links
    
    async def get_cars(self):
        # start = perf_counter()
        tasks = []
        async with httpx.AsyncClient() as client:
            for i in range(1, 11):
                url = f"{self.MAIN_URL}?page={i}"
                task = asyncio.create_task(self.get_page(url, client))
                tasks.append(task)
        
            results = await asyncio.gather(*tasks)
            # print("Page", url)
            all_links = []
            for result in results:
                links = self.get_car_links(result)
                all_links.extend(links)

        # links = self.get_car_links()
        # print("Time: ", perf_counter() - start)
        print(all_links)
        return all_links[:3]

if __name__ == "__main__":
    crawler = MashinaCrawler()
    # await crawler.get_cars()
    # crawler.get_page()
    # print("Title", crawler.get_title())
    # crawler.get_car_links()
    asyncio.run(crawler.get_cars())