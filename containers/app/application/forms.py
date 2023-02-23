from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired, NumberRange


class TryForm(FlaskForm):
    try_number = StringField(label=None,
                             validators=[Length(min=3, max=3), DataRequired()])
    submit_button = SubmitField(label='Try')


class NewGameForm(FlaskForm):
    start = SubmitField(label='Start new game')
