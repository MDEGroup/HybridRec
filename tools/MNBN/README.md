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


Notice that guesslang module requires Python 3.6. More information about this module can be found [here](https://pypi.org/project/guesslang/)


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

```




# Running the MNBN

In **MavenMain.py**, you have to edit the following paths:

- train_dir = "path_to_train_folder"
- test_dir = "path_to_test_folder"
- out_file = "name_of_output_file"


After the train data is loaded, you have to modify the following parameters in the predict_topics function: 

- dirs: the root folder that contains the test files
- test_dir: the test folder for a single round
- train_dir: the train folder for a single round
- labels: the list of topics to predict
- num_topics: number of predicted topics
- list_test: a txt file that contains the name of repository to test (available together with the datasets)

The output is a CSV files with all the metrics presented in the work:
- success rate (1..10)
- precision
- recall









