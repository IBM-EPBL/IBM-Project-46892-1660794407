
from flask import Flask, render_template      

app = Flask(__name__)
    
@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/base")
def base():
    return render_template("base.html")
    
if __name__ == "__main__":
    app.run(debug=True)
