# Project 4: Healthcare Machine Learning
## Project Overview
Group 6 analyzed a dataset containing symptoms that correspond to certain diseases. They sought to create a machine-learning model that predicts a patient's potential disease based on their symptoms. The group developed and compared a few machine-learning models and determined the one that most accurately predicts diseases based on symptoms.

## Data Set
The group utilized a dataset from [Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=dataset.csv). The initial dataset contained a column with the disease name and columns for the related symptoms. There were 41 different diseases and 120 rows for each disease.
![image](https://github.com/lvit001/Project-4/assets/140283164/6e489f25-910d-4825-9766-cbc0c96ce9c5)



## Resources
### Pre-Processing Code
- Code `str.lstrip` to remove excess string from symptom headers found [here](https://stackoverflow.com/questions/55679401/remove-prefix-or-suffix-substring-from-column-headers-in-pandas).
- Code `X.groupby(level=0,axis=1).sum()` to add columns with the same column title and remove duplicates found [here](https://stackoverflow.com/questions/58809851/how-can-i-add-the-values-of-pandas-columns-with-the-same-name). 
