# import csv

csv_filename = 'SourceRecord.csv'

# with open(csv_filename) as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row)


import csv; lst=[*csv.DictReader(open(csv_filename))]; 

print(lst)