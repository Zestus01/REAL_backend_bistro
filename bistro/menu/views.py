from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from .models import Category, Cuisine, Menu_Item
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    return HttpResponse("Hello, you shouldn't be here")

def get_menu(request):

    menu = Menu_Item.objects.values()
    data = []
    for item in menu:
        item['category_id'] = model_to_dict(Category.objects.get(id=item['category_id']))
        item['cuisine_id'] = model_to_dict(Cuisine.objects.get(id=item['cuisine_id']))
        data.append(item)
    return JsonResponse(data, safe=False)

    # ## data = list(Menu_Item.objects.values('category__title'))
    # data = list(Menu_Item.objects.values())
    # return JsonResponse({'data' : data})

    # Smash Smash Smash way
    # categories = Category.objects.values()
    # cuisines = Cuisine.objects.values()
    # menu = Menu_Item.objects.values()
    # data = []
    # for item in menu:
    #     item['category_id'] = categories[item['category_id'] - 1]
    #     item['cuisine_id'] = cuisines[item['cuisine_id'] - 1]
    #     data.append(item)
    
def cuisine_get(request, cuisine_id):
    return HttpResponse("You're looking at cuisine %s." %cuisine_id)

def some_view(request):
    data = list(SomeModel.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})