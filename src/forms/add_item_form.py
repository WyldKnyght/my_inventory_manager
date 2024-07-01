# forms/add_item_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Optional

class AddItemForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_code = StringField('Product Code', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    category_id = SelectField('Category', validators=[DataRequired()])
    brand_id = SelectField('Brand', validators=[DataRequired()])
    size = StringField('Size', validators=[Optional()])
    color = StringField('Color', validators=[Optional()])
    cost_price = DecimalField('Cost Price', places=2, validators=[Optional()])
    markup = IntegerField('Markup', validators=[Optional(), NumberRange(min=0)])
    retail_price = DecimalField('Retail Price', places=2, validators=[Optional()])
    product_status = SelectField('Product Status', validators=[DataRequired()])
    notes = TextAreaField('Notes', validators=[Optional()])
    supplier_id = SelectField('Supplier', validators=[DataRequired()])
    singles_in_stock = IntegerField('Singles In Stock', validators=[Optional(), NumberRange(min=0)])
    cases_in_stock = IntegerField('Cases In Stock', validators=[Optional(), NumberRange(min=0)])
    qty_per_case = IntegerField('Qty Per Case', validators=[Optional(), NumberRange(min=1)])
    condition = StringField('Condition', validators=[Optional()])

    submit = SubmitField('Add Item')

    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)
        # Populate choices dynamically
        self.category_id.choices = []  # Add category choices
        self.brand_id.choices = []  # Add brand choices
        self.product_status.choices = []  # Add status choices
        self.supplier_id.choices = []  # Add supplier choices