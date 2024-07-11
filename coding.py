from flask import Flask,render_template,redirect,request,url_for
# from flask_mail import Mail,Message

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# # Configuration settings for Flask-Mail
# app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Replace with your SMTP server
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'vysakh7995@gmail.com' # Replace with your email
# app.config['MAIL_PASSWORD'] = 'dkdm njdk qnom bxaj' # Replace with your email password
# app.config['MAIL_DEFAULT_SENDER'] = ('Vysakh', 'vysakh7995@gmail.com') # Replace with your default sender email


# @app.route('/contact_me', methods=['POST'])
# def contact_me():
    


#     name = request.form['name']
#     email = request.form['email']
#     subject = request.form['subject']
#     message = request.form['message']

#     msg = Message(subject, recipients=['vysakh7995@gmail.com']) # Replace with recipient email
#     msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
#     Mail.send(msg)

#     # Process the form data (e.g., print to console, save to database, etc.)
#     print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
    
#     return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
