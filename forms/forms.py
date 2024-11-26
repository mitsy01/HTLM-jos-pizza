from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    mark = wtforms.RadioField("Оберіть оцінку:")
    text = wtforms.TextAreaField("Напишіть свій відгук")
    owner = wtforms.StringField("Напишіть своє ім'я(можна несправжне)")
    submit = wtforms.SubmitField("Зберегти")