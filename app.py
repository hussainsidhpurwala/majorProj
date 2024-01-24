from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

app.run(debug=True)