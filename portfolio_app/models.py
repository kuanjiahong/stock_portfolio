from django.db import models

from portfolio_app.custom_validators import validate_positive_number


class Portfolio(models.Model):
    stock_symbol = models.CharField(max_length=200, unique=True)
    purchased_price = models.DecimalField(max_digits=6, decimal_places=6, validators=[validate_positive_number])
    quantity = models.IntegerField(validators=[validate_positive_number])
    purchased_timestamp = models.DateTimeField('purchased_timestamp')
    total_cost = models.DecimalField(max_digits=15, decimal_places=6, validators=[validate_positive_number], default=0)

    class Meta:
        # This model is linked to this db_table
        db_table = "tbl_portfolio"
