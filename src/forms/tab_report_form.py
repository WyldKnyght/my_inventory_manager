# forms/report_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField, DateField
from wtforms.validators import DataRequired, Optional

class ReportTabForm(FlaskForm):
    report_id = StringField('Report ID', validators=[DataRequired()])
    date = DateField('Date', validators=[Optional()])
    sales_total = DecimalField('Sales Total', places=2, validators=[Optional()])
    profit_total = DecimalField('Profit Total', places=2, validators=[Optional()])
    balance_sheet = TextAreaField('Balance Sheet', validators=[Optional()])
    stock_waiting_to_be_received = IntegerField('Stock Waiting to be Received', validators=[Optional(), NumberRange(min=0)])