from flask import Flask,request,render_template
app = Flask(__name__)

users=["luigi","gianni","maria"]
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] in users:
            return render_template("hallo.html",nome=request.form['username'])
        else:
            return "Non autorizzato"
    else:
        return render_template("login.html")
