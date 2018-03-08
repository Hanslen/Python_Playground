import json
import csv
csvfile = open('../../latest.csv', 'r')
jsonfile = open('../../forjs.json', 'w')
fieldnames = ("Location","weight","dest_id","long","la")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write("[")
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n') # need to remove the latestOne manually
jsonfile.write("]")