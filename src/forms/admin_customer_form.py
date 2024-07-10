# src/forms/admin_customer_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional

class CustomerForm(FlaskForm):
    customer_id = StringField('Customer ID', validators=[DataRequired()])
    customer_name = StringField('Customer Name', validators=[DataRequired()])
    contact_information = TextAreaField('Contact Information', validators=[Optional()])