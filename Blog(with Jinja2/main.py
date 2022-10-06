from flask import Flask,render_template,url_for,request
from data import data
import datetime
import time
import jinja2
import requests
# url='https://www.npoint.io/docs/4a937eb8edf3a8d9dedb'
# response=requests.get(url)

json_data=data
EMAIL=your_email
PASSWORD=your PASSWORD
app=Flask(__name__)
# HOME PAGE
@app.route('/')
def Home():
    data=json_data
    # date=datetime.date.today()
    return render_template('index.html', file=data)
# RENDERING SINGLE POST ON POST TEMPLATE TO DISPLAY
@app.route('/post/<int:index>')
def single_post(index):
    print(index)
    blog=json_data[index]
    return render_template('post.html',blg=blog)
@app.route('/About')
def about():
     return render_template('about.html')
# GETTING THE CONTACT DETAILS USING POST METHOD AND SENDING EMAIL
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data=request.form
        msg="The message was successfully sent"
        send_email(data['name'],data['email'],data['number'],data['message'])
        return render_template('contact.html', msg=msg)
    return render_template("contact.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD) #LOGGING IN
        connection.sendmail(EMAIL, EMAIL, email_message) #SENDING EMAIL TOWARDS SELF


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080,use_reloader=True)
