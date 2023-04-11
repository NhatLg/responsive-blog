from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

blog_contents = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=blog_contents)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()