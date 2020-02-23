import os
import csv

#import csv file
csvpath = os.path.join("Resources", "election_data.csv")

#variable list 
total_votes = 0
candidate_dict = {}
vote_percentage = []
winner_votes = 0
winner = "TBA"

#open and read file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row
    next(csvreader)

    #loop through file
    for row in csvreader:

        #calculate total number of votes cast
        total_votes += 1

        #check dictionary to find candidate's name:
            #if entry exists, add one in order to count votes
            #------------------------------------------------
            #if not, set value to one in order to
            #add the name to the dictionary
        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1

#format output/print
print("")
print("")
print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}")
print("-" * 25)
#finding/printing winner, winning percentage, and number of votes
for candidate, votes in candidate_dict.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
    percentage = format((votes/total_votes)*100,'.3f')
    print(f"{candidate}: {percentage}% ({votes})")
print("-" * 25)
print(f"Winner: {winner}")
print("-" * 25)
print("")
print("")    

filename = "election_analysis.txt"
with open(filename, 'w') as file_object:
    file_object.write("")

filename = "election_analysis.txt"
with open(filename, 'a') as file_object:
    file_object.write("Election Results\n")
    file_object.write("-" * 25)
    file_object.write(f"\nTotal Votes: {total_votes}\n")
    file_object.write("-" * 25)
    #finding/printing winner, winning percentage, and number of votes
    for candidate, votes in candidate_dict.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
        percentage = format((votes/total_votes)*100,'.3f')
        file_object.write(f"\n{candidate}: {percentage}% ({votes})")
    file_object.write("\n")
    file_object.write("-" * 25)
    file_object.write(f"\nWinner: {winner}\n")
    file_object.write("-" * 25)        