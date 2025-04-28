# Synonymy Representations in World Englishes

This is the repository for the Computational Linguistics Capstone project of John Speaks at the University of Illinois. For any questions related to the repository or data, please contact [jspeaks2@illinois.edu](mailto:jspeaks2@illinois.edu). The analysis in this repository aims to look at how models of synonymy differ from one another, specifically when it comes to different varieties of world English. It is important to understand how the tools we use both for linguistic research and consumer facing development represent people and cultures from around the world. This paper aims to identify inequities in who is best served by different forms of synonym models. The exploration uses a number of different methods (both static and dynamic LLM based approaches) to collect or generate synonyms for 1000 randomly sampled words from world English models. These synonym lists are then compared directly for analysis, and also are evaluated using embedding spaces created from different varieties of world English according to Kachru's World English model. The rest of this readme and the accompanying source files detail the approaches and data sources of this investigation.

As a paper is written and further analysis is completed, those changes will be reflected in this repository.

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

Additionally, before continuing, ensure you have all of the required python packages installed in your python environment. All required packages are listed in `requirements.txt`.

## 1. Training World English Embedding Spaces

Once all of the data is in place in the data directory you are able to start training the embedding spaces. Go to the first Jupyter notebook in the `src` folder. It is called `1.Train_Embedding_Models.ipynb`. This file walks you through the process of training the embedding spaces. At the start of the file, make sure to specify the route of your data directory and where you would like your models output if they differ. Run the cells cell by cell and make sure the code has completed and generated all the files into the `models` directory (or another directory you specify) before proceeding.

*Alternatively*, there is also a python file derived from the notebook. For some systems, this may run much faster. It is called `1.Train_Embedding_Models.py` and can be run from the terminal.

If you would like to or need to skip this step due to time savings or system constraints, the resulting models are stored [here](https://uofi.box.com/s/wql380ut9op44ns83eal4anrwkzp580n) as they were too large to be included in the GitHub repository.

## 2. Extracting Synonyms from Sources

In this step, synonyms for the sampled words are extracted using both traditional resources (e.g., Merriam-Webster and WordNet) and modern language models (e.g., GPT, DeepSeek, and Llama). The outputs include cleaned synonym lists for each method, which are saved in the `synonyms` directory for further analysis (though you can specify another output). For detailed instructions and implementation, refer to the `2.Get_Synonyms_From_Sources.ipynb` file in the `src` folder.

*Please note!* Some of the synonym generation in this file requires the use of paid APIs. In total, the code in this analysis should cost approximately $0.08 to run and no more than $0.10.

## 3. Scoring Synonym Lists

This step evaluates the quality and similarity of the extracted synonyms using metrics such as cosine similarity and Jaccard similarity. Statistical analyses, including ANOVA and Tukey HSD tests, are performed to identify significant differences across regions and methods. Visualizations and results are saved in the `results` and `visualizations` directories (though these can be changed by the user). For more details, see the `3.Score_Synonym_Lists.ipynb` file in the `src` folder.
