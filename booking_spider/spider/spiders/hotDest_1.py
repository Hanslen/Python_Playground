# extract hot locations

import scrapy
import re

class HotDest(scrapy.Spider):
    name = "hotDest"
    baseURL = 'https://www.booking.com/city.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfbnmIAQGYATG4AQfIAQzYAQPoAQH4AQKSAgF5qAID;sid=ec8e53f514787ce938077c928b031de4;inac=0&'
    start_urls = [baseURL]

    def parse(self, response):
        # write as file
        # with open("hotDest.html", "wb") as f:
        #     f.write(response.body)
        locations = response.css('div.block_header a::text').extract()
        print(locations)
        with open("hotLocation.csv", "a") as f:
            for location in locations:
                f.write(location+"\n")
        print("Successfully export hot locations!")