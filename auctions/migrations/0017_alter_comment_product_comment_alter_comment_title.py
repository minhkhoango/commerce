# Generated by Django 5.1.4 on 2025-01-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_product_current_bidder_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product_comment',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]