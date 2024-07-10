# forms/add_inventory_status_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InventoryStatusForm(FlaskForm):
    inventory_status_id = StringField('Inventory Status ID', validators=[DataRequired(), Length(max=128)])
    status_name = StringField('Status Name', validators=[DataRequired(), Length(max=128)])
    status_prefix = StringField('Status Prefix', validators=[DataRequired(), Length(max=4)])
    submit = SubmitField('Add Status')