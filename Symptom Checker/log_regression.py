import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
def format_result(prediction):
  print('prediction is' + str(prediction))
  disease = ""
  if prediction == 0:
    disease = 'Allergy'
  elif prediction == 1:
    disease = 'Drug Reaction'
  elif prediction == 1:
    disease = 'Migraine'  
  elif prediction == 1:
    disease = 'Common Cold'  
  elif prediction == 1:
    disease = 'Pneumonia'  
  elif prediction == 1:
    disease = 'Heart attack'  
  elif prediction == 1:
    disease = 'Fungal infection'  
  elif prediction == 1:
    disease = 'Hypoglycemia'  
  elif prediction == 1:
    disease = 'Urinary tract infection'  
  else:
    disease = 'Chicken pox'  

  return disease
  


def predict_disease(symptoms):
  df = pd.read_csv('encoded_data.csv')
  print(1)
  y = df["Disease"]
  print(2)
  X = df.drop(columns="Disease")
  print(3)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  print(4)
  logistic_model = LogisticRegression()
  print(5)
  logistic_model.fit(X_train, y_train)
  print(6)
  print (logistic_model.predict([symptoms]))
  #return str(format_result(regression.predict([symptoms])))
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
      print(symptom_list)
  print(symptom_list)
  result = predict_disease(symptom_list)
  #return (result)
  #html for result template
  #https://stackoverflow.com/questions/14652325/python-dictionary-in-to-html-table
  #return render_template('result.html', result = result)
  return(result)
  


if __name__ == '__main__':
  app.run(debug=True)
