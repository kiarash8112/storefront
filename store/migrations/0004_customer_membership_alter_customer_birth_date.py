# Generated by Django 4.2.6 on 2023-10-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('B', 'BRONZE'), ('S', 'SILVER'), ('G', 'GOLD')], default='B', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]