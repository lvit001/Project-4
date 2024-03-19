# Project 4: Healthcare Machine Learning
## Project Overview
Group 6 analyzed a dataset containing symptoms that correspond to certain diseases. They sought to create a machine-learning model that predicts a patient's potential disease based on their symptoms. The group developed and compared a few machine-learning models and determined the one that most accurately predicts diseases based on symptoms.

## Data Set
The group utilized a dataset from [Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=dataset.csv). The initial dataset contained a column with the disease name and columns for the related symptoms (up to 17 symptoms per disease). There were 41 different diseases and 120 rows for each disease.
![image](https://github.com/lvit001/Project-4/assets/140283164/6e489f25-910d-4825-9766-cbc0c96ce9c5)

## Data Pre-Processing
To prepare the dataset for machine learning, the following pre-processing steps were taken:

1. The group decided to use 10/41 diseases, so the data frame was filtered for the following diseases:
    - Allergy
    - Drug Reaction
    - Migraine
    - Common Cold
    - Pneumonia
    - Heart Attack
    - Fungal Infection
    - Hypoglycemia
    - Urinary Tract Infection
    - Chicken Pox 
2. The data was broken into X and y data frames, with X representing the features and y representing the output.
    - X = Disease Column
    - y = Symptom Columns
3. The X dataset was encoded first using `pd.get_dummies(X, dtype=int)`. This resulted in 127 columns of symptoms, which would need the titles cleaned and duplicate symptom columns combined. The value 1 represented the presence of a symptom and 0 represented the absence.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/49a89dd2-917f-4b62-94e0-b7e28a2ab5cc)
4. The `Symptom_X_` prefix was removed from all the columns to leave only the symptom name.
5. The duplicate columns were combined via addition through `X=X.groupby(level=0,axis=1).sum()`.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/8b576778-3815-448d-8df7-518ea92a9a9c)
6. The y dataset was cleaned next by first converting the string disease values to integers between 0-9.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/4060b96e-582a-4f37-8a28-a6bacabb3769)
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/7312e1fb-2cde-4136-b70e-5915db26e79a)
7.  



## Resources
### Pre-Processing Code
- Code `str.lstrip` to remove excess string from symptom headers found [here](https://stackoverflow.com/questions/55679401/remove-prefix-or-suffix-substring-from-column-headers-in-pandas).
- Code `X.groupby(level=0,axis=1).sum()` to add columns with the same column title and remove duplicates found [here](https://stackoverflow.com/questions/58809851/how-can-i-add-the-values-of-pandas-columns-with-the-same-name). 
