from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    return render_template("menu.html")


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)