from flask import Flask,render_template,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateTimeField
from wtforms.validators import DataRequired,Email
from flask_bootstrap import Bootstrap

# DEFINING THE FORM CLASS
class Form(FlaskForm):
    username=StringField(label='username',validators=[DataRequired(),Email()])
    password=PasswordField(label='password',validators=[DataRequired()])

    submit=SubmitField(label='Login')


app=Flask(__name__)
app.secret_key='minte'
Bootstrap(app)

# HOME FUNCTION
@app.route('/')
def home():
    return render_template('index.html')

# DEFINING THE LOGIN PAGE
@app.route('/login',methods=['GET','POST'])
def login():
    form=Form()
    if request.method=='POST' and form.validate_on_submit():
        if form.username.data=='admin@email.com' and form.password.data=='12345678':
            return render_template('success.html')
        else: return render_template('denied.html')

    form.validate_on_submit()
    
    return render_template('login.html',form=form)

# RUNNING THE APP
if __name__=='__main__':
    app.run(debug=True,use_reloader=True)




