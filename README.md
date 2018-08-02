# Drug Repurposing

This project computes the prediction probability of whether a compound will treat a disease. In another term, the project deals with repurposing the drugs to a disease, which is not a treatment at the moment.

## Prerequisites

In order to run the assests you will need the following:

* Install [Neo4j](https://neo4j.com)
* Python 3
* R

## NoteBooks

1. [Drug_Disease_HomogeneousPlot.py](https://github.com/SarveshP/Drug_Repurposing/blob/master/Drug_Disease_HomogeneousPlot.py) - Runs the homogeneous plot for the Drug and Disease pairs.
2. [Drug_Gene_HomogeneousPlot.py](https://github.com/SarveshP/Drug_Repurposing/blob/master/Drug_Gene_HomogeneousPlot.py) - Runs the homogeneous plot for the Drug and Gene pairs.
3. [Merging_Features.ipynb](https://github.com/SarveshP/Drug_Repurposing/blob/master/Merging_Features.ipynb) - Merges the features extracted from network and transforms them to [transformed-features.csv](https://github.com/SarveshP/Drug_Repurposing/blob/master/transformed-features.csv).
4. [Drug_Repurposing_Model.Rmd](https://github.com/SarveshP/Drug_Repurposing/blob/master/Drug_Repurposing_Model.Rmd) - Creates and run the model for predictions.

## Components

* [Data](https://github.com/SarveshP/Drug_Repurposing/tree/master/Data) - the directory containing all the input csv files.
* [Neo4j](https://github.com/SarveshP/Drug_Repurposing/tree/master/Neo4j) - the directory containing the data and code files to run the scripts in Neo4j.
* [Viz](https://github.com/SarveshP/Drug_Repurposing/tree/master/Viz) - the directory containing all the network vizualizations

## Authors

* **Sarvesh Prattipati**

## Acknowledgments

* **Daniel Himmelstein**
