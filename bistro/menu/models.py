from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

class Menu_Item(models.Model):

    class Spice_Levels(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    description = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    spice_level = models.IntegerField(choices=Spice_Levels.choices)

    def __str__(self):
        return f"The item is {self.title}, the price is {self.price}, it's from {self.cuisine}, {self.category}, and its {self.description}"
