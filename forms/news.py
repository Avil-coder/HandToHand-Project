from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    img = TextAreaField("Картинка")
    content = TextAreaField("Содержание")
    submit = SubmitField('Применить')