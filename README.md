# Project 4: Healthcare Machine Learning
## Project Overview
Group 6 analyzed a dataset containing symptoms that correspond to certain diseases. They sought to create a machine-learning model that predicts a patient's potential disease based on their symptoms. The group developed and compared a few machine-learning models and determined which one most accurately predicts diseases based on symptoms.

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
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/cd9e0cbe-154f-46d4-b443-1dbde2646eec)
6. The y dataset was cleaned next by first converting the string disease values to integers between 0-9. This was done as machine learning models required numerical data.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/4060b96e-582a-4f37-8a28-a6bacabb3769)
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/7312e1fb-2cde-4136-b70e-5915db26e79a)
7.  Once both datasets were cleaned, they were concatenated and saved to a CSV file.
8.  The encoded CSV file was then converted to a SQLite database
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/2f543dfa-a16b-4b04-931a-b15ce08f5044)

## Machine Learning Model 1: Neural Network
### Data Pre-Processing
For the neural network, additional pre-processing was required for the output data:
1. The data was loaded in from the diseases.sqlite database and converted to a pandas dataframe.
2. The data was split into X and y variables, with X once again representing the symptoms and y representing the diseases.
3. The data was then split into training and testing datasets with `train_test_split(X, y, random_state=42, stratify=y)`
4. The y_train and y_test datasets were converted to binary arrays using `to_categorical`
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/b629d024-7c86-49a4-b51d-b281c8e7ea26)

### Compiling, Training, and Evaluating the initial Model
- Total Number of Layers:
    - **1st Hidden Layer** (10 nodes; relu activation function; 10 input dimensions)
    - **2nd Hidden Layer** (10 nodes; relu activation function)
    - **Output Layer** (10 output nodes; softmax activation function)
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/3f7091de-d90c-4f30-9b70-b72d2d246696)
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/22063c0f-5b00-4e20-b8f4-9bc0c4bcf12d)
- Was the target model performance achieved?
    - Yes, the model initially had a 98% accuracy.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/f0598167-1b5f-4a16-9adf-99d110aba437)

### Model Optimization
- The model was optimized as follows:
    - 1st Hidden Layer increased to **20 nodes**.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/74bd8074-f2ae-49e1-803d-99b4da633ccc)
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/27492491-9d92-4cda-aeba-a08fbb074fe3)
- Was the target model performance achieved?
    - Yes, the model reached 100% accuracy.
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/f1dbce41-eded-42ea-a546-288805578773)

 ### Model Summary
 The neural network model performed excellently, reaching an accuracy score of 100% after minimal optimization. 

## Machine Learning Model 2: Logistic Regression
### Data Pre-Processing
Data preparation & extraction included reading in the 'diseases.sqlite' database into the pandas dataframe.
Next, the data was split into training and testing sets. 

### Compiling, Training, and Evaluating the initial Model
The columns (X) were extracted from the DataFrame, excluding the disease column. The disease column was used as labels (y). The data was split into 80% training and 20% testing sets using train_test_split.
A logistic regression model was trained using the training data (X_train and y_train), and evaluated through calculating accuracy, generating a confusion matrix, and classification report.

### Model Summary
The model achieved an accuracy of 100%, indicating perfect predictions on the testing set.
                  precision    recall  f1-score   support
    
       Disease 0       1.00      1.00      1.00        21
       Disease 1       1.00      1.00      1.00        26
       Disease 2       1.00      1.00      1.00        24
       Disease 3       1.00      1.00      1.00        23
       Disease 4       1.00      1.00      1.00        23
       Disease 5       1.00      1.00      1.00        33
       Disease 6       1.00      1.00      1.00        19
       Disease 7       1.00      1.00      1.00        22
       Disease 8       1.00      1.00      1.00        24
       Disease 9       1.00      1.00      1.00        25
    
        accuracy                           1.00       240
       macro avg       1.00      1.00      1.00       240
    weighted avg       1.00      1.00      1.00       240
For further details, refer to the code and documentation provided in this repository.


## Resources
### Pre-Processing Code
- Code `str.lstrip` to remove excess string from symptom headers found [here](https://stackoverflow.com/questions/55679401/remove-prefix-or-suffix-substring-from-column-headers-in-pandas).
- Code `X.groupby(level=0,axis=1).sum()` to add columns with the same column title and remove duplicates found [here](https://stackoverflow.com/questions/58809851/how-can-i-add-the-values-of-pandas-columns-with-the-same-name). 
