# src/forms/tab_sale_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, DecimalField, DateField
from wtforms.validators import DataRequired, NumberRange, Optional

class SaleTabForm(FlaskForm):
    sale_id = StringField('Sale ID', validators=[DataRequired()])
    sales_order = StringField('Sales Order', validators=[Optional()])
    product_id = SelectField('Product', validators=[DataRequired()])
    order_date = DateField('Order Date', validators=[Optional()])
    ship_delivery_pickup_date = DateField('Ship/Delivery/Pickup Date', validators=[Optional()])
    customer_id = SelectField('Customer', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[Optional(), NumberRange(min=0)])
    retail_price = DecimalField('Retail Price', places=2, validators=[Optional()])
    shipping = DecimalField('Shipping', places=2, validators=[Optional()])
    taxes = DecimalField('Taxes', places=2, validators=[Optional()])
    total_cost = DecimalField('Total Cost', places=2, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super(SaleTabForm, self).__init__(*args, **kwargs)
        # Populate choices dynamically
        self.product_id.choices = []  # Add product choices
        self.customer_id.choices = []  # Add customer choices