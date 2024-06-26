from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddBrandForm(FlaskForm):
    brand_id = StringField('Brand ID', validators=[DataRequired(), Length(max=128)])
    brand_name = StringField('Brand Name', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Add Brand')

