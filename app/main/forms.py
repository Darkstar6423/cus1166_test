# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField, TimeField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length


class TaskForm(FlaskForm):
    task_title = StringField('Title', validators=[DataRequired()])
    task_desc = TextAreaField('Description', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo', 'Todo'), ('doing', 'Doing'), ('done', 'Done')])
    task_time = StringField('Time', validators=[DataRequired()])
    task_location = StringField('Location', validators=[DataRequired()])
    task_CName = StringField('Customer', validators=[DataRequired()])
    task_duration = StringField('Duration', validators=[DataRequired()])
    task_date = ""
    submit = SubmitField('submit')
