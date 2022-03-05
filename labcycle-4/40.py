import csv
with open("csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("Period       Subject")
    print("--------------------")
    for i in d:
        print(i['Period'], i['Subject'])
