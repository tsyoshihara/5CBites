from django.db import models


class DiningHall(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    school = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'DiningHall'


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dining_hall = models.ForeignKey(DiningHall, to_field='name', db_column='diningHall', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    day_of_week = models.CharField(max_length=20, db_column='dayOfWeek')

    class Meta:
        managed = True
        db_table = 'Meal'


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    dining_hall = models.ForeignKey(DiningHall, on_delete=models.CASCADE, to_field='name')

    class Meta:
        managed = True
        db_table = 'Dish'


class MenuItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    station = models.CharField(max_length=20)

    class Meta:
        managed = True
        unique_together = (("dish", "meal"),)
        db_table = 'MenuItem'


class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'Ingredients'


class NutritionFacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'NutritionFacts'


class DietaryRestrictions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'DietaryRestrictions'


class IngredientsInDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    class Meta:
        managed = True
        unique_together = (("dish", "ingredient"),)
        db_table = 'IngredientsInDish'


class DietaryRestrictionsOfDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    dietary_restriction = models.ForeignKey(DietaryRestrictions, on_delete=models.CASCADE)

    class Meta:
        managed = True
        unique_together = (("dish", "dietary_restriction"),)
        db_table = 'DietaryRestrictionsOfDish'


class NutritionFactsOfDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    nutrition_fact = models.ForeignKey(NutritionFacts, on_delete=models.CASCADE)
    value = models.FloatField()
    units = models.CharField(max_length=10)

    class Meta:
        managed = True
        unique_together = (("dish", "nutrition_fact"),)
        db_table = 'NutritionFactsOfDish'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    school = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    grad_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'User'


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    forks = models.FloatField()
    comment = models.TextField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    dining_hall = models.ForeignKey(DiningHall, on_delete=models.CASCADE, to_field='name')

    class Meta:
        managed = True
        db_table = 'Rating'