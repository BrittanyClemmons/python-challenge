#IMPORT & READ CSV
import os
import csv
import numpy as np

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, newline = '') as election_csv:
    csv_reader = csv.reader(election_csv, delimiter = ',')
    csv_header = next(csv_reader)
    #print(csv_header)
    print('Calculating winner...')


#IMPORT DATA
    voter_id = []
    candidates = []

    for row in csv_reader:
        voter_id.append(row[0])
        candidates.append(row[2])
    

#TOTAL NUMBER OF VOTES CAST
total_votes = len(voter_id)
#print(total_votes)


#COMPLETE LIST OF CANDIDATE WHO RECEIVED VOTES
find_candidates= set(candidates)
unique_candidates = list(find_candidates)
sorted_candidates = sorted(unique_candidates)
#print(sorted_candidates)


#TOTAL NUMBER OF VOTES EACH CANDIDATE WON
Correy_Count = 0
Khan_Count = 0
Li_Count = 0
O_Tooley_Count = 0

Correy_Count = candidates.count("Correy")
Khan_Count = candidates.count("Khan")
Li_Count = candidates.count("Li")
O_Tooley_Count = candidates.count("O'Tooley")
#print(Correy_Count)
#print(Khan_Count)
#print(Li_Count)
#print(O_Tooley_Count)


#PERCENTAGE OF VOTES EACH CANDIDATE WON
Correy_win = round(((Correy_Count / total_votes) * 100), 3)
Khan_win = round(((Khan_Count / total_votes) * 100), 3)
Li_win = round(((Li_Count / total_votes) * 100), 3)
OTooley_win = round(((O_Tooley_Count / total_votes) * 100), 3)

#print(Correy_win)
#print(Khan_win)
#print(Li_win)
#print(OTooley_win)


#WINNER OF THE ELECTION BASED ON POPULAR VOTE
percentage = []

percentage.append(Correy_win)
percentage.append(Khan_win)
percentage.append(Li_win)
percentage.append(OTooley_win)

max = max(percentage)
index = percentage.index(max)

winner = sorted_candidates[index]
#print(winner)


#PRINT RESULT TO TERMINAL
def election_results():
    print(" ")
    print("Election Results")
    print("--------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------")
    print(f'Khan:     {Khan_win}%  ({Khan_Count})')
    print(f'Correy:   {Correy_win}%  ({Correy_Count})')
    print(f'Li:       {Li_win}%  ({Li_Count})')
    print(f"O'Tooley:  {OTooley_win}%  ({O_Tooley_Count})")
    print("--------------------------")
    print(f'Winner: {winner}')
    print("--------------------------")
election_results()


#OUTPUT TO TXT FILE
def election_results_txt():
    e_res = 'election_results'
    print(" ", file=open(e_res, 'w'))
    print("Election Results", file=open(e_res, 'a'))
    print("--------------------------", file=open(e_res, 'a'))
    print(f'Total Votes: {total_votes}', file=open(e_res, 'a'))
    print("--------------------------", file=open(e_res, 'a'))
    print(f'Khan:     {Khan_win}%  ({Khan_Count})', file=open(e_res, 'a'))
    print(f'Correy:   {Correy_win}%  ({Correy_Count})', file=open(e_res, 'a'))
    print(f'Li:       {Li_win}%  ({Li_Count})', file=open(e_res, 'a'))
    print(f"O'Tooley:  {OTooley_win}%  ({O_Tooley_Count})", file=open(e_res, 'a'))
    print("--------------------------", file=open(e_res, 'a'))
    print(f'Winner: {winner}', file=open(e_res, 'a'))
    print("--------------------------", file=open(e_res, 'a'))
election_results_txt()
