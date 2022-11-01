import pandas as pd
import os, csv
import sys

csvpath = r'\Users\Nickaruto\Desktop\python-challenge\PyRoll\Resources\election_data.csv'

data = pd.read_csv(csvpath)
election_df = pd.DataFrame(data)

#counting votes
total_votes = election_df['Ballot ID'].count()

#candidates_counts = election_df['Candidate'].value_counts()
candidate_name = election_df['Candidate'].value_counts().keys().tolist() #column1 in value_counts series to dictkey
candidate_votes = election_df['Candidate'].value_counts().tolist()       #column2 in value_counts series to key values
votes_per_candidate = dict(zip(candidate_name, candidate_votes))         #creating dict

#create list and calculate vote% for each candidate in dictionary
vote_percent_list = []
for i in votes_per_candidate:
    vote_percent = (votes_per_candidate[i]/total_votes)*100
    vote_percent_list.append(vote_percent.round(2))

# print(vote_percent_list)
# print(votes_per_candidate)

#printing to terminal
print("Election Results:")
print(f'Total Votes: {total_votes}')
print('Diana DeGette: ' + str(vote_percent_list[0]) + "% (" + str(votes_per_candidate['Diana DeGette']) + ")")
print('Charles Casper Stockham: ' + str(vote_percent_list[1]) + "% (" + str(votes_per_candidate['Charles Casper Stockham']) + ")")
print('Raymon Anthony Doane: ' + str(vote_percent_list[2]) + "% (" + str(votes_per_candidate['Raymon Anthony Doane']) + ")")
print('Winner: Diana DeGette')

#creating and printing to election_data_results
sys.stdout = open('election_data_results.txt', 'w')
print("Election Results:")
print(f'Total Votes: {total_votes}')
print('Diana DeGette: ' + str(vote_percent_list[0]) + "% (" + str(votes_per_candidate['Diana DeGette']) + ")")
print('Charles Casper Stockham: ' + str(vote_percent_list[1]) + "% (" + str(votes_per_candidate['Charles Casper Stockham']) + ")")
print('Raymon Anthony Doane: ' + str(vote_percent_list[2]) + "% (" + str(votes_per_candidate['Raymon Anthony Doane']) + ")")
print('Winner: Diana DeGette')
sys.stdout.close()
