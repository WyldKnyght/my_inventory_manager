# forms/add_supplier_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional, URL

class AddSupplierForm(FlaskForm):
    supplier_id = StringField('Supplier ID', validators=[DataRequired(), Length(max=128)])
    name = StringField('Name', validators=[DataRequired(), Length(max=128)])
    contact_person = StringField('Contact Person', validators=[Optional(), Length(max=128)])
    address = TextAreaField('Address', validators=[Optional()])
    phone = StringField('Phone', validators=[Optional(), Length(max=15)])
    email = StringField('Email', validators=[Optional(), Email(), Length(max=128)])
    website = StringField('Website', validators=[Optional(), URL(), Length(max=128)])
    submit = SubmitField('Add Supplier')