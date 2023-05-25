from flask import Flask, render_template, request, jsonify
import requests
from translate import Translator
from googletrans import Translator
from googletrans import Translator, LANGUAGES
import pandas as pd


translator = Translator()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')


i = 0
@app.route('/get_response', methods=['POST'])
def get_response():
   
    symptoms = list()
    symptoms_list = ['Symptom_1', 'Symptom_2', 'Symptom_3']

    csv_file_path ='static\dataset.csv'
    df = pd.read_csv(csv_file_path)

    prompt = ['one more symp', 'symp_please', 'ek aur']
    # Process the user's input and generate a response
    user_input = request.form['user_input']
    symptoms.append(user_input) 

    # 


    
    
    global i
    i += 1

    #filtered_data = df[df[symptoms_list[i].strip()] == symptoms[i-1]]

    # Perform chatbot logic here
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(user_input, src='hi', dest='hi')
    translated_text = translation.text
    # Return the translated text as the response

    # if len(symptoms) == 4:
    #     unique_value = filtered_data.iloc[:, 0].drop_duplicates()
    #     return jsonify({'response': unique_value[0]})
    
    return jsonify({'response': translated_text})


###################################################################################
########### NameGenerator ############################
pref = ["ine", "phen", "aid", "phan", "sin", "cea", "nna", "mine", "ara", "rave", "quel", "igil", "opin", "gam", "tine", "igil", "done", "pam", "bate", "trin", "toin", "trel", "pam", "cin", "trim"]


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        suggested_name = request.form['suggested']
        ingredient_used = request.form['ingred']
        country_name = request.form['country']
        number = int(request.form['number'])

        data = [number, suggested_name, ingredient_used]

        return render_template('result.html', data = data, pref=pref)

    return render_template('name.html')


@app.route('/result', methods=['POST'])
def result():
    suggested_name = request.form['suggested']
    ingredient_used = request.form['ingred']
    country_name = request.form['country']
    number = int(request.form['number'])

    data = [number, suggested_name, ingredient_used]

    return render_template('result.html', data=data, pref=pref)




if __name__ == '__main__':
    app.run(debug=True)
