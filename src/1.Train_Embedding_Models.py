#!/usr/bin/env python
# coding: utf-8

# ### 0. Imports
# 
# If this code block is failing, make sure you have all of the necessary packages installed. See `requirements.txt` in the root directory for more information.

# In[1]:


import os
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import pandas as pd
import gzip
from multiprocessing import Pool
import multiprocessing
import time


# ### 1. Set Variables and Paths
# 
# `data_dir` should match where you have your data saved and `model_dir` is where your embedding models will be output. The cores variable sets the number of cores dedicated to parallelizing preprocessing. By default, half of your cores will be used. Set these to your preference accordingly.

# In[ ]:


data_dir = "../data"
model_dir = "../models"
cores = multiprocessing.cpu_count() // 2


# ### 2. Identify Files for Model Training
# 
# This will find **all** files in the `data_dir` specified. You will run into problems in later steps if there are any other files in the directory that cannot be opened as expected or are named in unexpected ways (data is expected to be named `sample_region.Sample_Country.eng.[clean|1].IN.gz`).

# In[3]:


file_paths = [os.path.join(data_dir, file).replace("\\", "/") for file in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file))]


# ### 3. Function to Train and Save Embedding Space
# 
# This function does the following:
# 
# 1. Opens the file into a Pandas dataframe
# 2. Extracts the text column and preprocesses each sample using simple_preprocess from Gensim (throwing away the rest of the data)
# 3. Uses Gensim Word2Vec to train a skip-gram model, iterating over the samples 
# 4. Saves the model to the given directory

# In[ ]:


def preprocess_text(texts):
    return [simple_preprocess(text) for text in texts]

def create_and_save_embedding_model(file_path, timestamp=None):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    country = os.path.basename(file_path).split(".")[1] # Extract country name from file name
    model_path = os.path.join(model_dir, country + ".model")
    
    if os.path.exists(model_path):
        print(f"Model for {country} already exists. Skipping...")
        return
    print(f"Processing {country}...")

    with gzip.open(file_path, 'rt', encoding='utf-8', errors='replace') as f:
        df = pd.read_csv(f, encoding='utf-8', on_bad_lines='skip')
    if timestamp is not None:
        elapsed = time.time() - timestamp
        minutes, seconds = divmod(int(elapsed), 60)
        print(f"\tLoaded {df.shape[0]} rows of data ({minutes}:{seconds:02d})")
        timestamp = time.time()
    
    df = df['Text'].tolist()[1:2000000]  # limit to 2 million rows

    
    with Pool(processes=cores) as pool:
        sentences = pool.map(simple_preprocess, df)
    if timestamp is not None:
        elapsed = time.time() - timestamp
        minutes, seconds = divmod(int(elapsed), 60)
        print(f"\tPreprocessed data ({minutes}:{seconds:02d})")
        timestamp = time.time()

    del df
    
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1, workers=4, epochs=1)
    model.save(model_path)
    if timestamp is not None:
        elapsed = time.time() - timestamp
        minutes, seconds = divmod(int(elapsed), 60)
        print(f"\tWord2Vec model saved ({minutes}:{seconds:02d})")


# ### 4. Loop Through and Train All Models
# 
# Runs the embedding model code for each of the identified files

# In[ ]:


if __name__ == "__main__":
    for file_path in file_paths:
        create_and_save_embedding_model(file_path, timestamp=time.time())

