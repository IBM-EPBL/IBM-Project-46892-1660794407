
from flask import Flask, render_template      

app = Flask(__name__)
    
@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/updatestocks")
def updatestocks():
    return render_template("updatestocks.html")
    
if __name__ == "__main__":
    app.run(debug=True)
