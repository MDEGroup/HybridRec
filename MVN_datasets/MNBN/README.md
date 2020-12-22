# Dataset and experiments

This [link](https://drive.google.com/drive/folders/197LCCfBTcpbqqaPfxO4C8V0t3f-XFnKT) contains all the datasets used in the evaluation as well as the results in CSV format. The table below shows the composition for each dataset:

| Dataset | # of testing file | # of training files |
|---------|-------------------|---------------------|
| D1      | 134               | 1,206               |
| D2      | 670               | 6,030               |
| D3      | 1,340             | 12,060              |


As discussed in the paper, we have build three different dataset by variating the number of files used in the training phase as shown in the table above. The structure is the following:

```
evaluation

test_files
    .
    |--- test_files_D1/            It contains the test projects of D1 for each evaluation round
    |
    |--- test_files_D2/            It contains the test projects of D2 for each evaluation round
    |
    |--- test_files_D3/            It contains the test projects of D3 for each evaluation round

results
    .
    |--- validation_10/            It contains the results computed for D1  
    |
    |--- validation_50/            It contains the results computed for D2 
    |
    |--- validation_100/           It contains the results computed for D3 


evaluation structure
    .
    |--- ten_folder_10.rar/        The ten-folder structure for D1
    |
    |--- ten_folder_50.rar/        The ten-folder structure for D2
    |
    |--- ten_folder_100.rar/       The ten-folder structure for D3
    
```