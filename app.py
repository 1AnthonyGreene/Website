from flask import Flask, request, render_template, jsonify, session, redirect, url_for, flash;
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
import os
"""Google birthday: 5/15/1985"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'keykeydoyouloveme'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
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

@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    if request.method == 'POST':
        fName = request.form.get('fName')
        lName = request.form.get('lName')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        fullName = f"{fName} {lName}".strip()
        msg = Message(
            subject="New Contact Form Submission",
            sender=app.config['MAIL m89iu70o-p=, .l_USERNAME'],
            recipients=['harrysbodyshopinc@att.com']
        )
        msg.body = f"From: {fullName} <{email}>\nPhone: {phone}\n\n{message}"

        
        try:
            mail.send(msg)
            print("Message sent successfully!", "success")
        except Exception as e:
            print(f"Failed to send message: {str(e)}", "error")
        

        return redirect('/contactUs')

    return render_template('contactUs.html')

@app.route('/success', methods=['GET', "POST"])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)