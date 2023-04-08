from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()