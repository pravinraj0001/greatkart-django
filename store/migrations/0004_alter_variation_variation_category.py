# Generated by Django 3.2.3 on 2021-05-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], max_length=100),
        ),
    ]