from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    seats = StringField("Seats", validators=[DataRequired()])
    has_toilet = BooleanField("Has Toilet")
    has_wifi = BooleanField("Has WiFi")
    has_sockets = BooleanField("Has Sockets")
    can_take_calls = BooleanField("Can Take Calls")
    coffee_price = StringField("Coffee Price")
    add_cafe = SubmitField("Add Cafe ")


class RegisterForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")

