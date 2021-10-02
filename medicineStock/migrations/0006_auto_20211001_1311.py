# Generated by Django 3.2.7 on 2021-10-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineStock', '0005_auto_20211001_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='added_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='buying_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='due_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='selling_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='stock_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
