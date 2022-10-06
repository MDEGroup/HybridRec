# HybridRec Replication package

  
  

This repository contains the replication package and dataset of the paper entitled **HybridRec: A recommender system for tagging GitHub repositories** which has been published in the Springer Applied Intelligence Journal.

  

All the resources, including the tool, the dataset, and the article have been realized by:

- Juri Di Rocco
- Davide Di Ruscio
- Claudio Di Sipio
- Phuong T. Nguyen
- Riccardo Rubei

  
  

# Structure of the repository

The repository is structured as follows:  
  
```
|--- Datasets This folder contains all the datasets used in the evaluation
|--- HybridRec This folder contains the source code of the two modules presented in the paper, i.e., CNBN and TopFilter.
```

It is worth noting that each tool has a dedicated README file that explains how to replicate the results reported in the paper.

  
    

## How to cite

If you find our work useful for your research, please cite the paper using the following BibTex entry:

  

```
@article{di_rocco_hybridrec_2022,
title = {{HybridRec}: {A} recommender system for tagging {GitHub} repositories},
issn = {1573-7497},
url = {https://doi.org/10.1007/s10489-022-03864-y},
doi = {10.1007/s10489-022-03864-y},
abstract = {Software repositories are increasingly essential to support the management of typical artifacts building up projects, including source code, documentation, and bug reports. GitHub is at the forefront of this kind of platforms, providing developer with a reservoir of code contained in more than 28M repositories. To help developers find the right artifacts, GitHub uses topics, which are short texts assigned to the stored artifacts. However, assigning inappropriate topics to a repository might hamper its popularity and reachability. In our previous work, we implemented MNBN and TopFilter to recommend GitHub topics. MNBN exploits a stochastic network to predict topics, while TopFilter relies on a syntactic-based function to recommend topics. In this paper, we extend our work by building HybridRec, a recommender system based on stochastic and collaborative-filtering techniques to generate more relevant topics. To deal with unbalanced datasets, we employ a Complement Naïve Bayesian Network (CNBN). Furthermore, we apply a preprocessing phase to clean and refine the input data before feeding the recommendation engine. An empirical evaluation demonstrates that HybridRec outperforms three state-of-the-art baselines, obtaining a better performance with respect to various metrics. We conclude that the conceived framework can be used to help developers increase their projects’ visibility.},
journal = {Applied Intelligence},
author = {Di Rocco, Juri and Di Ruscio, Davide and Di Sipio, Claudio and Nguyen, Phuong T. and Rubei, Riccardo},
month = aug,
year = {2022}}
```