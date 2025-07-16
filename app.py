from flask import Flask, request, render_template, jsonify, session, redirect, url_for, flash;
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keykeydoyouloveme'

@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    return render_template('home.html')

@app.route('/tow', methods=['GET', "POST"])
def tow():
    return render_template('tow.html')

@app.route('/bodyShop', methods=['GET', "POST"])
def bodyShop():
    return render_template('bodyShop.html')

"""
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        message = request.form['message']
        # Normally you'd send an email or save to a DB here
        flash("Request submitted successfully!")
        return redirect(url_for('success'))
    return render_template('contact.html')
    """

@app.route('/about', methods=['GET', "POST"])
def about():
    return render_template('about.html')

@app.route('/contactUs', methods=['GET', "POST"])
def contactUs():
    return render_template('contactUs.html')

@app.route('/success', methods=['GET', "POST"])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)