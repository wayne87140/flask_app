from flask import render_template, redirect, flash, url_for
from flaskr import app
from flaskr.forms import LoginForm

@app.route('/')
@app.route('/homepage')
def homepage():
    user =  {'username' : 'Wayne'}
    return render_template('homepage.html', title = 'Home', user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user { form.username.data }, remember_me {form.remember_me.data}')
        return redirect(url_for('homepage'))
    return render_template('login.html', title = 'Login', form=form)
