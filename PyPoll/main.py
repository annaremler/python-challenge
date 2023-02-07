# Import modules os and csv
import os 
import csv

# Part 1: PyBank
## Pull CSV file "budget_data.csv" and set path
pypoll_csv = os.path.join("Resources", "election_data.csv")

## Open CSV as reader
with open (pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

## Create variables and lists
total_votes = 0
result = {}

## Calculating final results (am trying to streamline code now)        
    for row in csvreader:
        candidate = (row[2])
        total_votes = total_votes + 1
        if candidate in result:
            result[candidate]['votes'] += 1
        else:
            result[candidate] = {'votes': 1}
    candidate_winner = list(result.keys())[0]
    output = []
    for candidate in result:
        result[candidate]["candidate"] = candidate
        result[candidate]['percentage_vote'] = (result[candidate]['votes']/ total_votes) * 100
        if result[candidate_winner]['votes'] < result[candidate]['votes']:
            candidate_winner = candidate
        
# Print final results
    print(f"PyPoll Analysis")
    
    print(f"Total Votes:", total_votes)
    print(result)
    print(f"Winner:", candidate_winner)

# Export results to text file
with open ("PyPoll_analysis.txt", "w") as text:
    text.write("----------------------------------------------------------\n")
    text.write(f"PyPoll Analysis " + "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"Total Votes: " + str(total_votes) + "\n")
    text.write(str(result) + "\n")
    text.write(f"Winner: " + str(candidate_winner) + "\n")
