# Generated by Django 3.0.5 on 2020-04-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20200408_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]