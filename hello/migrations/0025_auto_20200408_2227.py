# Generated by Django 3.0.5 on 2020-04-08 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0024_auto_20200408_2220'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dietaryrestrictionsofdish',
            unique_together={('dish', 'dietary_restriction')},
        ),
        migrations.AlterUniqueTogether(
            name='ingredientsindish',
            unique_together={('dish', 'ingredient')},
        ),
    ]