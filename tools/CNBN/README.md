# MNB Replication package


This repository contains the replication package and dataset of the paper entitled **A Hybrid Recommender System fro Labeling Github and Maven Central repositories** 

All the resources, including the tool, the dataset, and the article have been realized by:

- Juri Di Rocco
- Davide Di Ruscio
- Claudio Di Sipio 
- Phuong T. Nguyen
- Riccardo Rubei





# Setting the environment 

To run the Python scripts, you need the following libraries:

- scikit-learn 0.23.2
- nltk 3.5
- pandas 1.1.4
- guessLang 2.2.1





# Code structure 

This folder contains the source code of the tool structured as follows:
```
CNBN
    .
    |--- main.py         It is used to run the ten folder evaluation      
    |
    |--- model.py        It contains the implementation of the MNBN/CNBN models  
    |
    |--- metrics.py      It contains all utilites that have been used to compute the metrics
    |
    |--- guessLang.py    This is the external module to predict the programming language of a repository
    |
    |--- lang_file.txt   This file contains the language for each repository computed by guessLang module
    |
    |--- topics_134.txt  This file contains the featured topics considered in the evaluation   

```




# Running the MNBN

To replicate the experiments shown in the paper, you have to edit the following paths **main.py**:

- train_dir = path for a single round of training 
- test_dir = path for a single round of testing
- out_file = name for the average metrics values computed 
- num_tags = interger that represents the number N of recommended items 
- model = string for choosing the model to run ('MNB' or 'CNB')












