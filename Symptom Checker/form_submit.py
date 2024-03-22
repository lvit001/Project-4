import pandas as pd
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request
def format_result(prediction):
  prediction = prediction[0]
  for i in range(0, len(prediction)):
    prediction[i] = round(prediction[i] * 100, 2)
    if prediction[i] < 0.1:
      prediction[i] = 0.0
  disease_dict = {"Allergy": str(prediction[0]) + "%",
                  "Drug Reaction": str(prediction[1]) + "%",
                  "Migraine": str(prediction[2]) + "%",
                  "Common Cold": str(prediction[3]) + "%",
                  "Pneumonia": str(prediction[4]) + "%",
                  "Heart attack": str(prediction[5]) + "%",
                  "Fungal infection": str(prediction[6]) + "%",
                  "Hypoglycemia": str(prediction[7]) + "%",
                  "Urinary tract infection": str(prediction[8]) + "%",
                  "Chicken pox": str(prediction[9]) + "%"}
  return disease_dict
  


def predict_disease(symptoms):
  df = pd.read_csv('encoded_data.csv')
  y = pd.get_dummies(df['Disease'])
  X = df.drop(columns='Disease')
  regression = LinearRegression()
  regression.fit(X,y)
  print (regression.predict([symptoms]))
  #return str(format_result(regression.predict([symptoms])))
  return format_result(regression.predict([symptoms]))

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
  return render_template('result.html', result = result)
  


if __name__ == '__main__':
  app.run(debug=True)

