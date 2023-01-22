from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PoknameForm(FlaskForm):
    pokname = StringField("Username", validators = [DataRequired()])
    submit = SubmitField()