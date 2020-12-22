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





# Code structure 

This folder contains the source code of the tool structured as follows:
```
MNBN
    .
    |--- MavenMain.py   It is used to run the tools      
    |
    |--- model.py     This file performs the training and testing phases. It also produces the needed files to compute the metrics presented in the paper
    |
    |--- utilites.py   	It contains all functions that have been used to run the tool
    |
    |--- lib_tags.csv   This file is used for evaluation purposes

```




# Running the MNBN

To replicate the experiments shown in the paper, you have to edit the following paths **MavenMain.py**:

- train_dir = path for a single round of training 
- test_dir = path for a single round of testing
- out_file = name for the average metrics values computed 
- num_tags = interger that represents the number N of recommended items 


After the train data is loaded, youcan run the **evaluation** function to compute the following metrics: 
- success rate (1..N)
- precision
- recall









