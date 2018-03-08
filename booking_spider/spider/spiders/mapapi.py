# import csv
# import urllib.request, json
# BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key=AIzaSyCbyIEf3sqn3I6tj4byGSYE8SlDbzo-kAE'

# with open('../../dest_id.csv', newline='') as f:
#     locations = csv.reader(f)
#     for l in locations:
#         newurl = BASE_URL.format(l[0]).replace(' ','%20')
#         try:
#             with urllib.request.urlopen(newurl) as url:
#                 data = json.loads(url.read().decode())
#                 geo = data['results'][0]["geometry"]["location"]
#                 with open('../../final.csv','a') as output:
#                     output.write(l[0]+","+l[1]+","+str(geo["lat"])+","+str(geo["lng"])+"\n")
#         except:
#             print("Fail on ", l[0])

