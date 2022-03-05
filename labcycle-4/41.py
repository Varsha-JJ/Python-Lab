import csv
field_name = ['No', 'College name', 'Place']
car = [{'No': 1,'College name':'St marrys college','Place':'Bathery'},
       {'No': 2,'College name':'Alphonsa college','Place':'Bathery'},
       {'No': 3,'College name':'Kerala achademic','Place': 'Meenagadi'},
       {'No': 4,'College name':'Bharathiyar university', 'Place':'Thaloor'},
       {'No': 5,'College name':'MG university', 'Place':'Thirur'}]
with open('b.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('b.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter='|')
    for r in d:
        print(','.join(r))
