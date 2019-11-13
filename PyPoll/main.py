#IMPORT & READ CSV
import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, newline = '') as election_csv:
    csv_reader = csv.reader(election_csv, delimiter = ',')
    csv_header = next(csv_reader)
    print(csv_header)

#IMPORT DATA

voter_id = []


#Total number of votes cast
#Complete list of Candidates who received votes
#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election based on popular vote