# Generated by Django 4.1.1 on 2022-09-28 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_strip_token_order_stripe_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]