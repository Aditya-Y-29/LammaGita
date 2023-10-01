import pandas as pd
import json

df = pd.read_csv('data/dataset.csv')

for row in df.itertuples():
    learning = row.Learning
    learning = learning.replace("\n", "")
    df.at[row.Index, 'Learning']=json.loads(learning)["content"]

file_path = "data/dataset.csv"
df.to_csv(file_path, index=False)