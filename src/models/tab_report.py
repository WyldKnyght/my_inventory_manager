# src/models/tab_reports.py
from utils.create_app import db

class ReportTab(db.Model):
    __tablename__ = 'report'
    __table_args__ = {'extend_existing': True}
    report_id = db.Column(db.String, primary_key=True)
    date = db.Column(db.Date)
    sales_total = db.Column(db.Numeric(10, 2))
    profit_total = db.Column(db.Numeric(10, 2))
    balance_sheet = db.Column(db.Text)
    stock_waiting_to_be_received = db.Column(db.Integer)

    def to_dict(self):
        return {
            'report_id': self.report_id,
            'date': str(self.date),
            'sales_total': str(self.sales_total),
            'profit_total': str(self.profit_total),
            'balance_sheet': self.balance_sheet,
            'stock_waiting_to_be_received': self.stock_waiting_to_be_received
        }