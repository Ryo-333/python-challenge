import os
import csv


# Initialize variables
total_votes = 0
candidates = {}  # Dictionary to store candidate names as keys and their vote counts as values

# Read the CSV file
with open("/Users/ryojousin/Downloads/Starter_Code 3/PyPoll/Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row
    data = list(csvreader)
    # Loop through the rows in the CSV file
    for row in data:
        total_votes += 1
        candidate_name = row[2]

        # If the candidate is already in the dictionary, increment their vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # If the candidate is not in the dictionary, add them with a vote count of 1
            candidates[candidate_name] = 1

# Find the winner
winner = max(candidates, key=candidates.get)

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes with 3 decimal places each candidate won, and their total votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export as text
with open('election_analysis.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------")
    output_file.write(f"Winner: {winner}")
    output_file.write("-------------------------")
