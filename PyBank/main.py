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

    #skip header row
    next(csvreader)

    #count number of months (1 month per line)
    total_months = 0

    #variables
    earnings = 0

    previous_month_earnings = 0
    current_month_earnings = 0
    
    greatest_increase_date = ""
    greatest_decrease_date = ""

    greatest_increase = 0
    greatest_decrease = 0

    cumulative_change = 0
    
    for row in csvreader:
        #sum months
        total_months += 1

        #calculate net total profits/losses
        earnings += int(row[1])

        #load current month earnings
        current_month_earnings = int(row[1])
    
        #calculate month over month change
        month_to_month_change = current_month_earnings - previous_month_earnings
        if greatest_increase_date != "":
            cumulative_change += month_to_month_change

        #check for greatest increase
        if month_to_month_change > greatest_increase:
            greatest_increase = month_to_month_change
            greatest_increase_date = row[0]
        
        #check for greatest decrease
        if month_to_month_change < greatest_decrease:
            greatest_decrease = month_to_month_change
            greatest_decrease_date = row[0]
        
        #load current month value into previous month variable
        previous_month_earnings = current_month_earnings

    #print total months to terminal
    print(f"Total Months: {total_months}")

    #print total earnings to terminal
    print(f"Earnings: ${earnings}")    

    #print average of changes in profits/losses to terminal
    #Had to subtract one from the total_months in the average_change
    #formula, since the first month would not have a previous month 
    #to compare against
    average_change = format(cumulative_change / (total_months-1), '.2f')
    print(f"Average Change: ${average_change}")

    #print greatest increase in profits/losses to terminal
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

    #print greatest decrease in profits/losses to terminal
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    #creates text file
    filename = "financial_analysis.txt"
    with open(filename, 'w') as file_object:
        file_object.write("")

    #appends information to text file
    filename = "financial_analysis.txt"
    with open(filename, 'a') as file_object:
        file_object.write("\nFinancial Analysis\n")
        file_object.write("-" * 25)
        file_object.write(f"\nTotal Months: {total_months}")
        file_object.write(f"\nTotal: ${earnings}")
        file_object.write(f"\nAverage Change: ${average_change}")
        file_object.write(f"\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        file_object.write(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    