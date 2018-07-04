import os
import csv

election_data = 'election_data.csv'

with open(election_data, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    votes = []
    candidates_list = []
    candidates_votes = []

    print("Election Results \n-------------------------")

    for row in csvreader:
        votes.append(row[2])
        total_votes = len(votes)
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

    print(f"Total Votes: {total_votes} \n-------------------------")

    for candidates in candidates_list:
        candidates_votes.append(votes.count(candidates))

    for x in range(len(candidates_list)):
        percentage_won = round((int(candidates_votes[x])/total_votes) * 100, 3)
        print(f"{candidates_list[x]}: {percentage_won}% ({candidates_votes[x]})")
    
    print(f"------------------------- \nWinner: {candidates_list[candidates_votes.index(max(candidates_votes))]} \n-------------------------")

with open("output.txt", "w") as txtfile:
    txtfile.write(f"Election Results \n------------------------- \nTotal Votes: {total_votes} \n------------------------- \n")
    for x in range(len(candidates_list)):
        txtfile.write(f"{candidates_list[x]}: {percentage_won}% ({candidates_votes[x]}) \n")
    txtfile.write(f"------------------------- \nWinner: {candidates_list[candidates_votes.index(max(candidates_votes))]} \n-------------------------")