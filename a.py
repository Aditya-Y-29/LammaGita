import pandas as pd

# Load the CSV file into a Pandas DataFrame, specifying columns to load
columns_to_load = [ 'Shloka', 'EngMeaning']
df = pd.read_csv('data/Bhagwad_Gita.csv', usecols=columns_to_load)

# Specify the file path where you want to save the CSV file
file_path = 'data/Bhagwad_Gita.csv'

# Use the to_csv method to save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

# Print the selected columns
print(df.iloc[0])
# from langchain.document_loaders.csv_loader import CSVLoader

# loader = CSVLoader(file_path='data/Bhagwad_Gita.csv')
# # loader = CSVLoader(file_path='data/Bhagwad_Gita.csv')
# data = loader.load()

# print(data[0])