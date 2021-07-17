# Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t
# ami csak az emailím és név oszlopokat tartalmazza. Tehát például:
# Email,Name
# peter.kiss@sel.hu,Kiss Péter
# ervin.nagy@sel.hu,Nagy Ervin

import csv

csv_in = open('table_in.csv', 'r')
reader = csv.reader(csv_in, skipinitialspace=True, delimiter=',')


with open('table_out.csv', 'w') as csv_out:
        out = csv.writer(csv_out, skipinitialspace=True, delimiter=',')
        for row in reader:
            line = [row[1], row[0]]
            out.writerow(line)


        # write the data
#        writer.writerow(data)
 #           csv.writer(csv_out, row[1])
  #          print(row[1], row[0], sep=",")



#    for row in csv_reader:
#        print(row[0], row[2])
