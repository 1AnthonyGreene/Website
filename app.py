from flask import Flask, request, render_template, jsonify, session, redirect, url_for, flash;
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
import os
"""Google birthday: 5/15/1985
Harryscontactmail@gmail.com
YnbdZ%fp52a_

AP: lwyu xzma kbrh doro
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'keykeydoyouloveme'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['Mail_Username']
app.config['MAIL_PASSWORD'] = os.environ['Mail_Password']

mail = Mail(app)

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
    if request.method == 'POST':
        fName = request.form['fName']
        lName = request.form['lName']
        if request.form['phone']:
            phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']


        msg = Message("New Contact Form Submission", 
                      sender=os.environ['Mail_Username'],
                      recipients=["harrysbodyshop@att.com"])
        fullName = fName + " " + lName
        msg.body = f"From: {fullName} <{email}>\n\n{message}"
        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send message: {str(e)}", "error")
        return redirect('contactUs')
        
    return render_template('contactUs.html')

@app.route('/success', methods=['GET', "POST"])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)