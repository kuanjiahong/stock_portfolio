# Generated by Django 4.0.6 on 2022-07-30 14:30

from django.db import migrations, models
import portfolio_app.custom_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=200, unique=True)),
                ('purchased_price', models.DecimalField(decimal_places=6, max_digits=6, validators=[portfolio_app.custom_validators.validate_positive_number])),
                ('quantity', models.IntegerField(validators=[portfolio_app.custom_validators.validate_positive_number])),
                ('purchased_timestamp', models.DateTimeField(verbose_name='purchased_timestamp')),
            ],
        ),
    ]