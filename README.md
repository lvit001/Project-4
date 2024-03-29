# Project 4: Healthcare Machine Learning
## Project Overview
Group 6 analyzed a dataset containing symptoms that correspond to certain diseases. They aimed to create a machine-learning model that can predict a patient's potential disease based on their symptoms. The group developed and compared a few machine-learning models to find the most accurate one. Once they had a successful model, they developed a Flask API using the machine learning model to predict a user's disease based on their inputs.

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
7.  Once cleaned, both datasets were concatenated and saved to a CSV file.
8.  The encoded CSV file was then converted to a SQLite database
    - ![image](https://github.com/lvit001/Project-4/assets/140283164/2f543dfa-a16b-4b04-931a-b15ce08f5044)
  

## Data Analysis
The data was analyzed by comparing commonly occurring symptoms (present in 3 or more diseases) by disease. A Tableau side-by-side bar chart was used to visualize the data [here](https://public.tableau.com/app/profile/lori.vitaioli/viz/Disease-SymptomComparison/SharedSymptoms?publish=yes).

![image](https://github.com/lvit001/Project-4/assets/140283164/640139c4-4751-45f8-95d6-e70d542b5929)

### Initial Observations:
1. Common Cold and Pneumonia share 4 out of 7 of the common symptoms being analyzed
2. Drug Reaction and Fungal Infection patients commonly report itching and skin rash
3. Urinary Tract Infection did not share any common symptoms with the other diseases in the dataset. Of the four reported symptoms of UTIs, only Drug Reaction shared one of the symptoms (burning micturition)

![image](https://github.com/lvit001/Project-4/assets/140283164/506ad2c1-ad0e-4970-9406-9946daef10a2)

## Machine Learning Model 1: Linear Regression
### Data Pre-Processing
For data pre-processing, data was read into a Pandas dataframe from a SQLite file.

### Compiling, Training, and Evaluating the initial Model
The data was split into X and y variables, y being the disease column and x being everything else. Afterwards, the y value was divided into 10 dummy columns and the X and y values were used to train a multiple LinearRegression() model.

### Model Summary
Details can also be found in the "Machine Learning Models" directory multiple_regression.ipynb file

The score is 0.9876581493722678.\
The r2 is 0.9876581493722678.\
The mean squared error is 0.001110766556495892.\
The root mean squared error is 0.03332816461337006.\
The standard deviation for each disease is:\
0: 0.3\
1: 0.3\
2: 0.3\
3: 0.3\
4: 0.3\
5: 0.3\
6: 0.3\
7: 0.3\
8: 0.3\
9: 0.3

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

## Machine Learning Model 3: Random Forest
### Data Pre-Processing

For the initial Random Forest, no additional pre-processing was needed and the data was pulled directly from SQL into Python.  The data was split into testing and training sets and a random forest classifier was created.

![Screenshot 2024-03-21 204138](https://github.com/lvit001/Project-4/assets/145800386/94c10ea7-b015-47c4-9046-421ab9b115d6)

The features (X) were the disease symptoms, and the target vector (y) was the diseases themselves.  The 10 randomly chosen diseases from earlier were used for this model and a random forest regressor was created as well to control over-fitting, but yielded the same results.

![Screenshot 2024-03-21 204331](https://github.com/lvit001/Project-4/assets/145800386/ec7324aa-a7e9-4daa-866f-873eefd28bf6)

### Model Summary
Similar to other Machine Learning Models, the Random Forest generated an accuracy of 100% indicating perfect predictions on the testing data.  

![Screenshot 2024-03-21 204955](https://github.com/lvit001/Project-4/assets/145800386/49e15fef-5d09-44b1-a6d2-b0889c89cb53)

![Screenshot 2024-03-21 204118](https://github.com/lvit001/Project-4/assets/145800386/a782a318-79ea-400f-bafd-147a7020ab17)

![Screenshot 2024-03-21 211951](https://github.com/lvit001/Project-4/assets/145800386/92e159f1-573d-4571-9d05-fad5cd4497e1)

## Machine Learning Model 4: Neural Network
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

## Flask API Details
### Summary
The Flask API re-implements the logistic regression model found in the "Machine Learning Models" directory "Logistic Regression.ipynb" and allows users to select from a list of 51 symptoms. After the user submits their list of symptoms, the model will predict the disease most likely present from our list of 10 diseases.
### How to use
- Run the log_regression.py file from the "Symptom Checker" directory
- Open localhost in your browser
- Click the checkboxes to indicate symptoms
- Click submit to see the results
### Limitations
The model only shows the most likely result but doesn't show how likely that result actually is. Also, the model only has 10 total diseases to compare against

## Conclusion
### ¾ of the machine learning models achieved 100% accuracy
The models were able to easily interpret the dataset due to the consistency of symptoms for each disease
### Limitations
Only selecting 10/41 diseases in the dataset means the model is limited in what it can predict
### What's next?
- Add more data to the model: the other 31 diseases not initially included and more beyond those
- Machine learning models like these can assist medical professionals when diagnosing patients, which can lead to more efficient treatment. However, a model alone should not be used as a diagnosis tool

## Resources
### Pre-Processing Code
- Code `str.lstrip` to remove excess string from symptom headers found [here](https://stackoverflow.com/questions/55679401/remove-prefix-or-suffix-substring-from-column-headers-in-pandas).
- Code `X.groupby(level=0,axis=1).sum()` to add columns with the same column title and remove duplicates found [here](https://stackoverflow.com/questions/58809851/how-can-i-add-the-values-of-pandas-columns-with-the-same-name).

### Machine Learning Code
- Code for creating X and y values for a multiple regression [here](https://www.w3schools.com/python/python_ml_multiple_regression.asp)
- Random Forest Visualization assistance [here](https://www.codementor.io/@mgalarny/visualizing-decision-trees-with-python-scikit-learn-graphviz-matplotlib-154mszcto7)

### Flask API Code
- Template for the results in the API page [here](https://stackoverflow.com/questions/14652325/python-dictionary-in-to-html-table)
- Code for starting a flask api [here](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)
- Code for creating checkboxes in html [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)
