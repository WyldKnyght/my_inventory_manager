# forms/brand_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class BrandForm(FlaskForm):
    brand_name = StringField('Brand Name', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Submit')

class BrandSearchForm(FlaskForm):
    search_term = StringField('Search', validators=[Length(max=100)])
    submit = SubmitField('Search')
