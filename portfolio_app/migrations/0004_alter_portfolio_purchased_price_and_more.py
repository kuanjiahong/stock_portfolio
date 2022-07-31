# Generated by Django 4.0.6 on 2022-07-31 01:53

from django.db import migrations, models
import portfolio_app.custom_validators


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_portfolio_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='purchased_price',
            field=models.DecimalField(decimal_places=6, max_digits=19, validators=[portfolio_app.custom_validators.validate_positive_number]),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='total_cost',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=19, validators=[portfolio_app.custom_validators.validate_positive_number]),
        ),
    ]
