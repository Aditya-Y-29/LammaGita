## Directory structure

```
LAMMAGITA/
├── data/
│   ├── Bhagwad_Gita.csv: This dataset was downloaded from Kaggle.
│   ├── dataset.csv: Processed dataset.
├── models/
│   ├── llama-2-7b.ggmlv3.q4_0.bin: Quantized LLM 2 model.
├── src/
│   ├── llm.py: This file contains the initial LLM configuration.
│   ├── prompt.py: It contains the prompts used for model inference.
│   ├── utils.py: This sets up the connection to VectorDB for inference.
├── vectorstore/ : This directory contains files related to the vector database.
├── custom_dataset.py: This script processes data from Bhagwad_Gita.csv and creates dataset.csv.
├── db_build.py: This script builds the vector database for similarity search.
├── main.py: This file contains the user interface for the chatbot created using Streamlit.
├── process_dataset.py: This script further processes the dataset.
└── README.md: This file provides information on the directory structure and instructions for running the project.
```

## Dataset
https://www.kaggle.com/datasets/a2m2a2n2/bhagwad-gita-dataset. This dataset was used for giving context to the llama 2 model. This dataset was further modified to have columns meaning and learning for each sanskrit shloka.

## Models
Model used: llama-2-7b.ggmlv3.q4_0.bin 
Link: https://huggingface.co/TheBloke/Llama-2-7B-GGML
Quantised models are used because they are less compute- and memory-intensive. 

## Tools and Data
![My Image](assests\overview.png)

##