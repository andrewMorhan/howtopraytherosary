from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/day/Sunday")
def sunday():
    return render_template("Sunday.html")

@app.route("/day/Monday")
def monday():
    return render_template("Monday.html")

@app.route("/day/Tuesday")
def tuesday():
    return render_template("Tuesday.html")

@app.route("/day/Wednesday")
def wednesday():
    return render_template("Wednesday.html")

@app.route("/day/Thursday")
def thursday():
    return render_template("Thursday.html")

@app.route("/day/Friday")
def friday():
    return render_template("Friday.html")

@app.route("/day/Saturday")
def saturday():
    return render_template("Saturday.html")

if __name__ == "__main__":
    app.run(debug=True)