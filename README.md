# Synonymy Representations in World Englishes

## 0. Sourcing Data

To access the data, visit the webpage for [Professor Jonathan Dunn's *Corpus of Global Language Use*](https://publicdata.canterbury.ac.nz/Research/Geocorpus/). For this project, we are using version CGLU_v5.2. Please follow these steps:

1. Identify the countries of interest within each region directory.
2. For each country, navigate to the `/eng` folder.
3. Download the first `.IN` file you find.
4. Place all downloaded files directly into a folder called `data` without decompressing or renaming them.

Countries Used in This Study:

| Region | Countries |
| --- | --- |
| Inner Circle | United States, Canada, United Kingdom, Ireland, Australia, New Zealand |
| Outer Circle | India, Singapore, Nigeria, Malaysia |
| Expanding Circle | China, Russia, Brazil |

## 1. Training World English Embedding Spaces

Once all of the data is in place in the data directory you are able to start training the embedding spaces. Go to the first Jupyter notebook in the `src` folder. It is called `1.Train_Embedding_Models.ipynb`. This file walks you through the process of training the embedding spaces. At the start of the file, make sure to specify the route of your data directory and where you would like your models output if they differ. Run the cells cell by cell and make sure the code has completed and generated all the files into the `models` directory (or another directory you specify) before proceeding.

*Alternatively*, there is also a python file derived from the notebook. For some systems, this may run much faster. It is called `1.Train_Embedding_Models.py` and can be run from the terminal.
