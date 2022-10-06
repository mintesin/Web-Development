from flask import Flask,render_template,url_for
from data import data

import time
import jinja2

json_data=data
# print(data)
#
app=Flask(__name__)
@app.route('/')
def Home():
    data=json_data
    # date=datetime.date.today()
    return render_template('index.html', file=data)
@app.route('/post/<int:index>')
def single_post(index):
    print(index)
    blog=json_data[index]
    return render_template('post.html',blg=blog)
@app.route('/About')
def about():
     return render_template('about.html')
@app.route('/contact')
def Contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True,use_reloader=True)
