import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
def format_result(prediction):
  disease_list = ['Allergy', 'Drug Reaction', 'Migraine', 'Common Cold', 
                  'Pneumonia', 'Heart attack', 'Fungal infection',
                  'Hypoglycemia', 'Urinary tract infection', 'Chicken pox']
  
  disease = disease_list[prediction[0]]

  return disease
  


def predict_disease(symptoms):
  df = pd.read_csv('encoded_data.csv')
  y = df["Disease"]
  X = df.drop(columns="Disease")
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  logistic_model = LogisticRegression()
  logistic_model.fit(X_train, y_train)
  return format_result(logistic_model.predict([symptoms]))
  

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('symptom_checker.html')

@app.route('/submit/', methods = ['POST'])
def submit():
  
  symptom_list = []
  for i in range(0, 51):
    symptom = request.form.get("checkbox" + str(i))
    if symptom:
      symptom_list.append(1)
    else:
      symptom_list.append(0)

  result = predict_disease(symptom_list)
  #html for result template
  #https://stackoverflow.com/questions/14652325/python-dictionary-in-to-html-table
  return render_template('result.html', result = result)


if __name__ == '__main__':
  app.run(debug=True)
