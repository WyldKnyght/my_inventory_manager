from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddCategoryForm(FlaskForm):
    category_id = StringField('Category ID', validators=[DataRequired(), Length(max=128)])
    category_name = StringField('Category Name', validators=[DataRequired(), Length(max=128)])
    category_prefix = StringField('Category Prefix', validators=[DataRequired(), Length(max=4)])
    parent_category_id = StringField('Parent Category ID', validators=[Length(max=128)])
    sub_categories_name = StringField('Sub-Categories Name', validators=[Length(max=128)])
    submit = SubmitField('Add Category')

