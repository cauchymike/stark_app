from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class JobForm(FlaskForm):
    """The content of the form to be filled by applicants"""
    name = StringField('First Name', validators = [DataRequired()])

    last_name = StringField('Last Name', validators=[DataRequired()])

    email = StringField('Email',validators = [DataRequired(),Email(message = 'This email address is not valid')])

    phone_number =  StringField('Phone Number',

                                validators=[DataRequired(),
                                            Length(min = 11, max = 14,
                                                        message =('Your phone number is incorrect'))])

    experience = IntegerField('Years Of Experience', validators =[DataRequired(),
                                                    NumberRange(min = 2,
                                                                message =('Minimum of 2 years experience'))])

    expertise = SelectField('Field of Discipline', choices=[('sft','Software Developer'),
                                                            ('web', 'Web Developer'),('ds', 'Data Scientist')],
                            validators = [DataRequired()])

    body = TextAreaField('Tell us About You', validators=[DataRequired(), Length(min=4, message = 'Message too short')])


    submit = SubmitField('submit')


