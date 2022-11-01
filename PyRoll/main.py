import pandas as pd
import os, csv

csvpath = r'\Users\Nickaruto\Desktop\python-challenge\PyRoll\Resources\election_data.csv'

data = pd.read_csv(csvpath)
election_df = pd.DataFrame(data)

total_votes = election_df[0].sum()
candidates = election_df[3].value_counts()

print(f'Total Votes: {total_votes}')