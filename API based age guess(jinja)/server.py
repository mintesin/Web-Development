from flask import Flask,render_template
import datetime as dt
import requests
import random
app=Flask(__name__)

@app.route('/')
def home():
    number=random.choice(list(range(20)))
    num=number*2
    dat=dt.date.today().year
    return "Enter your name"

@app.route('/guess/<name>')
def Guess(name):
    header={'name':name}
    api_one='https://api.agify.io?' #API use to guess the age of a person based on his/her name
    api_two='https://api.genderize.io/?' #API use to guess the gender of a person based on his/her name
    request_gender=requests.get(api_two,params=header)
    request_age=requests.get(api_one,params=header)
    data_gender=request_gender.json()['gender']
    data_age=request_age.json()['age']
    return render_template('index.html',name=name,gender=data_gender,age=data_age ) #returning the age and gender





if __name__=='__main__':
    app.run(debug=True,use_reloader=True)
