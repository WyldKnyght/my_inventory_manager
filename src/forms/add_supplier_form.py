from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddSupplierForm(FlaskForm):
    supplier_id = StringField('Supplier ID', validators=[DataRequired(), Length(max=128)])
    name = StringField('Name', validators=[DataRequired(), Length(max=128)])
    contact_person = StringField('Contact Person', validators=[Length(max=128)])
    address = TextAreaField('Address')
    phone = StringField('Phone', validators=[Length(max=15)])
    email = StringField('Email', validators=[Length(max=128)])
    website = StringField('Website', validators=[Length(max=128)])
    submit = SubmitField('Add Supplier')

