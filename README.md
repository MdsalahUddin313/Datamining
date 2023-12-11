# Data Mining Project
Our project objective is to implement Apriori algorithm and FP growth algorithms .Later comparing models with various experiments.  
This project contains the following components:
## Groceries Results
Results of data mining on groceries dataset with different confidence and support values:
- `CONF(0.1) SUP(0.005)`
- `CONF(0.05) SUP(0.05)`
- `CONF(0.25) SUP(0.05)`

## Store Results
Results of data mining on store dataset with different confidence and support values:
- `CONF(0.1) SUP(0.0045)`
- `CONF(0.05) SUP(0.045)`
- `CONF(0.25) SUP(0.05)`

## Virtual Environment

The `venv` directory contains the Python virtual environment for this project.
## Datasets
The `Datasets` directory contains the following datasets:
- `Groceries.csv`: The groceries dataset.
- `store.csv`: The store dataset.
## Scripts
The following Python scripts are included in this project:
- `AprioriAlgo.py`: This script implements the Apriori algorithm.
- `Fpgrowth.py`: This script implements the FP-Growth algorithm.
- `main.py`: This is the main script that runs the project.
## Results Analysis
Blue line represents FP-growths
Yellow/Red lines represents Apriori algorithm
![For Store dataset (S=0.05mC=0.25)](https://github.com/MdsalahUddin313/Datamining/blob/main/StoreResults/Conf(0.25)SUP(0.05)/Figure_2.png)
![For Groceries dataset (S=0.05mC=0.25)](https://github.com/MdsalahUddin313/Datamining/blob/main/GroceriesResults/CONF(0.25)SUP(0.05)/FPgrowth_vs_aprioiry.JPG)