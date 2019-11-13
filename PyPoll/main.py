#IMPORT & READ CSV
import os
import csv
import numpy as np

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, newline = '') as election_csv:
    csv_reader = csv.reader(election_csv, delimiter = ',')
    csv_header = next(csv_reader)
    print(csv_header)

#IMPORT DATA

    voter_id = []
    county = []
    candidates = []

    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    

#Total number of votes cast

total_votes = len(voter_id)
#print(total_votes)


#Complete list of Candidates who received votes

#unique_candidates = np.array(candidates)
#print(np.unique(unique_candidates))

#Total number of votes each candidate won


Correy_Count = 0
Khan_Count = 0
Li_Count = 0
O_Tooley_Count = 0

for i in range(0, len(candidates)):
    if candidates[i] == "Correy":
        Correy_Count = Correy_Count + 1
    elif candidates[i] == "Khan":
        Khan_Count = Khan_Count + 1
    elif candidates[i] == "Li":
        Li_Count = Li_Count + 1
    elif candidates[i] == "O'Tooley":
        O_Tooley_Count = O_Tooley_Count + 1
    else:
        print("Unknown candidate found")
        print("Run unique candidate function")

#print(Khan_Count)    
#print(Correy_Count)
#print(Li_Count)
#print(O_Tooley_Count)

#Percentage of votes each candidate won

Khan_win = round(((Khan_Count / total_votes) * 100), 3)
Correy_win = round(((Correy_Count / total_votes) * 100), 3)
Li_win = round(((Li_Count / total_votes) * 100), 3)
OTooley_win = round(((O_Tooley_Count / total_votes) * 100), 3)
#print(Khan_win)
#print(Correy_win)
#print(Li_win)
#print(OTooley_win)

#Winner of the election based on popular vote

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
    print(f'Winner: Khan')
    print("--------------------------")

election_results()
