from flask import Blueprint, render_template, request, redirect, url_for

from models.base import Session
from models.reviews import Review


review_route = Blueprint("reviews", __name__)

@app.route("/review/", methods=["GET", "POST"])
def add_review():
    with Session() as session:
        form = ReviewForm()
        marks = session.query(Mark).all()
        if request.method == "POST":
            mark_id = form.mark.data
            text = form.text.data
            owner = form.owner.data
            
            review = Review(text=text, owner=owner, mark_id=mark_id)
            session.add(review)
            session.commit()
            return redirect("/reviews/")
        
        form.mark.choices = []
        for mark in marks:
            form.mark.choices.append((mark.id, mark.value))
            
        return render_template("add_review.html", form=form)
    
@app.get("/reviews/")
def show_reviews():
    with Session() as session:
        reviews = session.query(Review).all()
        return render_template("reviews.html", reviews=reviews)

