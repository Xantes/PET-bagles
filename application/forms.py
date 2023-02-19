from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired

class TryForm(FlaskForm):
    try_number = StringField(label='Number for try', validators=[Length(min=3, max=3), DataRequired()])
    submit_button = SubmitField(label='TRY')

class NewGameForm(FlaskForm):
    start = SubmitField(label='new_game')