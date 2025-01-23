import csv
import json

file_csv='products.csv'
new_json_file='new_json.json'

data=[]

with open(file_csv,'r') as fileCSV:
    csvreader=csv.DictReader(fileCSV)
    for row in csvreader:
        data.append(row)

with open(new_json_file,mode='w') as file:
    json.dump(data,file,indent=4)