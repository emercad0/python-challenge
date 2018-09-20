import os
import csv
from collections import defaultdict



data_file = os.path.join("Resources","budget_data_1.csv")
data_file2 = os.path.join("Resources","budget_data_2.csv")
r_analysis = os.path.join("Resources","results.txt")

#!ls
#pwd

#The total number of months included in the dataset
# Add up all the months and if the date is equal to each other don't count
#The total amount of revenue gained over the entire period
# Sum of column 2
#The average change in revenue between months over the entire period
# average of totalSum -
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


ttlMonths = 0
prevRevenue = 0
month0fChng = []
revDiff = []
greatestInc = ["", 0]
greatestDec = ["", 999999]
amntOfRev = 0
avgRev = 0


def file_check(path):
    with open(path) as data:
        csvReader = csv.DictReader(data, delimiter=',')
        header = next(csvReader)
        for row in  csvReader:
            yield row


for row in (file_check(data_file2)):
    ttlMonths = ttlMonths + 1
    amntOfRev = amntOfRev+ int(row["Revenue"])
    #print(amntOfRev)
    revChng = int(row["Revenue"]) - prevRevenue
    revDiff = revDiff + [revChng]
    prevRev = int(row["Revenue"])
    #print(type(prevRev))
    month0fChng = month0fChng + [row["Date"]]
    if (revChng > greatestInc[1]):
        greatestInc[0] = row["Date"]
        greatestInc[1] = revChng
    if (revChng < greatestDec[1]):
        greatestDec[0] = row["Date"]
        greatestDec[1] = revChng

def _avg(self):
    for row in revDiff:
        avg = sum(revDiff)/len(revDiff)
        return "Average Revenue Change: $" +str(avg)


result = (
          f"\nFinancial Analysis\n"
          f"----------------------------\n"
          f"Total Months: {ttlMonths}\n"
          f"Total Revenue: {amntOfRev}\n"
          f"{_avg(revDiff)}\n"
          f"Greatest Increase in Revenue: {greatestInc[0]} (${greatestInc[1]})\n"
          f"Greatest Decrease in Revenue: {greatestDec[0]} (${greatestDec[1]})\n")
with open(r_analysis, "w") as file:
    file.write(result)

