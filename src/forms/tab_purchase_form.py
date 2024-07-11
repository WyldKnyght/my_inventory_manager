# src/forms/tab_purchase_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DecimalField, DateField
from wtforms.validators import DataRequired, NumberRange, Optional

class PurchaseTabForm(FlaskForm):
    purchase_id = StringField('Purchase ID', validators=[DataRequired()])
    purchase_order = StringField('Purchase Order', validators=[Optional()])
    order_number = StringField('Order Number', validators=[Optional()])
    product_id = SelectField('Product', validators=[DataRequired()])
    purchase_date = DateField('Purchase Date', validators=[Optional()])
    shipping_date = DateField('Shipping Date', validators=[Optional()])
    shipping_tracking_number = StringField('Shipping Tracking Number', validators=[Optional()])
    supplier_id = SelectField('Supplier', validators=[DataRequired()])
    singles_quantity = IntegerField('Singles Quantity', validators=[Optional(), NumberRange(min=0)])
    cases_quantity = IntegerField('Cases Quantity', validators=[Optional(), NumberRange(min=0)])
    product_status = SelectField('Product Status', validators=[DataRequired()])
    payment_method = StringField('Payment Method', validators=[Optional()])
    currency = StringField('Currency', validators=[Optional()])
    exchange_rate = DecimalField('Exchange Rate', places=4, validators=[Optional()])
    cost_price = DecimalField('Cost Price', places=2, validators=[Optional()])
    discount = DecimalField('Discount', places=2, validators=[Optional()])
    shipping = DecimalField('Shipping', places=2, validators=[Optional()])
    taxes = DecimalField('Taxes', places=2, validators=[Optional()])
    total_cost = DecimalField('Total Cost', places=2, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super(PurchaseTabForm, self).__init__(*args, **kwargs)
        # Populate choices dynamically
        self.product_id.choices = []  # Add product choices
        self.supplier_id.choices = []  # Add supplier choices
        self.product_status.choices = []  # Add status choices
