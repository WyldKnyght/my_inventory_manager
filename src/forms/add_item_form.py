# forms/add_item_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class AddItemForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_code = StringField('Product Code', validators=[DataRequired()])
    description = TextAreaField('Description')
    category_id = SelectField('Category ID', validators=[DataRequired()])  # Assuming categories are predefined
    brand_id = SelectField('Brand ID', validators=[DataRequired()])  # Assuming brands are predefined
    size = StringField('Size')
    color = StringField('Color')
    cost_price = StringField('Cost Price')  # Consider using DecimalField for precise calculations
    markup = IntegerField('Markup', validators=[NumberRange(min=0)])
    retail_price = StringField('Retail Price')  # Consider using DecimalField for precise calculations
    product_status = SelectField('Product Status', validators=[DataRequired()])  # Assuming statuses are predefined
    notes = TextAreaField('Notes')
    supplier_id = SelectField('Supplier ID', validators=[DataRequired()])  # Assuming suppliers are predefined
    singles_in_stock = IntegerField('Singles In Stock', validators=[NumberRange(min=0)])
    cases_in_stock = IntegerField('Cases In Stock', validators=[NumberRange(min=0)])
    qty_per_case = IntegerField('Qty Per Case', validators=[NumberRange(min=1)])
    condition = StringField('Condition')

    submit = SubmitField('Add Item')