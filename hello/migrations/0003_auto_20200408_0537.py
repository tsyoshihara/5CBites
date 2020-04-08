# Generated by Django 3.0.5 on 2020-04-08 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20200408_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryRestrictions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'DietaryRestrictions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Dish',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Ingredients',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('hours', models.CharField(max_length=20)),
                ('day_of_week', models.CharField(db_column='dayOfWeek', max_length=20)),
            ],
            options={
                'db_table': 'Meal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'NutritionFacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('grad_year', models.IntegerField()),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.AlterModelTable(
            name='dininghall',
            table='DiningHall',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('forks', models.FloatField()),
                ('comment', models.TextField()),
                ('dining_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.DiningHall')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Dish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.User')),
            ],
            options={
                'db_table': 'Rating',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NutritionFactsOfDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=10)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Dish')),
                ('nutrition_fact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.NutritionFacts')),
            ],
            options={
                'db_table': 'NutritionFactsOfDish',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=20)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Dish')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Meal')),
            ],
            options={
                'db_table': 'MenuItem',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='dining_hall',
            field=models.ForeignKey(db_column='diningHall', on_delete=django.db.models.deletion.CASCADE, to='hello.DiningHall'),
        ),
        migrations.CreateModel(
            name='IngredientsInDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Dish')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Ingredients')),
            ],
            options={
                'db_table': 'IngredientsInDish',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DietaryRestrictionsOfDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dietary_restrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.DietaryRestrictions')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Dish')),
            ],
            options={
                'db_table': 'DietaryRestrictionsOfDish',
                'managed': True,
            },
        ),
    ]