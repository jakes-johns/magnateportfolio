from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv(override=True)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Configure Flask-Mail
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contacts/')
def contacts():
    return render_template('contact.html')

@app.route('/more/')
def more():
    return render_template('learn_more.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Construct the email
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_ADDRESS
            msg['Subject'] = f"Contact Form Submission from {name}"

            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Secure the connection
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            flash('Your message has been sent successfully! I will get back to you in a few.', 'success')
            return render_template('index.html')

        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred while sending your message. Please try again later.', 'danger')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
