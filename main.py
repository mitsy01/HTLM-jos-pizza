from flask import Flask, render_template

import random


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", title="")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Суйгетсу", "price": 50, "ingredients": "ковбаса, сир, зелень, соус тартар"},
        {"name": "Моцарела", "price": 56, "ingredients": "сир, соус, зелень"},
        {"name": "Чотири ковбаси", "price": 47, "ingredients": "ковбаса 'Перероні', ковбаса 'Мадер', ковбаса 'Тульчин', ковбаса 'Бандерівська'"},
        {"name": "Хічіго", "price": 69, "ingredients": "полуниця, ананас, шоколад, зефір"}
    ]
    countext = {
        "pizzas": pizzas,
        "title": "Шикайне меню"
    }
    return render_template("menu.html", **countext)


@app.get("/contacts/")
def contacts():
    context = {
        "first_number": random.randint(101, 999),
        "second_number": random.randint(1001, 9999)
    }
    return render_template("contacts.html", **context)


if __name__ == "__main__":
    app.run(debug=True)