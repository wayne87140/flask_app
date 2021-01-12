from flask import render_template
from flaskr import app

@app.route('/')
@app.route('/index')
def homepage():
    user =  {'username' : 'Wayne'}
    posts = ['A post', 'B post', 'C post']
    return render_template('index.html', title = 'Index', user = user, posts = posts)
