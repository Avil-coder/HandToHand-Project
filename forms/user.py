from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers


class RegisterForm(FlaskForm):
    phone = StringField('Телефон', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')

    def validate_phone(form, field):
        if len(field.data) > 16 or len(field.data) < 11:
            raise ValidationError('Неправильный номер телефона.')