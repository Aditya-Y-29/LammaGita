import pandas as pd
import openai
import time
from dotenv import load_dotenv
import os

load_dotenv()
# Specify the file path to your CSV file
file_path = 'data/Bhagwad_Gita.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

openai.api_key = os.getenv("OPENAPI_KEY")

# for row in df.itertuples():
english_meaning=[]
learning=[]
for index in range(100):
    time.sleep(25)
    row=df.iloc[index]
    while(1):
        try:
            sholka=row.EngMeaning
            # Define the system message
            system_msg = 'You are expert at dealing with life problems by taking reference from Bhagvad Gita.'
            # Define the user message
            user_msg = f'''I would be giving you some Bhagvad Gita sholka's english meaning, return me what a human can learn in from this in atmost 60 words? Here is the sholka's meaning in English ->{sholka}'''
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "system", "content": system_msg},
                                                    {"role": "user", "content": user_msg}])
            english_meaning.append(sholka)
            print(response)
            learning.append(response["choices"][0]["message"]["content"])
            break;
        except Exception as e:
            print(e)
            print("Error")


data = {
    "Meaning": english_meaning,
    "Learning": learning
}

# Create the DataFrame from the dictionary
df = pd.DataFrame(data)
file_path = "data/dataset.csv"

# Use the to_csv method to save the DataFrame to a CSV file
df.to_csv(file_path, index=False)