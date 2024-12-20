from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Simulate saving or sending the contact message
    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    flash("Thank you for reaching out! We will get back to you soon.", "success")
    return redirect(url_for('home'))
    # return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
