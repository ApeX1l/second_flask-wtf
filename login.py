from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username_astronaut = StringField('Id Астронавта ', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    username_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
