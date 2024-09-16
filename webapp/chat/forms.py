from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class PhoneNumberForm(FlaskForm):
    #  phone_number = StringField('Phone Number', validators=[
    #     DataRequired(), 
    #     Length(min=10, max=15),
    #     Regexp(r'^\+?\d{10,15}$', message="Invalid phone number format.")
    # ])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    recipient =  IntegerField('Recipient', validators=[DataRequired()])
    submit = SubmitField('Send')
