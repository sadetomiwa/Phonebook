from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, EqualTo

class AddContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone = StringField('phone', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    submit = SubmitField('Add contact')
