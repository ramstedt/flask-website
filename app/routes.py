from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def landing_page():
    return render_template('landing.html')
@app.route('/about')
def about_page():
    return render_template('about.html') 