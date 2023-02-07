# Import modules os and csv
import os
import csv

# Part 2: Pypoll
## Pull CSV file "election_data.csv" and set path (NEED HELP FINDING PATH)
pypoll_csv = os.path.join("Resources", "election_data.csv")

## Open CSV as reader
with open(pypoll_csv, newline ="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)

    ## Create lists
    voter_id = []
    county = []
    candidates = []

    ## Insert variables
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    ## Looping through all rows
    for row in csvreader: 
        total_votes ==1
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

    ## Create list to insert into dictionary for analysis
    candidates = ["Khan", "Correy", "Li","O'Tooley"]
    votes = [khan_votes, correy_votes,li_votes,otooley_votes]

    ## Data analysis
    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    khan_percent = (khan_votes/total_votes) *100
    correy_percent = (correy_votes/total_votes) * 100
    li_percent = (li_votes/total_votes)* 100
    otooley_percent = (otooley_votes/total_votes) * 100

    ## Check that Election Results checks out
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    print(f"Li: {li_percent:.3f}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    print(f"----------------------------")
    print(f"Winner: {key}")

## Save and export text file with results
with open(results_text, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
## Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        ### Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        ### Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        ###  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        ### Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    ## Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    ## Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)