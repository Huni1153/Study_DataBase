from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo
from ledModels import ledTable

class LedForm(FlaskForm):
    red = StringField('red', validators=[DataRequired()])
    green = StringField('green', validators=[DataRequired()])
    yellow = StringField('yellow', validators=[DataRequired()])
    time = StringField('time', validators=[DataRequired()])