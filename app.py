from flask import Flask,render_template,redirect,request,url_for,flash
from flask_mail import Mail,Message
# import pyautogui as pag
# from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'supersecretkey'
mail=Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vysakh7995@gmail.com' # Replace with your email
app.config['MAIL_PASSWORD'] = 'cqad lqjy swuy zxwy' # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = ('Vysakh', 'vysakh7995@gmail.com') # Replace with your default sender email
# app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail=Mail(app)

@app.route('/')
def index():
    # flash("!! Messege sent successfull I will contact you as soon as possible !!","success")

    return render_template('index.html')

# if __name__ == '__main__':
# app.run(port=5001,debug=True)

# Configuration settings for Flask-Mail


@app.route('/contact_me', methods=['POST'])
def contact_me1():
    print("Contactme")
    if request.method=='POST':
        print(request)
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject, recipients=['elayedathvysakh@gmail.com'],sender='vysakh7995@gmail.com') # Replace with recipient email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"
        print(name,email,subject,message)
        mail.send(msg)
        flash("!! Messege sent successfull I will contact you as soon as possible !!","success")
        
    
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
