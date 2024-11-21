from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    mark = wtforms.RadioField("")
    text = wtforms.TextAreaField("")
    owner = wtforms.StringField("")
    submit = wtforms.SubmitField("")