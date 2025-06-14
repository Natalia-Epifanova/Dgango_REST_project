# Generated by Django 5.2.1 on 2025-06-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Ожидает оплаты"),
                    ("paid", "Оплачено"),
                    ("canceled", "Отменено"),
                ],
                default="pending",
                max_length=10,
                verbose_name="Статус платежа",
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="stripe_payment_link",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="payments",
            name="stripe_price_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="payments",
            name="stripe_product_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="payments",
            name="stripe_session_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("cash", "Наличные"),
                    ("transfer", "Перевод на счет"),
                    ("stripe", "Stripe"),
                ],
                max_length=10,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
