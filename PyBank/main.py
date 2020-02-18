import os
import csv

#import csv file
csvpath = os.path.join("Resources", "budget_data.csv") 

#format/print start of form
print("")
print("")
print("Financial Analysis")
print("-" * 25)

#open and read file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #count number of months (1 month per line)
    total_months = sum(1 for row in csvreader)
    print(f"Total Months: {total_months-1}")

    Integer earnings = 0
    
    for row in csvreader:

        #calculate net total profits/losses
        earnings += row[1]
        print(f"Total: ${net_total}")

        #calculate average of changes in profits/losses
        average_change = " to be calculated"
        print(f"Average Change: ${average_change}")

        #calculate greatest increase in profits/losses
        greatest_increase = " to be calculated"
        print(f"Greatest Increase in Profits: {greatest_increase}")

        #calculate greatest decrease in profits/losses
        greatest_decrease = " to be calculated"
        print(f"Greatest Decrease in Profits: {greatest_decrease}")

        print("")
        print("")