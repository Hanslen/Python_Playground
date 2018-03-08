# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import re
# import csv
# browser = webdriver.Chrome()
# with open('../../hotLocation.csv', newline='') as f:
#     locations = csv.reader(f)
#     for l in locations:
#         browser.get('https://www.booking.com/')
#         elem = browser.find_element_by_name('ss')  # Find the search box
#         elem.send_keys(l[0] + Keys.RETURN)
#         try:
#             dest_id = re.search(r'dest_id=\D*\d+', browser.current_url).group(0).split('=')[1]
#             with open('../../dest_id.csv', 'a') as of:
#                 of.write(l[0]+","+dest_id+"\n")
#         except:
#             print("Can not get the information of ",l[0])
# browser.quit()