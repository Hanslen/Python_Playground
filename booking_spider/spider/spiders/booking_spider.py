import scrapy
import re

class BookingSpider(scrapy.Spider):
    name = "booking"
    offset = 0
    fullindemand = 0
    total = 0
    baseURL = 'https://m.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfbnmIAQGYATG4AQfIAQzYAQPoAQGSAgF5qAID;sid=fd5b0b32a48729553549d6232dc8cabc;checkin=2018-05-05;checkin_monthday=5;checkin_year_month=2018-5;checkout=2018-05-10;checkout_monthday=10;checkout_year_month=2018-5;class_interval=1;dest_id=20088325;dest_type=city;dtdisc=0;genius_rate=1;group_adults=2;group_children=0;inac=0;index_postcard=0;label_click=undef;no_rooms=1;not_last_min_flag=1;postcard=0;raw_dest_type=city;room1=A%2CA;sb_price_type=total;search_form_id=5dee8c81abd7031b;src=index;ss=New+York+City;ss_all=0;ssb=empty;sshis=0;ssne=New+York+City;ssne_untouched=New+York+City;rows=40;offset='
    start_urls = [baseURL+str(offset)]

    def parse(self, response):
        # let hotels list        
        hotels = response.css('div.lastbooking::text').extract() + response.css('span.lastbooking::text').extract()
        for hotel in hotels:
            if hotel != '\n':
                try:
                    num = int(re.search('\d+ times', hotel).group(0).split(' ')[0])
                except:
                    num = 0
                self.total += num
        print(self.total)
        # print(hotels)
        # for hotel in hotels:
        #     print("._.")
        #     bookMsg = hotel.css('::text')[2].extract()
        #     print("0.0")
        #     if bookMsg:
        #         num = int(re.search('\d+',bookMsg).group(0))
        #         self.total += num
        #         print("Hot", self.total)
        # print("Hello")
        # print("Total", self.total)
        
        # print(hotels[0].css('div.'))
        # for hotel in hotels:
        #     self.total += 1
        #     if hotel.css('div.data-number-of-users'):
        #         print(hotel.css('div.data-number-of-users'))
        # print("Total:",self.total)
        # print("In demand", self.fullindemand)
        # self.offset += 15
        # next_page = self.baseURL + str(self.offset)
        # yield response.follow(next_page, callback=self.parse)
        # content = quote.css('span.text::text').extract_first()
        # print(content)