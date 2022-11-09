from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.title

class Menu_Item(models.Model):

    # class Spice_Levels(models.IntegerChoices):
    #     ZERO = 0
    #     ONE = 1
    #     TWO = 2
    #     THREE = 3
    #     FOUR = 4
    #     FIVE = 5
    ZERO = ' '
    ONE = '🌶️'
    TWO = '🌶️🌶️'
    THREE = '🌶️🌶️🌶️'
    FOUR = '🌶️🌶️🌶️🌶️'
    FIVE = '🌶️🌶️🌶️🌶️🌶️'
    SPICE_LEVEL_CHOICES=[
        (ZERO, ' '),
        (ONE, '🌶️'),
        (TWO, '🌶️🌶️'),
        (THREE, '🌶️🌶️🌶️'),
        (FOUR, '🌶️🌶️🌶️🌶️'),
        (FIVE, '🌶️🌶️🌶️🌶️🌶️'),
    ]

    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    spice_level = models.CharField(max_length=12, choices=SPICE_LEVEL_CHOICES, default=ZERO,)

    def __str__(self):
        return f"The item is {self.title}, the price is {self.price}, it's from {self.cuisine}, {self.category}, and its {self.description}"
