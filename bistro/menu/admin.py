from django.contrib import admin
from .models import Menu_Item, Cuisine, Category

# Register your models here.
admin.site.register(Menu_Item)
admin.site.register(Cuisine)
admin.site.register(Category)