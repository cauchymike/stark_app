from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange


app = Flask(__name__)
app.config['SECRET_KEY'] = 'seunmelody-is-my-secret-key'


#################################################################################
#form section
###########################################################################

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


##################################################################################
#view section
#################################################################################

@app.route('/', methods = ('GET', 'POST'))
def jobformm():
    form = JobForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return  render_template('index.html', form = form)

@app.route('/success')
def success():
    return 'Application Received, We will contact you soon'







if __name__ == '__main__':
    app.run(debug=False)



