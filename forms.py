from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL


# class RegisterForm(FlaskForm):
#     email = StringField("Email:", validators=[DataRequired()])
#     password = PasswordField("Password:", validators=[DataRequired()])
#     name = StringField("Name:", validators=[DataRequired()])
#     occupation = StringField("Your Occupation", validators=[DataRequired()])
#     address = StringField("Residence", validators=[DataRequired()])
#     qualification = StringField("Highest Degree")
#     zodiac = StringField("Zodiac")
#     height = StringField("Height")
#     status = StringField("Social Status")
#     fav_food = StringField("Favorite Food")
#     languages = StringField("Languages you know", validators=[DataRequired()])
#     passion = StringField("Passions")
#     submit = SubmitField("Sign me up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Log me in!")
