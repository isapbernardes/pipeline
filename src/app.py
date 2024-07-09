from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {"admin": "password"}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("home"))
        else:
            return "Invalid credentials", 401
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

