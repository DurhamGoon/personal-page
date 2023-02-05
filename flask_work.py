from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/projects/")
def projects():
    return render_template("projects.html",title="Projects")

if __name__ == '__main__':
    app.run(debug=True)