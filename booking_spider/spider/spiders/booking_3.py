# getting the latest Booking information
import scrapy
import re
import csv

class BookingSpider(scrapy.Spider):
    name = "booking"
    offset = 0
    total = 0
    # ['Venice', '-132007', '45.4408474', '12.3155151']
    with open('../../final.csv', newline='') as f:
        tmp = csv.reader(f)
        dest_id = list(tmp)
    id = 0
    baseURL = 'https://m.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfbnmIAQGYATG4AQfIAQzYAQPoAQGSAgF5qAID;sid=fd5b0b32a48729553549d6232dc8cabc;checkin=2018-05-05;checkin_monthday=5;checkin_year_month=2018-5;checkout=2018-05-10;checkout_monthday=10;checkout_year_month=2018-5;class_interval=1;dest_id={0};dest_type=city;dtdisc=0;genius_rate=1;group_adults=2;group_children=0;inac=0;index_postcard=0;label_click=undef;no_rooms=1;not_last_min_flag=1;postcard=0;raw_dest_type=city;room1=A%2CA;sb_price_type=total;search_form_id=5dee8c81abd7031b;src=index;ss=New+York+City;ss_all=0;ssb=empty;sshis=0;ssne=New+York+City;ssne_untouched=New+York+City;rows=15;offset={1}'
    start_urls = [baseURL.format(dest_id[id][1], offset)]
    progress = len(dest_id)

    def parse(self, response):
        # write as file
        # with open("test"+str(self.offset)+".html", "wb") as f:
        #     f.write(response.body)

        # get hotels list
        hotels = response.css('div.lastbooking::text').extract() + response.css('span.lastbooking::text').extract()
        if len(hotels) == 0 or self.offset == 15:
            print(self.dest_id[self.id][0], self.total)
            with open("latest.csv", "a") as f:
                output = self.dest_id[self.id][0] +","+ str(self.total)+","+self.dest_id[self.id][1]+","+self.dest_id[self.id][2]+","+self.dest_id[self.id][3]+"\n"
                f.write(output)
            self.id += 1
            print(self.id / self.progress)
            self.total = 0
            self.offset = 0
            try:
                next_page = self.baseURL.format(self.dest_id[self.id][1], self.offset)
            except:
                print("Finish all destination...")
                return
            yield response.follow(next_page, callback=self.parse)

        for hotel in hotels:
            if hotel != '\n':
                try:
                    num = int(re.search(r'\d+ times', hotel).group(0).split(' ')[0])
                except:
                    num = 0
                self.total += num
        # print(self.total)
        self.offset += 15
        next_page = self.baseURL.format(self.dest_id[self.id][1], self.offset)
        yield response.follow(next_page, callback=self.parse)
