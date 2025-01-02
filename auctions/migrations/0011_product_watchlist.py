# Generated by Django 5.1.4 on 2025-01-02 04:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
